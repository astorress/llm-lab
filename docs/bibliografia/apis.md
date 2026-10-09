# Bibliografía — APIs

> Dominio `apis` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | RESTful Web APIs | L. Richardson, M. Amundsen, S. Ruby | 2013 | 3 | 5 | Alta | 5 | 1 |
| F2 | Web API Design: The Missing Link (Apigee) | Apigee / Google Cloud | 2018 | 2 | 4 | Alta | 4 | 1 |
| F3 | Designing Web APIs | B. Jin, S. Sahni, A. Shevat | 2018 | 2 | 4 | Alta | 4 | 1 |

#### F1 — *RESTful Web APIs*
- **Cobertura conceptual:** REST, hipermedia (HATEOAS), modelo de madurez de Richardson, formatos, semántica HTTP.
- **Cobertura práctica:** diseñar APIs REST correctas y evolutivas, no solo "HTTP + JSON".
- **Valor como guía para el LLM:** el texto canónico de REST; aclara malentendidos comunes con autoridad.
- **Conocimiento que aporta:** el modelo conceptual real de REST (más allá de CRUD sobre HTTP).
- **Vocabulario técnico:** *resource*, *representation*, *HATEOAS*, *idempotent method*, *media type*, *Richardson Maturity Model*.
- **Razonamiento que aporta:** razonamiento sobre diseño de recursos, contratos y evolución de APIs.

#### F2 — *Web API Design (Apigee)*
- **Cobertura conceptual:** convenciones pragmáticas: nombrado de recursos, versionado, paginación, errores, filtrado.
- **Cobertura práctica:** tomar decisiones de diseño cotidianas con criterio consistente.
- **Valor como guía para el LLM:** guía concisa de best practices muy citada en la industria.
- **Conocimiento que aporta:** las convenciones pragmáticas que la mayoría de APIs siguen.
- **Vocabulario técnico:** *resource naming*, *pagination*, *versioning*, *partial response*, *error envelope*.
- **Razonamiento que aporta:** trade-offs de usabilidad y consistencia de APIs.

#### F3 — *Designing Web APIs*
- **Cobertura conceptual:** diseño orientado a casos de uso, paginación, rate limiting, webhooks, autenticación, versionado.
- **Cobertura práctica:** diseñar una API pública completa pensando en sus consumidores.
- **Valor como guía para el LLM:** perspectiva de producto + ingeniería; cubre webhooks y rate limiting.
- **Conocimiento que aporta:** el diseño de APIs desde la experiencia del desarrollador consumidor.
- **Vocabulario técnico:** *rate limiting*, *webhook*, *pagination cursor*, *API key*, *SDK*, *developer experience*.
- **Razonamiento que aporta:** diseño centrado en el consumidor y en la evolución.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | API Design Patterns | J. J. Geewax | 2021 | 4 | 5 | Alta | 5 | 1 |
| A2 | Building Microservices (2ª ed.) | S. Newman | 2021 | 3 | 4 | Alta | 5 | 1 |
| A3 | gRPC: Up and Running | K. Indrasiri, D. Kuruppu | 2020 | 3 | 3 | Media | 4 | 1 |

#### A1 — *API Design Patterns*
- **Cobertura conceptual:** catálogo exhaustivo de patrones (resource layout, standard methods, long-running operations, batch, pagination).
- **Cobertura práctica:** resolver problemas recurrentes de diseño de APIs con patrones probados (origen en Google AIPs).
- **Valor como guía para el LLM:** patrones con nombre y estructura — el material más sistemático del dominio.
- **Conocimiento que aporta:** el catálogo de patrones de API más completo.
- **Vocabulario técnico:** *standard methods*, *custom methods*, *resource hierarchy*, *long-running operation*, *idempotency key*.
- **Razonamiento que aporta:** aplicación de patrones según contexto; consistencia a escala.

#### A2 — *Building Microservices*
- **Cobertura conceptual:** comunicación entre servicios (REST/gRPC/eventos), contratos, versionado, API gateways.
- **Cobertura práctica:** diseñar las APIs que conectan microservicios.
- **Valor como guía para el LLM:** conecta APIs con los dominios vecinos `arquitectura_software` y `devops`.
- **Conocimiento que aporta:** las APIs en el contexto de sistemas distribuidos.
- **Vocabulario técnico:** *API gateway*, *contract testing*, *BFF (backend for frontend)*, *service discovery*.
- **Razonamiento que aporta:** trade-offs de estilos de comunicación inter-servicio.

