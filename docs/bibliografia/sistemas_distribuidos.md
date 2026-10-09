# Bibliografía — Sistemas Distribuidos / Computación

> Dominio `sistemas_distribuidos` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Designing Data-Intensive Applications | M. Kleppmann | 2017 | 4 | 5 | Alta | 5 | 2 |
| F2 | Distributed Systems (3ª ed.) | A. Tanenbaum, M. van Steen | 2017 | 4 | 5 | Alta | 5 | 3 |
| F3 | Introduction to Reliable and Secure Distributed Programming (2ª ed.) | C. Cachin, R. Guerraoui, L. Rodrigues | 2011 | 5 | 4 | Media | 5 | 4 |

#### F1 — *Designing Data-Intensive Applications*
- **Cobertura conceptual:** replicación, particionamiento, consenso, consistencia, transacciones distribuidas, procesamiento batch/stream.
- **Cobertura práctica:** razonar sobre garantías de un sistema distribuido real y sus modos de fallo.
- **Valor como guía para el LLM:** referencia compartida con arquitectura y data engineering; rigor y claridad excepcionales.
- **Conocimiento que aporta:** el puente práctico entre teoría distribuida e ingeniería de datos.
- **Vocabulario técnico:** *linearizability*, *quorum*, *consensus*, *split-brain*, *causal consistency*, *exactly-once*.
- **Razonamiento que aporta:** análisis de trade-offs de consistencia/latencia y razonamiento sobre fallos parciales.

#### F2 — *Distributed Systems* (Tanenbaum & van Steen)
- **Cobertura conceptual:** arquitecturas, comunicación, nombrado, sincronización, replicación, tolerancia a fallos, seguridad.
- **Cobertura práctica:** entender los mecanismos base (RPC, relojes lógicos, elección de líder) desde primeros principios.
- **Valor como guía para el LLM:** texto académico estructurado; cubre el nivel teórico-fundamental del dominio.
- **Conocimiento que aporta:** la teoría canónica enseñada en cursos universitarios.
- **Vocabulario técnico:** *Lamport clock*, *vector clock*, *RPC*, *two-phase commit*, *Byzantine fault*, *gossip*.
- **Razonamiento que aporta:** derivación de algoritmos distribuidos y pruebas de corrección informales.

#### F3 — *Introduction to Reliable and Secure Distributed Programming*
- **Cobertura conceptual:** abstracciones de comunicación, broadcast, memoria compartida, consenso, modelos de fallo.
- **Cobertura práctica:** especificar e implementar primitivas distribuidas con garantías demostrables.
- **Valor como guía para el LLM:** texto formal con especificaciones precisas — registro escaso y valioso.
- **Conocimiento que aporta:** la formalización rigurosa que falta en los textos más aplicados.
- **Vocabulario técnico:** *reliable broadcast*, *failure detector*, *fail-stop*, *safety/liveness*, *atomic register*.
- **Razonamiento que aporta:** especificación formal (safety/liveness) y demostración de propiedades.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Distributed Algorithms | N. Lynch | 1996 | 5 | 3 | Media | 5 | 5 |
| A2 | Database Internals | A. Petrov | 2019 | 4 | 4 | Alta | 5 | 2 |
| A3 | Streaming Systems | T. Akidau, S. Chernyak, R. Lax | 2018 | 4 | 4 | Media | 5 | 2 |

#### A1 — *Distributed Algorithms*
- **Cobertura conceptual:** modelos síncronos/asíncronos, consenso, exclusión mutua, cotas de imposibilidad.
- **Cobertura práctica:** demostrar corrección y complejidad de algoritmos distribuidos.
- **Valor como guía para el LLM:** el texto teorema-demostración de referencia; estructura lógica formal pura.
- **Conocimiento que aporta:** los límites teóricos (FLP, lower bounds) que definen el campo.
- **Vocabulario técnico:** *FLP impossibility*, *synchronous model*, *I/O automata*, *round complexity*.
- **Razonamiento que aporta:** demostraciones de imposibilidad y cotas inferiores.

#### A2 — *Database Internals*
- **Cobertura conceptual:** motores de almacenamiento (B-tree/LSM), WAL, distribución, consenso (Paxos/Raft), replicación.
- **Cobertura práctica:** entender cómo funcionan por dentro las bases de datos distribuidas modernas.
- **Valor como guía para el LLM:** conecta sistemas distribuidos con los dominios `postgresql` y `mongodb`.
- **Conocimiento que aporta:** la implementación real de las ideas distribuidas en bases de datos.
- **Vocabulario técnico:** *WAL*, *MemTable/SSTable*, *Raft*, *anti-entropy*, *read repair*, *Merkle tree*.
- **Razonamiento que aporta:** análisis de implementación y trade-offs de motores de almacenamiento.

