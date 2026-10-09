# Bibliografía y Fuentes del Corpus — Índice Maestro

> Bibliografía de referencia por dominio. **Importante:** los libros guían qué temas y vocabulario debe cubrir el corpus, pero **su texto no se ingiere**. Las fuentes que de verdad entran al corpus están en [`configs/data.yaml`](../configs/data.yaml) (resumen abajo). Organizada por los 26 dominios de [`configs/corpus.yaml`](../configs/corpus.yaml). Cada dominio tiene su ficha detallada en [`docs/bibliografia/`](bibliografia/).

## Metodología de selección

Un libro no entra al corpus de un LLM por "ser bueno", sino por **qué le aporta al modelo**. Cada fuente se evalúa en cuatro ejes:

1. **Conocimiento conceptual.** ¿Cubre el modelo mental del dominio (definiciones, teoremas, arquitecturas, patrones)? Un LLM que nunca vio la derivación del descenso de gradiente no puede razonar sobre por qué diverge un entrenamiento.
2. **Vocabulario técnico.** Cada dominio tiene un léxico propio (*posterior*, *quorum*, *frente de Pareto*, *bounded context*). El modelo solo genera con fluidez los términos que vio en contexto suficiente. Por eso cada ficha lista vocabulario representativo.
3. **Tipo de razonamiento.** Derivaciones matemáticas, análisis de trade-offs, debugging, diseño, demostraciones formales. La **diversidad de registros de razonamiento** es lo que hace a un modelo versátil; un corpus de solo tutoriales produce un modelo que solo sabe seguir recetas.
4. **Registro textual.** Prosa matemática densa (Bishop), teorema-demostración (Lynch), narrativa (The Phoenix Project), especificación declarativa (OpenAPI), código comentado. Mezclar registros mejora la generalización.

Cada dominio aporta **9 libros** (3 fundamentales, 3 avanzados, 3 prácticos) + papers + documentación oficial + blogs + repos + benchmarks + datasets. La estructura fija facilita el balanceo y el control de calidad del corpus (Fase 3).

> **Nota de licencias.** Listar un libro como *referencia de conocimiento* no implica derecho a incluir su texto íntegro en el corpus. La distinción es crítica: los libros guían **qué temas y vocabulario** debe cubrir el corpus; el **texto** se obtiene de fuentes con licencia adecuada (documentación oficial, papers de acceso abierto, dumps con licencia explícita, o datos sintéticos generados a partir del conocimiento). Cada ficha marca con *"verificar licencia"* lo que no es claramente reutilizable.

## Resumen de dominios

| Dominio | Peso | Ficha | Núcleo |
|---------|:----:|-------|--------|
| Estadística | 1.5 | [estadistica](bibliografia/estadistica.md) | Casella & Berger · Wasserman · Gelman (BDA) |
| Optimización | 1.5 | [optimizacion](bibliografia/optimizacion.md) | Boyd & Vandenberghe · Nocedal & Wright |
| Metaheurísticas | 1.5 | [metaheuristica](bibliografia/metaheuristica.md) | Luke · Eiben & Smith · Talbi · Deb |
| Ciencia de Datos | 1.5 | [ciencia_datos](bibliografia/ciencia_datos.md) | McKinney · VanderPlas · Wickham |
| Analítica y BI | 1.5 | [analitica](bibliografia/analitica.md) | Kimball · Provost & Fawcett · Kohavi |
| Inteligencia Artificial | 1.5 | [inteligencia_artificial](bibliografia/inteligencia_artificial.md) | Russell & Norvig · Sutton & Barto |
| LLMs | 1.5 | [llm](bibliografia/llm.md) | Raschka · Jurafsky & Martin · Tunstall et al. · Huyen |
| Desarrollo Full Stack | 1.5 | [full_stack](bibliografia/full_stack.md) | Eloquent JS · Full Stack Open · Learning React |
| Filosofía | 1.5 | [filosofia](bibliografia/filosofia.md) | Russell · Kenny · Kant · Aristóteles · Kuhn |
| Música | 1.5 | [musica](bibliografia/musica.md) | Kostka · Aldwell & Schachter · Levine · Müller |
| Machine Learning | 1.2 | [machine_learning](bibliografia/machine_learning.md) | Bishop · ESL · Murphy · Géron |
| Deep Learning | 1.2 | [deep_learning](bibliografia/deep_learning.md) | Goodfellow · Prince · Zhang (d2l) |
| Matemáticas | 1.2 | [matematicas](bibliografia/matematicas.md) | Strang · Axler · Rudin |
| Python | 1.2 | [python](bibliografia/python.md) | Ramalho · Beazley |
| Programación | 1.0 | [programacion](bibliografia/programacion.md) | SICP · CLRS · Pragmatic Programmer |
| PostgreSQL | 1.0 | [postgresql](bibliografia/postgresql.md) | docs oficiales · Up and Running |
| MongoDB | 1.0 | [mongodb](bibliografia/mongodb.md) | The Definitive Guide · docs |
| AWS | 1.0 | [aws](bibliografia/aws.md) | Well-Architected · docs oficiales |
| Serverless Framework | 1.0 | [serverless](bibliografia/serverless.md) | Serverless Architectures on AWS · docs |
| Infraestructura como Código | 1.0 | [iac](bibliografia/iac.md) | Terraform Up & Running |
| APIs | 1.0 | [apis](bibliografia/apis.md) | RESTful Web APIs · API Design Patterns · FastAPI |
| Arquitectura de Software | 1.0 | [arquitectura_software](bibliografia/arquitectura_software.md) | Clean Architecture · DDIA · DDD |
| DevOps | 1.0 | [devops](bibliografia/devops.md) | DevOps Handbook · SRE · Accelerate |
| Data Engineering | 1.0 | [data_engineering](bibliografia/data_engineering.md) | Fundamentals of DE · Kimball |
| Sistemas Distribuidos | 1.0 | [sistemas_distribuidos](bibliografia/sistemas_distribuidos.md) | DDIA · Tanenbaum · Raft/Paxos |
| Ingeniería Eléctrica | 1.0 | [ingenieria_electrica](bibliografia/ingenieria_electrica.md) | Sadiku · Hayt · Sedra-Smith · Chapman |

