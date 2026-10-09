"""Detección automática de hardware: GPU CUDA, Apple Silicon (MPS) o CPU.

Diseñado para funcionar igual en Google Colab, macOS y Linux local.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import torch


@dataclass
class HardwareInfo:
    """Snapshot del hardware disponible para entrenamiento."""

    device: str                      # "cuda" | "mps" | "cpu"
    device_name: str                 # p.ej. "NVIDIA A100-SXM4-40GB"
    total_vram_gb: float | None      # None si no hay GPU NVIDIA
    supports_bf16: bool              # Ampere+ (A100, L4); la T4 solo fp16
    is_colab: bool
    recommended_profile: str         # "small" | "large"
    recommended_precision: str       # "bf16" | "fp16" | "fp32"
    notes: list[str] = field(default_factory=list)


def is_running_in_colab() -> bool:
    """Detecta si el proceso corre dentro de Google Colab."""
    try:
        import google.colab  # noqa: F401
        return True
    except ImportError:
        return False


def get_device() -> torch.device:
    """Devuelve el mejor device disponible: cuda > mps > cpu."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def detect_hardware(verbose: bool = True) -> HardwareInfo:
    """Inspecciona el hardware y recomienda perfil (small/large) y precisión.

    Reglas:
    - GPU con >= 24 GB y soporte bf16 (A100/L4)  -> perfil "large", bf16
    - GPU con < 24 GB (T4 de Colab Free, 16 GB)  -> perfil "small", fp16
    - MPS (Apple Silicon) o CPU                  -> perfil "small", fp32
    """
    notes: list[str] = []
    colab = is_running_in_colab()

    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        vram_gb = props.total_memory / 1024**3
        bf16 = torch.cuda.is_bf16_supported()
        profile = "large" if (vram_gb >= 24 and bf16) else "small"
        precision = "bf16" if bf16 else "fp16"
        info = HardwareInfo(
            device="cuda",
            device_name=props.name,
            total_vram_gb=round(vram_gb, 1),
            supports_bf16=bf16,
            is_colab=colab,
            recommended_profile=profile,
            recommended_precision=precision,
            notes=notes,
        )
        if not bf16:
            notes.append(
                "GPU sin bf16 (pre-Ampere): usar fp16 con GradScaler para evitar overflow."
            )
    elif torch.backends.mps.is_available():
        info = HardwareInfo(
            device="mps",
            device_name="Apple Silicon (MPS)",
            total_vram_gb=None,
            supports_bf16=False,
            is_colab=False,
            recommended_profile="small",
            recommended_precision="fp32",
            notes=["MPS no soporta todos los kernels; algunos ops caen a CPU."],
        )
    else:
        info = HardwareInfo(
            device="cpu",
            device_name="CPU",
            total_vram_gb=None,
            supports_bf16=False,
            is_colab=colab,
            recommended_profile="small",
            recommended_precision="fp32",
            notes=["Sin GPU: usar versiones SMALL y reducir max_steps."],
        )

    if verbose:
        print(f"🖥️  Device: {info.device} ({info.device_name})")
        if info.total_vram_gb is not None:
            print(f"💾 VRAM total: {info.total_vram_gb} GB | bf16: {info.supports_bf16}")
        print(f"📍 Colab: {info.is_colab}")
        print(f"✅ Perfil recomendado: {info.recommended_profile.upper()} "
              f"({info.recommended_precision})")
        for note in info.notes:
            print(f"⚠️  {note}")

    return info


def gpu_memory_snapshot() -> dict[str, float]:
    """Devuelve uso actual de VRAM en GB (solo CUDA). Útil para monitoreo."""
    if not torch.cuda.is_available():
        return {}
    return {
        "allocated_gb": round(torch.cuda.memory_allocated() / 1024**3, 3),
        "reserved_gb": round(torch.cuda.memory_reserved() / 1024**3, 3),
        "max_allocated_gb": round(torch.cuda.max_memory_allocated() / 1024**3, 3),
    }
