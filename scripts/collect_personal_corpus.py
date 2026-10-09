"""Recolecta TU corpus personal: tesis, artículos, notebooks, código y libros propios.

Lee las carpetas de ``configs/personal.yaml``, extrae texto de .md/.tex/.txt/
.py/.ipynb/.scala/.sql/.pdf/.docx, redacta secretos y correos, deduplica por
hash y escribe ``datasets/raw/personal/personal.jsonl`` (ignorado por git).

    python scripts/collect_personal_corpus.py            # usa PERSONAL_ROOT o ..
    PERSONAL_ROOT=/personal python scripts/collect_personal_corpus.py   # devcontainer

Notebooks: se conservan celdas markdown y de código (sin outputs).
PDFs: pypdf; DOCX: python-docx (opcionales — si faltan, se omiten esos archivos).
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from llm_lab.data.cleaning import normalize_text  # noqa: E402
from llm_lab.data.domains import DomainClassifier  # noqa: E402
from llm_lab.utils.config import load_yaml  # noqa: E402

OUT = ROOT / "datasets" / "raw" / "personal" / "personal.jsonl"

# ── Redacción de secretos ──────────────────────────────────────────
_SECRET_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "<AWS_KEY>"),
    (re.compile(r"(?i)aws_secret_access_key\s*[=:]\s*\S+"), "aws_secret_access_key=<REDACTED>"),
    (re.compile(r"hf_[A-Za-z0-9]{30,}"), "<HF_TOKEN>"),
    (re.compile(r"sk-[A-Za-z0-9_\-]{20,}"), "<API_KEY>"),
    (re.compile(r"ghp_[A-Za-z0-9]{30,}|glpat-[A-Za-z0-9_\-]{20,}"), "<GIT_TOKEN>"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S),
     "<PRIVATE_KEY>"),
    (re.compile(r"(?i)\b(password|passwd|secret|token|api[_-]?key)\b(\s*[=:]\s*)(['\"])[^'\"]{6,}\3"),
     r"\1\2\3<REDACTED>\3"),
    (re.compile(r"(?i)(postgres(?:ql)?|mongodb(?:\+srv)?|mysql)://[^\s'\"]+"), r"\1://<REDACTED>"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "<EMAIL>"),
]


def redact(text: str) -> tuple[str, int]:
    n = 0
    for pattern, repl in _SECRET_PATTERNS:
        text, k = pattern.subn(repl, text)
        n += k
    return text, n


# ── Extractores por extensión ──────────────────────────────────────
def read_notebook(path: Path) -> str:
    nb = json.loads(path.read_text(encoding="utf-8"))
    parts = []
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        parts.append(src if cell.get("cell_type") == "markdown" else f"```python\n{src}\n```")
    return "\n\n".join(parts)


def read_pdf(path: Path, max_pages: int) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = [p.extract_text() or "" for p in reader.pages[:max_pages]]
    return "\n".join(pages)


def read_docx(path: Path) -> str:
    import docx

    return "\n".join(p.text for p in docx.Document(str(path)).paragraphs)


def read_tex(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Quita comentarios LaTeX (% no escapado) pero conserva las ecuaciones.
    return re.sub(r"(?<!\\)%.*", "", text)


def extract(path: Path, max_pdf_pages: int) -> str:
    ext = path.suffix.lower()
    if ext == ".ipynb":
        return read_notebook(path)
    if ext == ".pdf":
        return read_pdf(path, max_pdf_pages)
    if ext == ".docx":
        return read_docx(path)
    if ext == ".tex":
        return read_tex(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def iter_files(root: Path, cfg: dict, exclude: list[str]):
    skip_dirs = set(cfg["skip_dirs"])
    exts = set(cfg["extensions"])
    max_bytes = cfg["max_file_mb"] * 1024**2
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs and not d.startswith(".")]
        for fn in filenames:
            path = Path(dirpath) / fn
            rel = path.relative_to(root).as_posix()
            if path.suffix.lower() not in exts:
                continue
            if any(fnmatch.fnmatch(fn.lower(), pat) for pat in cfg["skip_files"]):
                continue
            if any(fnmatch.fnmatch(rel, pat.removeprefix("**/")) or fnmatch.fnmatch(rel, pat)
                   for pat in exclude):
                continue
            if path.stat().st_size > max_bytes:
                continue
            yield path


def main() -> None:
    cfg = load_yaml("personal")
    os.environ.setdefault("PERSONAL_ROOT", str(ROOT.parent))
    classifier = DomainClassifier()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    seen: set[str] = set()
    stats: Counter = Counter()
    redactions = 0
    missing_libs: set[str] = set()

    with OUT.open("w", encoding="utf-8") as out:
        for entry in cfg["roots"]:
            root = Path(os.path.expandvars(entry["path"]))
            if not root.is_absolute():
                root = (ROOT / root).resolve()
            if not root.exists():
                print(f"⚠️  No existe {root} — se omite")
                continue
            n_before = stats["docs"]
            for path in iter_files(root, cfg, entry.get("exclude", [])):
                try:
                    raw = extract(path, cfg["max_pdf_pages"])
                except ImportError as exc:
                    missing_libs.add(exc.name or str(exc))
                    continue
                except Exception as exc:  # PDFs corruptos, encodings raros, etc.
                    stats["errores"] += 1
                    print(f"   ✗ {path.name}: {exc.__class__.__name__}")
                    continue
                code_like = path.suffix.lower() in {".py", ".scala", ".sql"}
                text = raw.strip() if code_like else normalize_text(raw)
                if len(text) < cfg["min_chars"]:
                    continue
                text, k = redact(text)
                redactions += k
                h = hashlib.sha256(text.encode()).hexdigest()
                if h in seen:
                    stats["duplicados"] += 1
                    continue
                seen.add(h)
                match = classifier.classify(text)
                domain = match.domain if match.total_hits >= 3 else entry.get("domain_hint", "general")
                out.write(json.dumps({
                    "id": f"sha256:{h}",
                    "text": text,
                    "domain": domain,
                    "path": path.relative_to(root.parent).as_posix(),
                    "ext": path.suffix.lower(),
                }, ensure_ascii=False) + "\n")
                stats["docs"] += 1
                stats["chars"] += len(text)
                stats[f"ext{path.suffix.lower()}"] += 1
            print(f"✓ {root}: {stats['docs'] - n_before} documentos")

    print(f"\n📄 {stats['docs']} documentos · ~{stats['chars'] / 4 / 1e6:.2f} M tokens "
          f"· {stats['duplicados']} duplicados · {redactions} secretos/correos redactados")
    print("   por extensión:", {k[3:]: v for k, v in stats.items() if k.startswith("ext")})
    if missing_libs:
        print(f"⚠️  Faltan librerías opcionales {missing_libs}: pip install pypdf python-docx")
    print(f"→ {OUT}")


if __name__ == "__main__":
    main()
