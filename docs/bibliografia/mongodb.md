# Bibliografía — MongoDB

> Dominio `mongodb` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | MongoDB: The Definitive Guide (3ª ed.) | S. Bradshaw, E. Brazil, K. Chodorow | 2019 | 2 | 5 | Alta | 5 | 2 |
| F2 | MongoDB Applied Design Patterns | R. Copeland | 2013 | 3 | 5 | Alta | 4 | 2 |
| F3 | MongoDB in Action (2ª ed.) | K. Banker, D. Garrett, P. Bakkum, S. Verch | 2016 | 2 | 4 | Alta | 4 | 2 |

#### F1 — *MongoDB: The Definitive Guide*
- **Cobertura conceptual:** CRUD, indexación, aggregation framework, replicación, sharding, administración, drivers.
- **Cobertura práctica:** el manual de referencia de MongoDB; desde insertar documentos hasta operar un replica set.
- **Valor como guía para el LLM:** el texto canónico de MongoDB; vocabulario oficial y patrones de uso de la guía definitiva.
- **Conocimiento que aporta:** la cobertura completa de MongoDB: modelo de documentos, consultas, índices y operaciones de cluster.
- **Vocabulario técnico:** *document*, *collection*, *BSON*, *replica set*, *sharding*, *aggregation pipeline*, *index*, *write concern*, *read preference*.
- **Razonamiento que aporta:** diseño de documentos para casos de uso específicos, elección de índices, operaciones atómicas.

#### F2 — *MongoDB Applied Design Patterns*
- **Cobertura conceptual:** patrones de diseño de documentos: embedding vs. referencing, polimorfismo, versión de esquema, catálogos, árboles, time-series.
- **Cobertura práctica:** diseñar esquemas MongoDB para casos de uso reales; evitar antipatrones comunes.
- **Valor como guía para el LLM:** el único texto dedicado a patrones de diseño de documentos; conecta el modelo de datos con decisiones de aplicación.
- **Conocimiento que aporta:** los patrones de diseño específicos de bases de datos documentales — conocimiento que no existe en textos relacionales.
- **Vocabulario técnico:** *embedding*, *referencing*, *bucket pattern*, *outlier pattern*, *polymorphism*, *schema versioning*, *pre-allocation*.
- **Razonamiento que aporta:** razonamiento sobre trade-offs embedding vs. referencing, diseño orientado a queries.

#### F3 — *MongoDB in Action*
- **Cobertura conceptual:** introducción a MongoDB, modelado de datos, queries, aggregation, indexación, performance, sharding.
- **Cobertura práctica:** construir aplicaciones completas con MongoDB; ejemplos con Node.js y Ruby.
- **Valor como guía para el LLM:** perspectiva del desarrollador de aplicaciones usando MongoDB; registro más orientado a la aplicación.
- **Conocimiento que aporta:** el ciclo completo de desarrollo de aplicaciones con MongoDB desde la perspectiva del desarrollador.
- **Vocabulario técnico:** *query operators*, *projection*, *cursor*, *aggregation stages*, *geospatial index*, *text index*, *explain plan*.
- **Razonamiento que aporta:** decisiones de modelado orientadas a la aplicación, optimización de consultas frecuentes.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | MongoDB Performance Tuning | G. Harrison, M. Harrison | 2021 | 4 | 5 | Alta | 5 | 3 |
| A2 | Designing Data-Intensive Applications | M. Kleppmann | 2017 | 4 | 4 | Media | 5 | 2 |
| A3 | NoSQL Distilled | M. Fowler, P. Sadalage | 2012 | 3 | 4 | Media | 4 | 2 |

