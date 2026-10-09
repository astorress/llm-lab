# Bibliografía — Serverless Framework

> Dominio `serverless` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Serverless Architectures on AWS (2ª ed.) | P. Sbarski, Y. Cui, A. Nair | 2022 | 3 | 5 | Alta | 4 | 1 |
| F2 | AWS Lambda Quick Start Guide | M. Klems | 2018 | 1 | 4 | Alta | 3 | 1 |
| F3 | The Cloud Resume Challenge Book | F. Brazeal | 2021 | 1 | 3 | Media | 4 | 1 |

#### F1 — *Serverless Architectures on AWS*
- **Cobertura conceptual:** patrones serverless, Lambda, API Gateway, DynamoDB, autenticación con Cognito, Step Functions, event-driven.
- **Cobertura práctica:** construir aplicaciones serverless de producción completas en AWS.
- **Valor como guía para el LLM:** el texto más completo del dominio; cubre el ciclo completo de diseño serverless con vocabulario oficial.
- **Conocimiento que aporta:** la arquitectura serverless completa para aplicaciones modernas: API, auth, datos, eventos.
- **Vocabulario técnico:** *event source*, *trigger*, *cold start*, *Lambda function*, *Step Functions state machine*, *Cognito pool*, *API Gateway stage*.
- **Razonamiento que aporta:** diseño de arquitecturas event-driven, gestión de estado en sistemas stateless, seguridad serverless.

#### F2 — *AWS Lambda Quick Start Guide*
- **Cobertura conceptual:** fundamentos de Lambda: handlers, triggers, variables de entorno, layers, testing, debugging, monitoreo.
- **Cobertura práctica:** poner en producción funciones Lambda funcionales rápidamente.
- **Valor como guía para el LLM:** texto introductorio conciso con ejemplos directos; aporta la curva de onboarding del dominio.
- **Conocimiento que aporta:** los fundamentos de Lambda en su forma más directa y práctica.
- **Vocabulario técnico:** *handler function*, *event object*, *context object*, *Lambda Layer*, *environment variable*, *execution role*, *timeout*, *memory*.
- **Razonamiento que aporta:** estructuración de funciones Lambda, manejo de errores, configuración de recursos.

#### F3 — *The Cloud Resume Challenge Book*
- **Cobertura conceptual:** proyecto completo: S3 static site, CloudFront, Lambda, DynamoDB, API Gateway, SAM, GitHub Actions.
- **Cobertura práctica:** proyecto integrador de múltiples servicios serverless — excelente ejercicio práctico.
- **Valor como guía para el LLM:** registro narrativo de un proyecto completo con decisiones explicadas; conecta todos los servicios serverless.
- **Conocimiento que aporta:** la integración de múltiples servicios serverless en un proyecto coherente de principio a fin.
- **Vocabulario técnico:** *SAM template*, *CloudFront distribution*, *S3 static website*, *API Gateway route*, *CORS*, *GitHub Actions workflow*.
- **Razonamiento que aporta:** toma de decisiones en un proyecto serverless real, debugging de integraciones entre servicios.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Serverless Design Patterns and Best Practices | B. Zambrano | 2018 | 3 | 5 | Alta | 4 | 2 |
| A2 | Production-Ready Serverless (curso, Manning) | Y. Cui | 2018 | 4 | 5 | Alta | 5 | 2 |
| A3 | Building Serverless Applications on Knative | E. Anderson | 2023 | 4 | 3 | Baja | 4 | 2 |

#### A1 — *Serverless Design Patterns and Best Practices*
- **Cobertura conceptual:** patrones serverless: command, API gateway, fan-out, event streaming, saga, scheduled jobs.
- **Cobertura práctica:** aplicar patrones de diseño al mundo serverless; resolver problemas comunes con soluciones probadas.
- **Valor como guía para el LLM:** catálogo de patrones serverless con código; el "GoF patterns" del mundo serverless.
- **Conocimiento que aporta:** los patrones de diseño específicos del paradigma serverless que resuelven problemas recurrentes.
- **Vocabulario técnico:** *fan-out*, *saga pattern*, *choreography*, *orchestration*, *compensating transaction*, *idempotency key*, *command pattern*.
- **Razonamiento que aporta:** selección de patrón serverless por tipo de problema, análisis de trade-offs de consistencia.

