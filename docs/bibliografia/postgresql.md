# Bibliografía — PostgreSQL

> Dominio `postgresql` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | PostgreSQL: Up and Running (3ª ed.) | R. Obe, L. Hsu | 2017 | 2 | 5 | Alta | 5 | 2 |
| F2 | Learning PostgreSQL | S. Juba, A. Vannahme, A. Volkov | 2015 | 2 | 4 | Alta | 4 | 2 |
| F3 | The Art of PostgreSQL | D. Fontaine | 2019 | 3 | 5 | Alta | 5 | 2 |

#### F1 — *PostgreSQL: Up and Running*
- **Cobertura conceptual:** instalación, tipos de datos, funciones, índices, roles y seguridad, replicación, extensiones, PostGIS.
- **Cobertura práctica:** el manual introductorio más completo de PostgreSQL; desde instalación hasta uso productivo.
- **Valor como guía para el LLM:** cobertura amplia con vocabulario de administración y uso de PostgreSQL desde perspectiva operacional.
- **Conocimiento que aporta:** el ciclo completo de PostgreSQL: desde DDL hasta tuning básico, pasando por roles y replicación.
- **Vocabulario técnico:** *tablespace*, *role*, *schema*, *index*, *VACUUM*, *ANALYZE*, *WAL*, *streaming replication*, *pg_hba.conf*.
- **Razonamiento que aporta:** decisiones de diseño de base de datos, elección de tipos de datos, estrategias de indexación básicas.

#### F2 — *Learning PostgreSQL*
- **Cobertura conceptual:** instalación, SQL en PostgreSQL, procedimientos almacenados, triggers, optimización básica, diseño de esquemas.
- **Cobertura práctica:** desarrollar aplicaciones con PostgreSQL desde cero.
- **Valor como guía para el LLM:** texto pedagógico accesible; aporta el registro introductorio del dominio PostgreSQL.
- **Conocimiento que aporta:** el camino de aprendizaje estructurado de un desarrollador nuevo en PostgreSQL.
- **Vocabulario técnico:** *SELECT/INSERT/UPDATE/DELETE*, *JOIN*, *CTE*, *trigger*, *stored procedure*, *partitioning*, *sequences*.
- **Razonamiento que aporta:** diseño de esquemas relacionales, optimización de consultas básicas, uso de constraints.

#### F3 — *The Art of PostgreSQL*
- **Cobertura conceptual:** SQL avanzado: window functions, CTEs recursivos, arrays, JSONB, full text search, extensiones, integración con Python.
- **Cobertura práctica:** usar PostgreSQL como herramienta de análisis de datos; queries avanzados reales.
- **Valor como guía para el LLM:** el texto de PostgreSQL avanzado más orientado al desarrollador; ejemplos reales con patrones avanzados.
- **Conocimiento que aporta:** el nivel de PostgreSQL que diferencia a un usuario básico de un experto en análisis de datos con SQL.
- **Vocabulario técnico:** *window function*, *PARTITION BY*, *LATERAL JOIN*, *UNNEST*, *JSONB operators*, *GIN index*, *range types*.
- **Razonamiento que aporta:** reformulación de problemas de análisis como queries SQL eficientes, debugging de planes de ejecución.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | PostgreSQL 10 High Performance | I. Ahmed, G. Smith, E. Pirozzi | 2018 | 4 | 5 | Alta | 5 | 3 |
| A2 | PostgreSQL: Introduction and Concepts | B. Momjian | 2001 | 4 | 4 | Media | 5 | 3 |
| A3 | PostgreSQL 14 Internals | E. Rogov | 2022 | 5 | 4 | Media | 5 | 4 |