#### A1 — *MongoDB Performance Tuning*
- **Cobertura conceptual:** profiling, explain plans, índices avanzados, aggregation optimization, memory management, sharding performance.
- **Cobertura práctica:** identificar y resolver cuellos de botella en MongoDB de producción.
- **Valor como guía para el LLM:** el texto de performance más completo para MongoDB; vocabulario de tuning avanzado.
- **Conocimiento que aporta:** el nivel de optimización que usa un DBA de MongoDB en producción.
- **Vocabulario técnico:** *execution stats*, *COLLSCAN vs IXSCAN*, *covered query*, *index intersection*, *chunk migration*, *WiredTiger cache*.
- **Razonamiento que aporta:** interpretación de explain plans, diseño de índices compuestos, análisis de carga de trabajo.

#### A2 — *Designing Data-Intensive Applications*
- **Cobertura conceptual:** bases de datos relacionales y NoSQL, replicación, particionamiento, transacciones, procesamiento por batches y streams.
- **Cobertura práctica:** diseñar sistemas de datos confiables y escalables; entender MongoDB en el contexto de otras soluciones.
- **Valor como guía para el LLM:** el mejor texto técnico de sistemas de datos; ubica MongoDB en el contexto de las alternativas (referencia cruzada con `sistemas_distribuidos`).
- **Conocimiento que aporta:** las garantías y limitaciones de MongoDB comparado con sistemas relacionales y otros NoSQL.
- **Vocabulario técnico:** *BASE*, *eventual consistency*, *multi-document transaction*, *change streams*, *oplog*, *document model vs relational*.
- **Razonamiento que aporta:** comparación entre modelos de consistencia, elección de base de datos por requisitos del sistema.

#### A3 — *NoSQL Distilled*
- **Cobertura conceptual:** teorema CAP, modelos de bases de datos NoSQL: documentos, columnas, grafos, clave-valor; cuándo usar cada uno.
- **Cobertura práctica:** elegir el tipo de base de datos NoSQL apropiado para un caso de uso.
- **Valor como guía para el LLM:** ubica MongoDB en el panorama NoSQL con vocabulario de la literatura académica y de industria.
- **Conocimiento que aporta:** el contexto histórico y técnico del movimiento NoSQL que explica por qué existe MongoDB.
- **Vocabulario técnico:** *CAP theorem*, *BASE*, *aggregate-oriented databases*, *polyglot persistence*, *schema-less*, *horizontal scaling*.
- **Razonamiento que aporta:** selección de base de datos por características de consistencia, escalabilidad y modelo de datos.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | MongoDB Aggregation Framework | MongoDB Inc. (documentación) | Continuo | 3 | 5 | Alta | 5 | 2 |
| P2 | Practical MongoDB Aggregations | P. Done | 2023 | 3 | 4 | Media | 4 | 1 |
| P3 | PyMongo documentation | MongoDB Inc. | Continuo | 2 | 4 | Media | 4 | 1 |

#### P1 — *MongoDB Aggregation Framework* (documentación oficial)
- **Cobertura conceptual:** todos los stages del aggregation pipeline: $match, $group, $project, $lookup, $unwind, $facet, $bucket, $merge.
- **Cobertura práctica:** construir pipelines de análisis complejos; transformar y agregar datos directamente en MongoDB.
- **Valor como guía para el LLM:** referencia oficial técnica con ejemplos; el aggregation framework es el SQL de MongoDB.
- **Conocimiento que aporta:** el poder analítico de MongoDB sin necesidad de mover datos a otra capa.
- **Vocabulario técnico:** *pipeline stage*, *accumulator*, *$lookup*, *$unwind*, *$facet*, *$bucket*, *$merge*, *$out*, *expression operators*.
- **Razonamiento que aporta:** diseño de pipelines de análisis, elección de stages por tipo de transformación.

#### P2 — *Practical MongoDB Aggregations*
- **Cobertura conceptual:** patrones y buenas prácticas del aggregation pipeline, con ejemplos completos por caso de uso.
- **Cobertura práctica:** diseñar pipelines de agregación legibles y eficientes.
- **Valor como guía para el LLM:** ejemplos de pipelines explicados paso a paso; complementa la referencia oficial (P1).
- **Conocimiento que aporta:** cómo componer stages para análisis reales dentro de MongoDB.
- **Vocabulario técnico:** *$match*, *$group*, *$lookup*, *$unwind*, *$setWindowFields*, *pipeline optimization*.
- **Razonamiento que aporta:** descomposición de un análisis en etapas de pipeline.