#### A2 — *Production-Ready Serverless* (Yan Cui)
- **Cobertura conceptual:** testing de Lambda, observabilidad, performance, seguridad, resiliencia, gestión de secretos, CI/CD.
- **Cobertura práctica:** llevar funciones Lambda a producción con calidad de ingeniería de nivel enterprise.
- **Valor como guía para el LLM:** el texto más completo de serverless en producción; vocabulario de operaciones serverless.
- **Conocimiento que aporta:** el nivel de madurez operacional que diferencia un prototipo serverless de una aplicación de producción.
- **Vocabulario técnico:** *structured logging*, *correlation ID*, *tracing*, *X-Ray segment*, *Lumigo*, *Lambda Power Tuning*, *canary deployment*.
- **Razonamiento que aporta:** estrategias de testing de funciones, observabilidad en sistemas distribuidos serverless.

#### A3 — *Building Serverless Applications on Knative*
- **Cobertura conceptual:** Knative Serving y Eventing, serverless en Kubernetes, cloud-agnostic serverless, KEDA.
- **Cobertura práctica:** serverless en Kubernetes para evitar vendor lock-in.
- **Valor como guía para el LLM:** perspectiva de serverless agnóstico de nube; vocabulario de Kubernetes y serverless convergentes.
- **Conocimiento que aporta:** la dimensión de portabilidad del serverless más allá de AWS Lambda específicamente.
- **Vocabulario técnico:** *Knative Service*, *Revision*, *autoscaling to zero*, *KEDA*, *CloudEvents*, *Broker*, *Trigger*, *Sink*.
- **Razonamiento que aporta:** comparación entre serverless administrado (AWS) vs. auto-hospedado (Knative); trade-offs de portabilidad.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Serverless Framework Documentation | Serverless Inc. | Continuo | 2 | 5 | Alta | 5 | 1 |
| P2 | AWS SAM (Serverless Application Model) Guide | AWS | Continuo | 2 | 4 | Alta | 5 | 1 |
| P3 | Serverless Stack (SST) Guide | SST contributors | Continuo | 2 | 4 | Media | 4 | 1 |

#### P1 — *Serverless Framework Documentation*
- **Cobertura conceptual:** serverless.yml, funciones, eventos, plugins, stages, variables, packaging, despliegue.
- **Cobertura práctica:** la referencia oficial del framework más usado para desplegar funciones serverless.
- **Valor como guía para el LLM:** documentación técnica de alta calidad con ejemplos de configuración YAML — vocabulario del framework.
- **Conocimiento que aporta:** la sintaxis y capacidades del Serverless Framework de referencia; vocabulario oficial del proyecto.
- **Vocabulario técnico:** *serverless.yml*, *functions*, *events*, *plugins*, *stages*, *custom variables*, *packaging*, *provider block*.
- **Razonamiento que aporta:** estructuración de proyectos serverless, gestión de múltiples entornos, configuración de permisos.

#### P2 — *AWS SAM Guide*
- **Cobertura conceptual:** SAM template, SAM CLI, testing local, debugging, despliegue con CloudFormation.
- **Cobertura práctica:** la alternativa oficial de AWS al Serverless Framework; muy integrada con los servicios AWS.
- **Valor como guía para el LLM:** documentación oficial AWS con vocabulario de SAM/CloudFormation; complementa al Serverless Framework.
- **Conocimiento que aporta:** el enfoque oficial de AWS para definir aplicaciones serverless como código.
- **Vocabulario técnico:** *SAM template*, *AWS::Serverless::Function*, *AWS::Serverless::Api*, *sam local invoke*, *sam deploy*, *nested stacks*.
- **Razonamiento que aporta:** decisiones entre Serverless Framework y SAM, integración con CloudFormation.