#### A1 — *PostgreSQL 10 High Performance*
- **Cobertura conceptual:** tuning de memoria, EXPLAIN/EXPLAIN ANALYZE, índices avanzados (GiST, GIN, BRIN), particionamiento, VACUUM agresivo, replicación.
- **Cobertura práctica:** optimizar PostgreSQL para cargas de producción; identificar y resolver cuellos de botella.
- **Valor como guía para el LLM:** vocabulario de performance avanzado de PostgreSQL; el texto más completo en optimización.
- **Conocimiento que aporta:** el nivel de tuning que usa un DBA de producción; tema del corpus y de la Etapa 2 (el código del repo no usa PostgreSQL).
- **Vocabulario técnico:** *planner cost*, *seq scan vs index scan*, *bitmap index scan*, *work_mem*, *shared_buffers*, *checkpoint*, *bloat*.
- **Razonamiento que aporta:** interpretación de planes de ejecución, diagnóstico de consultas lentas, tuning de parámetros del servidor.

#### A2 — *PostgreSQL: Introduction and Concepts*
- **Cobertura conceptual:** historia y diseño del sistema, modelo de objetos relacionales, extensibilidad, sistema de tipos.
- **Cobertura práctica:** entender las decisiones de diseño de PostgreSQL como DBMS objeto-relacional.
- **Valor como guía para el LLM:** perspectiva histórica y conceptual de PostgreSQL escrita por un core developer.
- **Conocimiento que aporta:** la filosofía de diseño de PostgreSQL y cómo difiere de otros DBMS; base conceptual profunda.
- **Vocabulario técnico:** *OODBMS*, *type system*, *operator class*, *aggregate function*, *table inheritance*, *rule system*.
- **Razonamiento que aporta:** razonamiento sobre diseño de DBMS, extensibilidad del sistema de tipos, selección entre DBMS.

#### A3 — *PostgreSQL 14 Internals*
- **Cobertura conceptual:** MVCC, buffer manager, WAL, planificador de consultas, índices internos, bloqueos, vacuum internals.
- **Cobertura práctica:** entender el motor interno para diagnosticar problemas difíciles y diseñar mejor.
- **Valor como guía para el LLM:** el texto técnico más profundo sobre internals de PostgreSQL; disponible libremente en PDF.
- **Conocimiento que aporta:** cómo funciona PostgreSQL por dentro: MVCC, transacciones, recovery, planner — conocimiento de experto.
- **Vocabulario técnico:** *MVCC*, *XMIN/XMAX*, *visibility map*, *FSM*, *WAL segments*, *checkpoint*, *lock manager*, *cost model*.
- **Razonamiento que aporta:** diagnóstico profundo de problemas de concurrencia, transacciones y rendimiento.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | SQL Performance Explained | M. Winand | 2012 | 3 | 5 | Alta | 5 | 3 |
| P2 | Seven Databases in Seven Weeks (2ª ed.) | L. Perkins, E. Redmond, J. Wilson | 2018 | 2 | 3 | Baja | 4 | 2 |
| P3 | Practical SQL (2ª ed.) | A. DeBarros | 2022 | 2 | 4 | Media | 5 | 1 |

#### P1 — *SQL Performance Explained*
- **Cobertura conceptual:** anatomía de un índice, estrategias de acceso, condiciones de búsqueda compleja, JOIN, sorting, parcialmente.
- **Cobertura práctica:** diseñar índices eficientes; entender por qué una consulta es lenta y cómo arreglarla.
- **Valor como guía para el LLM:** el mejor libro de indexación SQL; conecta teoría de B-Trees con práctica de consultas.
- **Conocimiento que aporta:** el conocimiento de índices que todo desarrollador que usa PostgreSQL necesita para escribir queries eficientes.
- **Vocabulario técnico:** *B-Tree index*, *index scan*, *index-only scan*, *covering index*, *partial index*, *concatenated index*, *selectivity*.
- **Razonamiento que aporta:** diseño de índices para queries específicas, razonamiento sobre selectividad y uso de índices.

#### P2 — *Seven Databases in Seven Weeks*
- **Cobertura conceptual:** PostgreSQL, HBase, MongoDB, CouchDB, Neo4j, DynamoDB, Redis — paradigmas distintos de almacenamiento.
- **Cobertura práctica:** comparar bases de datos relacionales, documentales, grafos y clave-valor.
- **Valor como guía para el LLM:** contexto comparativo que ubica PostgreSQL en el ecosistema de bases de datos.
- **Conocimiento que aporta:** la perspectiva comparativa que ayuda a elegir entre diferentes tipos de bases de datos.
- **Vocabulario técnico:** *CAP theorem*, *ACID vs BASE*, *document store*, *graph database*, *key-value store*, *column family*.
- **Razonamiento que aporta:** decisión entre paradigmas de bases de datos por características del problema.

