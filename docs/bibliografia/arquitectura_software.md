# Bibliografía — Arquitectura de Software

> Dominio `arquitectura_software` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Clean Architecture | R. C. Martin | 2017 | 3 | 5 | Alta | 4 | 1 |
| F2 | Designing Data-Intensive Applications | M. Kleppmann | 2017 | 4 | 5 | Alta | 5 | 2 |
| F3 | Software Architecture: The Hard Parts | N. Ford, M. Richards, P. Sadalage, Z. Dehghani | 2021 | 4 | 4 | Alta | 5 | 1 |

#### F1 — *Clean Architecture*
- **Cobertura conceptual:** SOLID, límites de componentes, regla de dependencia, arquitectura hexagonal/puertos-adaptadores, política vs detalle.
- **Cobertura práctica:** estructurar un sistema para que la lógica de negocio no dependa de frameworks ni de la base de datos.
- **Valor como guía para el LLM:** prosa argumentativa sobre *por qué* de las decisiones de diseño; enseña el registro "principio → justificación → consecuencia".
- **Conocimiento que aporta:** el vocabulario canónico de diseño orientado a objetos y de capas.
- **Vocabulario técnico:** *dependency inversion*, *boundary*, *entity*, *use case*, *interface adapter*, *screaming architecture*.
- **Razonamiento que aporta:** razonamiento sobre acoplamiento/cohesión y trade-offs de mantenibilidad a largo plazo.

#### F2 — *Designing Data-Intensive Applications*
- **Cobertura conceptual:** modelos de datos, almacenamiento (LSM/B-tree), encoding, replicación, particionamiento, transacciones, consistencia, batch/stream.
- **Cobertura práctica:** elegir bases de datos y topologías según garantías de consistencia y patrones de carga.
- **Valor como guía para el LLM:** referencia número uno del campo; conecta arquitectura, sistemas distribuidos y data engineering con rigor.
- **Conocimiento que aporta:** el puente entre arquitectura, bases de datos y sistemas distribuidos — núcleo de los temas técnicos de Sebastian.
- **Vocabulario técnico:** *quorum*, *linearizability*, *log-structured*, *partition*, *leader/follower*, *MVCC*, *CDC*.
- **Razonamiento que aporta:** análisis de trade-offs de consistencia/disponibilidad/latencia con ejemplos reales de fallo.

#### F3 — *Software Architecture: The Hard Parts*
- **Cobertura conceptual:** descomposición de monolitos, granularidad de servicios, gestión de datos distribuidos, sagas, contratos.
- **Cobertura práctica:** decidir dónde poner los límites de servicio y cómo manejar datos compartidos.
- **Valor como guía para el LLM:** estructura de "trade-off analysis" explícita; enseña a razonar sin respuestas únicas.
- **Conocimiento que aporta:** las decisiones difíciles que los libros introductorios evitan.
- **Vocabulario técnico:** *saga pattern*, *data domain*, *quantum arquitectónico*, *coupling (static/dynamic)*, *fitness function*.
- **Razonamiento que aporta:** marco de decisión por trade-offs cuantificados; "no hay best practices, hay trade-offs".

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Domain-Driven Design | E. Evans | 2003 | 4 | 4 | Alta | 5 | 1 |
| A2 | Patterns of Enterprise Application Architecture | M. Fowler | 2002 | 4 | 3 | Media | 5 | 1 |
| A3 | Building Microservices (2ª ed.) | S. Newman | 2021 | 3 | 4 | Alta | 5 | 1 |

#### A1 — *Domain-Driven Design*
- **Cobertura conceptual:** lenguaje ubicuo, agregados, entidades, value objects, bounded contexts, context mapping.
- **Cobertura práctica:** modelar dominios complejos alineando el código con el lenguaje del negocio.
- **Valor como guía para el LLM:** el vocabulario DDD es referenciado en miles de discusiones de arquitectura modernas.
- **Conocimiento que aporta:** la disciplina de modelado de dominio que sustenta microservicios y event sourcing.
- **Vocabulario técnico:** *bounded context*, *aggregate root*, *ubiquitous language*, *anti-corruption layer*, *value object*.
- **Razonamiento que aporta:** descomposición de dominios y alineación negocio-código.

#### A2 — *Patterns of Enterprise Application Architecture*
- **Cobertura conceptual:** catálogo de patrones: Active Record, Data Mapper, Unit of Work, Repository, Identity Map.
- **Cobertura práctica:** implementar capas de persistencia y mapeo objeto-relacional con criterio.
- **Valor como guía para el LLM:** patrones con nombre canónico que aparecen en frameworks (Rails, Hibernate, Django).
- **Conocimiento que aporta:** el origen de los patrones que hoy se usan sin saber su nombre.
- **Vocabulario técnico:** *Repository*, *Unit of Work*, *Lazy Load*, *Data Mapper*, *Service Layer*.
- **Razonamiento que aporta:** selección de patrón según contexto; trade-offs de mapeo O-R.