#### A3 — *Streaming Systems*
- **Cobertura conceptual:** tiempo de evento vs procesamiento, watermarks, ventanas, triggers, exactly-once.
- **Cobertura práctica:** diseñar pipelines de streaming correctos (modelo Dataflow/Beam).
- **Valor como guía para el LLM:** vocabulario de streaming compartido con data engineering.
- **Conocimiento que aporta:** la semántica formal del procesamiento de flujos.
- **Vocabulario técnico:** *watermark*, *event time*, *windowing*, *trigger*, *exactly-once*, *late data*.
- **Razonamiento que aporta:** razonamiento sobre corrección en presencia de desorden temporal.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Understanding Distributed Systems (2ª ed.) | R. Vitillo | 2022 | 3 | 5 | Alta | 5 | 1 |
| P2 | Designing Distributed Systems | B. Burns | 2018 | 3 | 4 | Alta | 4 | 1 |
| P3 | Site Reliability Engineering | Google (Beyer et al.) | 2016 | 3 | 3 | Media | 5 | 1 |

#### P1 — *Understanding Distributed Systems*
- **Cobertura conceptual:** comunicación, coordinación, escalabilidad, resiliencia, operabilidad — visión moderna y accesible.
- **Cobertura práctica:** diseñar servicios distribuidos del mundo real (estilo cloud-native).
- **Valor como guía para el LLM:** prosa clara y actual; excelente "puente" entre teoría e ingeniería.
- **Conocimiento que aporta:** la síntesis pragmática 2022 del campo.
- **Vocabulario técnico:** *idempotency*, *backpressure*, *bulkhead*, *load shedding*, *consistent hashing*.
- **Razonamiento que aporta:** diseño orientado a fallos y escala.

#### P2 — *Designing Distributed Systems*
- **Cobertura conceptual:** patrones de sistemas distribuidos sobre contenedores (sidecar, ambassador, scatter-gather).
- **Cobertura práctica:** componer sistemas con patrones reutilizables sobre Kubernetes.
- **Valor como guía para el LLM:** conecta sistemas distribuidos con el dominio `devops` (contenedores).
- **Conocimiento que aporta:** los patrones cloud-native con nombre canónico.
- **Vocabulario técnico:** *sidecar*, *ambassador*, *adapter*, *scatter-gather*, *work queue*.
- **Razonamiento que aporta:** composición de sistemas a partir de patrones.

#### P3 — *Site Reliability Engineering*
- **Cobertura conceptual:** SLO/SLI, error budgets, eliminación de toil, gestión de incidentes a escala Google.
- **Cobertura práctica:** operar sistemas distribuidos de forma fiable y medible.
- **Valor como guía para el LLM:** vocabulario SRE compartido con DevOps; casos reales de operación.
- **Conocimiento que aporta:** la disciplina operativa de sistemas a escala.
- **Vocabulario técnico:** *SLO*, *error budget*, *toil*, *blameless postmortem*, *cascading failure*.
- **Razonamiento que aporta:** decisiones operativas basadas en presupuestos de error.

## Papers y artículos clave

- Lamport, L. (1978). *Time, Clocks, and the Ordering of Events in a Distributed System*. [DOI](https://doi.org/10.1145/359545.359563)
- Fischer, Lynch, Paterson (1985). *Impossibility of Distributed Consensus with One Faulty Process* (FLP).
- Lamport, L. (1998/2001). *The Part-Time Parliament* / *Paxos Made Simple*.
- Ongaro, D., Ousterhout, J. (2014). *In Search of an Understandable Consensus Algorithm* (Raft). [enlace](https://raft.github.io/raft.pdf)
- DeCandia et al. (2007). *Dynamo: Amazon's Highly Available Key-value Store*.
- Brewer, E. (2000/2012). *CAP Theorem* / *CAP Twelve Years Later*.

## Documentación oficial / referencia

- [Raft visualization (thesecretlivesofdata)](https://thesecretlivesofdata.com/raft/).
- [Jepsen analyses](https://jepsen.io/analyses) — verificación empírica de garantías de bases de datos distribuidas.
- [MIT 6.824 Distributed Systems](https://pdos.csail.mit.edu/6.824/) — material de curso.

## Blogs técnicos

- [Marc Brooker's blog](https://brooker.co.za/blog/) — ingeniero principal de AWS.
- [Murat Demirbas — Metadata](https://muratbuffalo.blogspot.com/) — lecturas de papers distribuidos.
- [Aphyr (Kyle Kingsbury) — Jepsen](https://aphyr.com/) — testing de consistencia.
- [the morning paper](https://blog.acolyer.org/) (archivo) — resúmenes de papers.

## Repositorios GitHub

- [pingcap/talent-plan](https://github.com/pingcap/talent-plan) — cursos de sistemas distribuidos (Rust/Go).
- [theanalyst/awesome-distributed-systems](https://github.com/theanalyst/awesome-distributed-systems).
- [maxhumber/papers / papers-we-love](https://github.com/papers-we-love/papers-we-love) — papers fundacionales.

## Benchmarks / proxy

- **YCSB** (Yahoo! Cloud Serving Benchmark) — carga de bases de datos distribuidas.
- **TPC-C / TPC-H** — transaccional y analítico.
- **Jepsen** como proxy de corrección (no de rendimiento).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

- **MIT 6.824 / UWisconsin notes** (verificar licencia de uso).
- **Stack Exchange** (Stack Overflow tags: distributed-systems, consensus — CC BY-SA, *verificar atribución*).
- Papers de arXiv cs.DC (Distributed, Parallel, and Cluster Computing) — esta sí está en el corpus: fuente `arxiv` de configs/data.yaml (solo abstracts).
