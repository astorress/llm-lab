# Bibliografía — Data Engineering

> Dominio `data_engineering` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Fundamentals of Data Engineering | J. Reis, M. Housley | 2022 | 3 | 5 | Alta | 5 | 1 |
| F2 | Designing Data-Intensive Applications | M. Kleppmann | 2017 | 4 | 5 | Alta | 5 | 2 |
| F3 | The Data Warehouse Toolkit (3ª ed.) | R. Kimball, M. Ross | 2013 | 3 | 4 | Alta | 5 | 1 |

#### F1 — *Fundamentals of Data Engineering*
- **Cobertura conceptual:** ciclo de vida de la ingeniería de datos (generación, ingestión, transformación, serving), arquitecturas modernas, undercurrents.
- **Cobertura práctica:** diseñar pipelines y elegir herramientas según requisitos, no por moda.
- **Valor como guía para el LLM:** el texto de referencia moderno del campo; vocabulario actualizado y estructurado.
- **Conocimiento que aporta:** el marco conceptual unificado de data engineering (2022).
- **Vocabulario técnico:** *data lifecycle*, *ELT*, *batch/micro-batch/streaming*, *idempotencia*, *data contract*, *medallion*.
- **Razonamiento que aporta:** decisiones de arquitectura de datos por trade-offs (build vs buy, batch vs stream).

#### F2 — *Designing Data-Intensive Applications*
- **Cobertura conceptual:** almacenamiento, encoding, replicación, batch (MapReduce) y stream processing, derivación de datos.
- **Cobertura práctica:** entender los fundamentos de los sistemas que mueven datos a escala.
- **Valor como guía para el LLM:** fundamento teórico compartido con arquitectura y sistemas distribuidos.
- **Conocimiento que aporta:** la base de sistemas que sostiene cualquier pipeline serio.
- **Vocabulario técnico:** *log*, *CDC*, *derived data*, *MapReduce*, *dataflow*, *unbundling the database*.
- **Razonamiento que aporta:** razonamiento sobre integridad y flujo de datos extremo a extremo.

#### F3 — *The Data Warehouse Toolkit*
- **Cobertura conceptual:** modelado dimensional, esquemas estrella/copo de nieve, tablas de hechos y dimensiones, SCD.
- **Cobertura práctica:** modelar un data warehouse analítico correcto y consultable.
- **Valor como guía para el LLM:** el canon del modelado analítico; vocabulario presente en todo BI/DW.
- **Conocimiento que aporta:** modelado dimensional, ausente en los textos más nuevos.
- **Vocabulario técnico:** *fact table*, *dimension*, *star schema*, *slowly changing dimension*, *grain*, *conformed dimension*.
- **Razonamiento que aporta:** diseño de modelos analíticos orientados a consulta.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Streaming Systems | T. Akidau, S. Chernyak, R. Lax | 2018 | 4 | 4 | Alta | 5 | 2 |
| A2 | Data Pipelines Pocket Reference | J. Densmore | 2021 | 2 | 3 | Media | 4 | 1 |
| A3 | Spark: The Definitive Guide | B. Chambers, M. Zaharia | 2018 | 3 | 4 | Media | 4 | 1 |

#### A1 — *Streaming Systems*
- **Cobertura conceptual:** modelo Dataflow, tiempo de evento, watermarks, ventanas, triggers, exactly-once.
- **Cobertura práctica:** diseñar pipelines de streaming correctos bajo desorden temporal.
- **Valor como guía para el LLM:** semántica formal del streaming, vocabulario compartido con sistemas distribuidos.
- **Conocimiento que aporta:** el tratamiento riguroso del procesamiento de flujos.
- **Vocabulario técnico:** *watermark*, *event/processing time*, *windowing*, *trigger*, *accumulation mode*.
- **Razonamiento que aporta:** razonamiento sobre completitud vs latencia en streams.

#### A2 — *Data Pipelines Pocket Reference*
- **Cobertura conceptual:** extracción, carga, transformación, orquestación, validación, patrones ELT.
- **Cobertura práctica:** construir un pipeline ELT funcional de principio a fin.
- **Valor como guía para el LLM:** ejemplos concretos y código — registro práctico conciso.
- **Conocimiento que aporta:** la mecánica concreta de un pipeline ELT moderno.
- **Vocabulario técnico:** *incremental extraction*, *idempotent load*, *orchestration DAG*, *data validation*.
- **Razonamiento que aporta:** debugging y diseño práctico de pipelines.