#### P3 — *Practical SQL*
- **Cobertura conceptual:** SQL desde cero con PostgreSQL: tipos, joins, subqueries, window functions, análisis de datos geográficos.
- **Cobertura práctica:** análisis de datos reales con SQL; muy orientado a periodistas de datos y analistas.
- **Valor como guía para el LLM:** el texto más accesible con ejemplos de análisis de datos reales; registro no técnico con SQL práctico.
- **Conocimiento que aporta:** el uso de PostgreSQL para análisis de datos: desde tablas básicas hasta análisis estadístico con SQL.
- **Vocabulario técnico:** *aggregate functions*, *GROUP BY*, *HAVING*, *subquery*, *window function*, *rank/row_number*, *PostGIS basics*.
- **Razonamiento que aporta:** análisis de datos con SQL, formulación de preguntas de negocio como consultas.

## Papers importantes

- Stonebraker, M. & Rowe, L. A. — *The Design of POSTGRES* (SIGMOD 1986). [ACM link](https://dl.acm.org/doi/10.1145/16856.16888)
- Hellerstein, J. M., Stonebraker, M., Hamilton, J. — *Architecture of a Database System* (Foundations and Trends in Databases, 2007).
- Ramakrishnan, R. & Gehrke, J. — *Database Management Systems* (capítulos seleccionados como referencia).

## Documentación oficial

- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/current/) — PostgreSQL License (open source); la referencia definitiva.
- [PostgreSQL Wiki](https://wiki.postgresql.org/) — artículos técnicos y guías de la comunidad.
- [EXPLAIN documentation](https://www.postgresql.org/docs/current/sql-explain.html) — referencia para interpretación de planes.
- [pgAdmin documentation](https://www.pgadmin.org/docs/) — herramienta de administración.

## Blogs técnicos

- [Planet PostgreSQL](https://planet.postgresql.org/) — agregador de blogs de la comunidad PostgreSQL.
- [pganalyze blog](https://pganalyze.com/blog) — optimización y monitoreo de PostgreSQL.
- [Citus Data blog](https://www.citusdata.com/blog/) — PostgreSQL distribuido y análisis.
- [depesz.com (H. Lubaczewski)](https://www.depesz.com/) — análisis profundos de PostgreSQL por experto de la comunidad.
- [Severalnines — PostgreSQL](https://severalnines.com/database-blog/postgresql/) — operaciones y administración.

## Repositorios GitHub

- [postgres/postgres](https://github.com/postgres/postgres) — código fuente de PostgreSQL (PostgreSQL License).
- [citusdata/citus](https://github.com/citusdata/citus) — PostgreSQL distribuido (AGPLv3).
- [pgvector/pgvector](https://github.com/pgvector/pgvector) — búsqueda vectorial en PostgreSQL (PostgreSQL License).
- [supabase/supabase](https://github.com/supabase/supabase) — backend-as-a-service sobre PostgreSQL (Apache-2.0).
- [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) — linter SQL (MIT).

## Benchmarks

- **pgbench** — benchmark oficial incluido en PostgreSQL; TPC-B simplificado.
- **TPC-H** — benchmark analítico de referencia para data warehouses.
- **TPC-C** — benchmark transaccional OLTP de referencia.
- Para evaluar el LLM: preguntas de certificación PostgreSQL (PostgreSQL CE / PGCES-02, de LPI-Japan).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| PostgreSQL official documentation dump | PostgreSQL License | Texto completo de la documentación oficial |
| StackOverflow PostgreSQL questions | CC BY-SA 4.0 | Preguntas y respuestas etiquetadas con [postgresql] |
| TPC-H sample data | Verificar TPC license | Datos de referencia para queries analíticos |
| Pagila (sample database) | PostgreSQL License | Base de datos de ejemplo con datos realistas |
| IMDB (Internet Movie Database) subset | Verificar licencia | Dataset de referencia popular para SQL |