#### A3 — *gRPC: Up and Running*
- **Cobertura conceptual:** Protocol Buffers, RPC, streaming (uni/bidireccional), interceptores, deadlines.
- **Cobertura práctica:** construir APIs de alto rendimiento con gRPC.
- **Valor como guía para el LLM:** alternativa a REST con vocabulario distinto (RPC, protobuf) — amplía cobertura.
- **Conocimiento que aporta:** el paradigma RPC moderno y los formatos binarios.
- **Vocabulario técnico:** *protobuf*, *stub*, *streaming RPC*, *deadline*, *interceptor*, *IDL*.
- **Razonamiento que aporta:** trade-offs REST vs gRPC (rendimiento, contratos, tooling).

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | FastAPI documentation / Full Stack | S. Ramírez (tiangolo) | 2023 | 2 | 5 | Alta | 5 | 1 |
| P2 | Designing APIs with Swagger and OpenAPI | J. Ponelat, L. Rosenstock | 2022 | 2 | 4 | Alta | 4 | 1 |
| P3 | Irresistible APIs | K. L. Hunter | 2016 | 2 | 2 | Baja | 3 | 1 |

#### P1 — *FastAPI*
- **Cobertura conceptual:** validación con Pydantic, async, inyección de dependencias, generación automática de OpenAPI, autenticación.
- **Cobertura práctica:** construir APIs Python modernas, tipadas y documentadas (relevante para la Etapa 2 del lab).
- **Valor como guía para el LLM:** documentación excepcional; código Python tipado — conecta con `python` y `apis`.
- **Conocimiento que aporta:** el framework de APIs Python dominante actual.
- **Vocabulario técnico:** *path operation*, *dependency injection*, *Pydantic model*, *async endpoint*, *response model*.
- **Razonamiento que aporta:** diseño de APIs tipadas con validación declarativa.

#### P2 — *Designing APIs with Swagger and OpenAPI*
- **Cobertura conceptual:** especificación OpenAPI, diseño API-first, generación de código y documentación, mocking.
- **Cobertura práctica:** definir contratos OpenAPI y generar artefactos a partir de ellos.
- **Valor como guía para el LLM:** el formato OpenAPI es ubicuo; enseña el registro "especificación declarativa".
- **Conocimiento que aporta:** el estándar de descripción de APIs.
- **Vocabulario técnico:** *OpenAPI*, *schema*, *path*, *component*, *API-first*, *contract*.
- **Razonamiento que aporta:** diseño contract-first y generación a partir de especificaciones.

#### P3 — *Irresistible APIs*
- **Cobertura conceptual:** APIs como producto, alineación con valor de negocio, ciclo de vida.
- **Cobertura práctica:** planificar APIs orientadas a negocio.
- **Valor como guía para el LLM:** perspectiva de producto/negocio — diversidad de registro.
- **Conocimiento que aporta:** la dimensión de producto de las APIs.
- **Vocabulario técnico:** *API product*, *value proposition*, *consumer journey*.
- **Razonamiento que aporta:** alineación negocio-API.

## Papers y artículos clave

- Fielding, R. (2000). *Architectural Styles and the Design of Network-based Software Architectures* (REST). [enlace](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
- Google. *API Improvement Proposals (AIPs)*. [aip.dev](https://google.aip.dev/)
- IETF RFC 9110 — *HTTP Semantics*. [enlace](https://www.rfc-editor.org/rfc/rfc9110)
- IETF RFC 7807 / 9457 — *Problem Details for HTTP APIs*.

## Documentación oficial / referencia

- [OpenAPI Specification](https://spec.openapis.org/), [JSON Schema](https://json-schema.org/), [GraphQL](https://graphql.org/learn/).
- [FastAPI](https://fastapi.tiangolo.com/), [Swagger](https://swagger.io/docs/).
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines) y [Google AIPs](https://google.aip.dev/).

## Blogs técnicos

- [Nordic APIs](https://nordicapis.com/blog/).
- [API Evangelist (Kin Lane)](https://apievangelist.com/).
- [Stripe blog — engineering](https://stripe.com/blog/engineering) — referencia de diseño de APIs.
- [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/).

## Repositorios GitHub

- [public-apis/public-apis](https://github.com/public-apis/public-apis).
- [microsoft/api-guidelines](https://github.com/microsoft/api-guidelines).
- [OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification).

## Benchmarks / proxy

- No hay benchmark de "calidad de prosa"; proxy = presencia de especificaciones OpenAPI válidas y ejemplos de request/response completos.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

- **APIs.guru OpenAPI Directory** (miles de specs OpenAPI reales, *verificar licencia por API*).
- **Documentación oficial** de FastAPI/OpenAPI/Stripe (verificar licencia).
- **Stack Exchange — Stack Overflow** (tags: rest, api, openapi, graphql — CC BY-SA, *verificar atribución*).