#### A3 — *Building Microservices*
- **Cobertura conceptual:** límites de servicio, comunicación (sync/async), despliegue, observabilidad, seguridad, evolución de contratos.
- **Cobertura práctica:** diseñar, desplegar y operar una arquitectura de microservicios real.
- **Valor como guía para el LLM:** conecta arquitectura con DevOps y APIs — dominios vecinos (`devops`, `apis`).
- **Conocimiento que aporta:** el manual de referencia de microservicios moderno (2ª ed.).
- **Vocabulario técnico:** *service mesh*, *circuit breaker*, *contract testing*, *strangler fig*, *choreography vs orchestration*.
- **Razonamiento que aporta:** trade-offs de distribución, falacias del cómputo distribuido aplicadas.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Fundamentals of Software Architecture | M. Richards, N. Ford | 2020 | 3 | 5 | Alta | 5 | 1 |
| P2 | The Software Architect Elevator | G. Hohpe | 2020 | 2 | 3 | Media | 4 | 1 |
| P3 | Documenting Software Architectures (Views and Beyond) | P. Clements et al. | 2010 | 3 | 3 | Media | 4 | 1 |

#### P1 — *Fundamentals of Software Architecture*
- **Cobertura conceptual:** estilos arquitectónicos (capas, eventos, microkernel, microservicios), características (-ilities), soft skills del arquitecto.
- **Cobertura práctica:** evaluar y comunicar decisiones arquitectónicas; fitness functions.
- **Valor como guía para el LLM:** taxonomía clara de estilos — excelente material estructurado y categorizado.
- **Conocimiento que aporta:** mapa completo del espacio de estilos arquitectónicos.
- **Vocabulario técnico:** *architecture characteristic*, *fitness function*, *event-driven*, *space-based*, *microkernel*.
- **Razonamiento que aporta:** evaluación comparativa de estilos según requisitos no funcionales.

#### P2 — *The Software Architect Elevator*
- **Cobertura conceptual:** rol del arquitecto entre negocio y tecnología, comunicación, organización.
- **Cobertura práctica:** traducir estrategia técnica a lenguaje ejecutivo y viceversa.
- **Valor como guía para el LLM:** registro de comunicación técnico-organizacional, poco presente en textos centrados en código.
- **Conocimiento que aporta:** la dimensión socio-técnica de la arquitectura.
- **Vocabulario técnico:** *architecture elevator*, *option value*, *technical debt*, *enterprise architecture*.
- **Razonamiento que aporta:** razonamiento estratégico y de comunicación.

#### P3 — *Documenting Software Architectures*
- **Cobertura conceptual:** vistas arquitectónicas (módulo, C&C, asignación), modelo 4+1, ADRs.
- **Cobertura práctica:** documentar arquitecturas de forma navegable y mantenible.
- **Valor como guía para el LLM:** estructura de documentación formal — útil para el registro técnico-descriptivo.
- **Conocimiento que aporta:** cómo se documentan sistemas en la industria seria.
- **Vocabulario técnico:** *view*, *viewtype*, *ADR*, *4+1 model*, *allocation view*.
- **Razonamiento que aporta:** organización de información compleja por audiencias.

## Papers y artículos clave

- Fielding, R. (2000). *Architectural Styles and the Design of Network-based Software Architectures* (tesis, origen de REST). [enlace](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
- Parnas, D. (1972). *On the Criteria To Be Used in Decomposing Systems into Modules*. CACM. [DOI](https://doi.org/10.1145/361598.361623)
- Brooks, F. (1987). *No Silver Bullet — Essence and Accidents of Software Engineering*.
- Nygard, M. *Documenting Architecture Decisions* (origen de los ADR). [enlace](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

## Documentación oficial / referencia

- [C4 model](https://c4model.com/) — notación de diagramas de arquitectura (Simon Brown).
- [arc42](https://arc42.org/) — plantilla de documentación de arquitectura.
- [Azure Architecture Center](https://learn.microsoft.com/azure/architecture/) y [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Blogs técnicos

- [martinfowler.com](https://martinfowler.com/) — referencia de patrones y refactoring.
- [The Architecture of Open Source Applications (aosabook)](https://aosabook.org/).
- [High Scalability](http://highscalability.com/) — estudios de caso de sistemas reales.
- [InfoQ — Architecture & Design](https://www.infoq.com/architecture-design/).

## Repositorios GitHub

- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) — referencia de diseño de sistemas.
- [Sairyss/domain-driven-hexagon](https://github.com/Sairyss/domain-driven-hexagon) — DDD + hexagonal.
- [ardalis/CleanArchitecture](https://github.com/ardalis/CleanArchitecture) — plantilla de Clean Architecture.

## Benchmarks / proxy

- No hay benchmarks numéricos; el proxy de calidad es la presencia de **ADRs**, diagramas C4 y discusión explícita de trade-offs en el documento.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

- **Stack Exchange — Software Engineering** (dumps CC BY-SA, *verificar atribución*).
- ADRs públicos en repos GitHub (filtrar por licencia permisiva).
- Documentación arc42/C4 de proyectos open source.