#### P3 — *PyMongo documentation*
- **Cobertura conceptual:** cliente pymongo, CRUD, índices, agregaciones, transacciones, GridFS, change streams.
- **Cobertura práctica:** usar MongoDB desde Python. Tema del corpus y de la Etapa 2; el código de este repo no usa MongoDB.
- **Valor como guía para el LLM:** código Python con MongoDB; conecta con el dominio `python`.
- **Conocimiento que aporta:** el uso idiomático del driver oficial de Python.
- **Vocabulario técnico:** *MongoClient*, *cursor*, *bulk_write*, *GridFS*, *change stream*, *connection pooling*.
- **Razonamiento que aporta:** manejo de conexiones y errores en aplicaciones Python con MongoDB.

## Papers importantes

- Chang, F. et al. — *Bigtable: A Distributed Storage System for Structured Data* (OSDI 2006). [Link](https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/)
- DeCandia, G. et al. — *Dynamo: Amazon's Highly Available Key-value Store* (SOSP 2007). [ACM link](https://dl.acm.org/doi/10.1145/1294261.1294281)
- MongoDB, Inc. — whitepapers de arquitectura de MongoDB/Atlas (verificar título y año vigentes).

## Documentación oficial

- [MongoDB Manual](https://www.mongodb.com/docs/manual/) — referencia completa oficial (documentación: verificar licencia; el servidor usa SSPL).
- [MongoDB Aggregation Operations](https://www.mongodb.com/docs/manual/aggregation/) — referencia del aggregation framework.
- [pymongo documentation](https://pymongo.readthedocs.io/) — Apache-2.0; driver Python oficial.
- [Motor (async MongoDB driver)](https://motor.readthedocs.io/) — Apache-2.0; driver asíncrono para Python.

## Blogs técnicos

- [MongoDB Developer Hub](https://www.mongodb.com/developer/) — artículos y tutoriales del equipo MongoDB.
- [Studio 3T blog](https://studio3t.com/knowledge-base/) — herramienta GUI para MongoDB; artículos técnicos.
- [Percona blog — MongoDB](https://www.percona.com/blog/tag/mongodb/) — operaciones y performance.
- [MongoDB University](https://learn.mongodb.com/) — cursos oficiales con contenido textual.
- [DZone — MongoDB](https://dzone.com/nosql-database/mongodb) — artículos técnicos de la comunidad.

## Repositorios GitHub

- [mongodb/mongo](https://github.com/mongodb/mongo) — código fuente del servidor (SSPL).
- [mongodb/mongo-python-driver](https://github.com/mongodb/mongo-python-driver) — pymongo (Apache-2.0).
- [mongodb/motor](https://github.com/mongodb/motor) — driver async Python (Apache-2.0).
- [mongodb/specifications](https://github.com/mongodb/specifications) — especificaciones técnicas del protocolo.

## Benchmarks

- **YCSB (Yahoo Cloud Serving Benchmark)** — benchmark estándar para NoSQL; incluye workloads MongoDB.
- **TPC-W** — benchmark de aplicaciones web con BD.
- Para evaluar el LLM: preguntas de MongoDB Certified Developer Associate exam; verificar disponibilidad de material de práctica.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| MongoDB sample datasets (Atlas) | MongoDB License | Datasets de ejemplo: restaurants, movies, weather |
| OpenStreetMap exports | ODbL 1.0 | Datos geoespaciales compatibles con GeoJSON/MongoDB |
| Yelp Open Dataset | Verificar licencia de uso | Datos de reseñas con estructura de documentos |
| TMDB (The Movie Database) API | CC BY-NC 3.0 | Datos de películas en formato JSON |
| Stack Overflow (subset JSON) | CC BY-SA 4.0 | Para ejercicios de importación de documentos |