#### P3 — *SST (Serverless Stack) Guide*
- **Cobertura conceptual:** SST, CDK, desarrollo local con Live Lambda, constructs de alto nivel, fullstack serverless.
- **Cobertura práctica:** el framework serverless de nueva generación con TypeScript y CDK.
- **Valor como guía para el LLM:** perspectiva moderna del desarrollo serverless con las herramientas más recientes.
- **Conocimiento que aporta:** el estado actual del ecosistema serverless en 2022-2024 con constructs de alto nivel.
- **Vocabulario técnico:** *SST construct*, *Live Lambda Development*, *CDK stack*, *Ion*, *console dashboard*, *Function construct*.
- **Razonamiento que aporta:** desarrollo y debugging local de funciones Lambda, gestión de infraestructura con TypeScript.

## Papers importantes

- Hellerstein, J. et al. — *Serverless Computing: One Step Forward, Two Steps Back* (CIDR 2019). [arXiv:1812.03651](https://arxiv.org/abs/1812.03651)
- Jonas, E. et al. — *Cloud Programming Simplified: A Berkeley View on Serverless Computing* (UCB Tech Report 2019). [arXiv:1902.03383](https://arxiv.org/abs/1902.03383)
- Wang, L. et al. — *Peeking Behind the Curtains of Serverless Platforms* (ATC 2018).
- Shahrad, M. et al. — *Serverless in the Wild: Characterizing and Optimizing the Serverless Workload at a Large Cloud Provider* (ATC 2020).

## Documentación oficial

- [Serverless Framework documentation](https://www.serverless.com/framework/docs/) — referencia del framework (MIT).
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/) — documentación oficial de Lambda.
- [AWS SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/) — guía oficial de SAM.
- [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/) — orquestación serverless.

## Blogs técnicos

- [The Burning Monk (Y. Cui)](https://theburningmonk.com/) — el blog de referencia para Lambda avanzado y observabilidad.
- [Lumigo blog](https://lumigo.io/blog/) — serverless, observabilidad, performance.
- [Serverless Land (AWS)](https://serverlessland.com/) — recursos, patrones y ejemplos serverless de AWS.
- [Off-by-none (J. Daly)](https://offbynone.io/) — newsletter serverless.
- [Serverless Tips (Paul Swail)](https://serverlessfirst.com/) — prácticas de producción serverless.

## Repositorios GitHub

- [serverless/serverless](https://github.com/serverless/serverless) — Serverless Framework (MIT).
- [aws/aws-sam-cli](https://github.com/aws/aws-sam-cli) — SAM CLI (Apache-2.0).
- [sst/sst](https://github.com/sst/sst) — Serverless Stack (MIT).
- [alexcasalboni/aws-lambda-power-tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning) — optimización de memoria Lambda (Apache-2.0).
- [yan-cui/production-ready-serverless](https://github.com/yan-cui/production-ready-serverless) — código de Production Serverless.

## Benchmarks

- **AWS Lambda Power Tuning** — herramienta para encontrar la configuración óptima de memoria/costo.
- **Cold start benchmarks** — mediciones públicas de cold starts por runtime y framework.
- Para evaluar el LLM: preguntas de AWS Certified Developer Associate sobre Lambda y serverless.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| Serverless Framework documentation | MIT (código) | Documentación y ejemplos del framework |
| AWS Lambda developer guide | AWS documentation license | Guía oficial con ejemplos de código |
| Serverless examples (GitHub) | MIT (mayoría) | Repositorio oficial de ejemplos del Serverless Framework |
| FunctionBench dataset | Apache-2.0 | Benchmark de funciones Lambda con trazas de ejecución |
| Azure Functions benchmark data | Verificar licencia | Datos comparativos de plataformas FaaS |