#### A3 — *Spark: The Definitive Guide*
- **Cobertura conceptual:** RDDs, DataFrames, Spark SQL, Structured Streaming, particionamiento, tuning.
- **Cobertura práctica:** procesar datos a gran escala con Spark con buen rendimiento.
- **Valor como guía para el LLM:** vocabulario de procesamiento distribuido de datos muy usado en la industria.
- **Conocimiento que aporta:** el motor de procesamiento batch/stream más extendido.
- **Vocabulario técnico:** *RDD*, *shuffle*, *catalyst*, *partition*, *broadcast join*, *lazy evaluation*.
- **Razonamiento que aporta:** optimización de jobs distribuidos y diagnóstico de cuellos de botella.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | The dbt / Analytics Engineering Guide (dbt Labs) | dbt Labs | 2023 | 2 | 4 | Alta | 4 | 1 |
| P2 | Data Engineering with Python | P. Crickard | 2020 | 2 | 3 | Media | 3 | 1 |
| P3 | 97 Things Every Data Engineer Should Know | T. Macey (ed.) | 2021 | 2 | 2 | Baja | 3 | 1 |

#### P1 — *Analytics Engineering / dbt*
- **Cobertura conceptual:** transformación en el warehouse, modelado modular, tests, documentación, lineage.
- **Cobertura práctica:** construir capas de transformación versionadas y testeadas con dbt.
- **Valor como guía para el LLM:** el paradigma "analytics engineering" moderno (SQL + ingeniería de software).
- **Conocimiento que aporta:** la práctica dominante de transformación ELT actual.
- **Vocabulario técnico:** *model*, *seed*, *snapshot*, *lineage*, *materialization*, *staging/mart*.
- **Razonamiento que aporta:** aplicar prácticas de software (tests, versionado) a datos.

#### P2 — *Data Engineering with Python*
- **Cobertura conceptual:** Airflow, NiFi, ingestión, transformación, calidad de datos en Python.
- **Cobertura práctica:** orquestar pipelines reales con herramientas concretas.
- **Valor como guía para el LLM:** código Python de pipelines — conecta con el dominio `python`.
- **Conocimiento que aporta:** la implementación práctica con el stack Python.
- **Vocabulario técnico:** *DAG*, *operator*, *sensor*, *backfill*, *data quality check*.
- **Razonamiento que aporta:** orquestación y manejo de dependencias entre tareas.

#### P3 — *97 Things Every Data Engineer Should Know*
- **Cobertura conceptual:** ensayos cortos sobre prácticas, cultura y errores comunes.
- **Cobertura práctica:** heurísticas y lecciones aprendidas de profesionales.
- **Valor como guía para el LLM:** registro de "consejo experto" diverso y conciso.
- **Conocimiento que aporta:** sabiduría práctica difícil de sistematizar.
- **Vocabulario técnico:** *data contract*, *SLA*, *observability*, *governance*.
- **Razonamiento que aporta:** heurísticas y juicio profesional.

## Papers y artículos clave

- Dean, J., Ghemawat, S. (2004). *MapReduce: Simplified Data Processing on Large Clusters*.
- Zaharia et al. (2012). *Resilient Distributed Datasets* (Spark).
- Armbrust et al. (2021). *Lakehouse: A New Generation of Open Platforms*. [enlace](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)
- Akidau et al. (2015). *The Dataflow Model*. VLDB.

## Documentación oficial / referencia

- [Apache Airflow](https://airflow.apache.org/docs/), [Apache Spark](https://spark.apache.org/docs/latest/), [Apache Kafka](https://kafka.apache.org/documentation/).
- [dbt docs](https://docs.getdbt.com/), [Delta Lake](https://docs.delta.io/), [Apache Iceberg](https://iceberg.apache.org/docs/latest/).
- [Apache Arrow](https://arrow.apache.org/docs/) y [Parquet](https://parquet.apache.org/docs/) — formatos columnares (el pipeline del repo exporta `corpus.parquet` opcional además de JSONL).

## Blogs técnicos

- [Data Engineering Weekly](https://www.dataengineeringweekly.com/).
- [Seattle Data Guy](https://seattledataguy.substack.com/).
- [Maxime Beauchemin — Functional Data Engineering](https://maximebeauchemin.medium.com/) (creador de Airflow/Superset).
- [Databricks blog](https://www.databricks.com/blog).

## Repositorios GitHub

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook).
- [andkret/Cookbook](https://github.com/andkret/Cookbook) — The Data Engineering Cookbook.
- [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core).

## Benchmarks / proxy

- **TPC-H / TPC-DS** — benchmarks analíticos estándar.
- **Parquet vs JSONL** compresión/velocidad como proxy de eficiencia de almacenamiento (se mide en el notebook 03).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

- **Documentación oficial** de Airflow/Spark/Kafka/dbt (Apache 2.0 / permisivas).
- **NYC Taxi**, **GDELT**, datasets de [data.gov](https://data.gov/) para ejemplos de pipeline.
- **Stack Exchange — Data Science / Database Administrators** (CC BY-SA, *verificar atribución*).