Los pesos se aplican al construir el corpus (`scripts/build_pretrain_corpus.py`): en las fuentes mixtas, un documento del dominio *d* se acepta con probabilidad w_d / max(w). Se priorizan (1.5) estadística, optimización, metaheurísticas, ciencia de datos, analítica, IA, LLMs, full stack, filosofía y música.

## Fuentes que SÍ usa el corpus (`configs/data.yaml`)

| Fuente | Dataset HF | Licencia | Filtro aplicado |
|--------|-----------|----------|-----------------|
| Wikipedia ES / EN | `wikimedia/wikipedia` (20231101.es / .en) | CC BY-SA | léxico de dominio (≥4 / ≥5 términos) |
| FineWeb-2 español | `HuggingFaceFW/fineweb-2` (spa_Latn) | ODC-BY | léxico (≥5) |
| FineWeb-Edu | `HuggingFaceFW/fineweb-edu` (sample-10BT) | ODC-BY | `int_score ≥ 3` + léxico (≥4) |
| Cosmopedia v2 | `HuggingFaceTB/smollm-corpus` (cosmopedia-v2) | ver ficha del dataset | léxico (≥3) |
| OpenWebMath | `open-web-math/open-web-math` | ODC-BY | ninguno (todo es matemática) |
| arXiv abstracts | `gfissore/arxiv-abstracts-2021` | metadatos de arXiv (CC0) | categorías (stat.*, math.OC, cs.NE, cs.LG, cs.CL, cs.SD…) |
| Código Python | `codeparrot/codeparrot-clean` | la de cada repo | solo MIT/Apache/BSD/ISC/Unlicense/CC0; sin autogenerado |
| Corpus personal | local (`configs/personal.yaml`) | tuyo | secretos y correos redactados; nunca se versiona |
| Corpus semilla | local (`scripts/seed_documents.py`) | propio | — |

## Otras fuentes de referencia (no usadas hoy)

The Pile, Stack Exchange dumps, documentación oficial de PostgreSQL/AWS/etc. y Proyecto Gutenberg son
candidatas para ampliar el corpus; **no** están en `configs/data.yaml`. Antes de añadirlas, revisa su licencia.

### Consideraciones legales y éticas

- **Atribución CC BY-SA:** Wikipedia y Stack Exchange exigen atribución y *share-alike*; el corpus derivado hereda obligaciones. Documentar la procedencia en `metadata.source`/`metadata.license` de cada documento (ver [schema](../datasets/schemas/document.schema.json)).
- **Código con licencia:** `code_python` acepta solo licencias permisivas (`allowed_licenses` en `configs/data.yaml`); GPL/copyleft queda fuera.
- **PII y contenido sensible:** hoy solo el corpus personal pasa por redacción de secretos y correos (`collect_personal_corpus.py`); las fuentes públicas no tienen filtro de PII ni de toxicidad (pendiente). El notebook 08 enseña evaluación de toxicidad y sesgo.
- **Contaminación de benchmarks:** si evalúas con benchmarks públicos (MMLU, etc.), ten presente que el corpus web puede contenerlos; no hay descontaminación automática.
- **Datos sintéticos:** cuando el conocimiento esté en libros no reutilizables, generar Q&A sintéticos *a partir* del conocimiento (no copia textual), documentando `source: sintetico` y vigilando *model collapse*.

## Próximos pasos

1. Añadir fuentes con licencia clara para los dominios con poca cobertura web (p. ej. analítica, full stack).
2. Filtro de PII y toxicidad para las fuentes públicas.
3. Generar SFT sintético a partir del conocimiento de los libros (sin copia textual) para ampliar `datasets/sft`.
