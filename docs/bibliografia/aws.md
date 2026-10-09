# Bibliografía — AWS

> Dominio `aws` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Amazon Web Services in Action (3ª ed.) | A. Wittig, M. Wittig | 2023 | 2 | 5 | Alta | 5 | 1 |
| F2 | AWS Certified Solutions Architect Study Guide (4ª ed.) | B. Piper, D. Clinton | 2022 | 2 | 4 | Alta | 4 | 1 |
| F3 | Cloud Computing: Concepts, Technology & Architecture | T. Erl, R. Puttini, Z. Mahmood | 2013 | 3 | 3 | Media | 4 | 2 |

#### F1 — *Amazon Web Services in Action*
- **Cobertura conceptual:** EC2, VPC, RDS, S3, Lambda, CloudFormation, IAM, ECS, SQS, SNS, DynamoDB, CloudWatch.
- **Cobertura práctica:** el texto más completo para usar AWS en proyectos reales; examples con código CloudFormation.
- **Valor como guía para el LLM:** la cobertura más amplia de AWS con vocabulario de infraestructura cloud moderno.
- **Conocimiento que aporta:** el stack AWS completo para proyectos de datos y ML — tema del corpus y de la Etapa 2 (el código de este repo no usa AWS).
- **Vocabulario técnico:** *VPC*, *subnet*, *security group*, *IAM role*, *S3 bucket policy*, *Auto Scaling*, *ECS task definition*, *CloudWatch alarm*.
- **Razonamiento que aporta:** diseño de arquitecturas AWS para diferentes casos de uso, decisiones de networking y seguridad.

#### F2 — *AWS Certified Solutions Architect Study Guide*
- **Cobertura conceptual:** todos los servicios AWS relevantes para arquitecturas de sistemas: compute, storage, database, networking, security, serverless.
- **Cobertura práctica:** preparación para la certificación SAA-C03; preguntas y respuestas de escenarios reales.
- **Valor como guía para el LLM:** amplia cobertura de servicios AWS con preguntas de escenarios — formato examen útil como guía de temas.
- **Conocimiento que aporta:** la visión de arquitecto de soluciones AWS: cómo combinar servicios para diferentes requisitos.
- **Vocabulario técnico:** *shared responsibility model*, *high availability*, *fault tolerance*, *disaster recovery*, *RTO/RPO*, *multi-AZ*, *read replica*.
- **Razonamiento que aporta:** selección de servicios AWS por requisitos de disponibilidad, costo y rendimiento.

#### F3 — *Cloud Computing: Concepts, Technology & Architecture*
- **Cobertura conceptual:** IaaS/PaaS/SaaS, modelos de despliegue, mecanismos cloud, patrones de arquitectura, SLAs.
- **Cobertura práctica:** marco conceptual para comparar proveedores de nube y diseñar arquitecturas agnósticas.
- **Valor como guía para el LLM:** vocabulario y conceptos de cloud computing más allá de AWS específico; aporta el contexto del dominio.
- **Conocimiento que aporta:** los fundamentos de cloud computing que explican por qué existen los servicios de AWS.
- **Vocabulario técnico:** *elasticidad*, *on-demand*, *multitenancy*, *resource pooling*, *measured service*, *cloud bursting*, *vertical/horizontal scaling*.
- **Razonamiento que aporta:** comparación de modelos de servicio, análisis de trade-offs de arquitecturas cloud.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | AWS Well-Architected Framework | AWS | 2023 | 3 | 5 | Alta | 5 | 1 |
| A2 | Terraform: Up & Running (3ª ed.) | Y. Brikman | 2022 | 3 | 4 | Media | 5 | 2 |
| A3 | Cloud Native Patterns | C. Davis | 2019 | 4 | 4 | Media | 5 | 2 |

#### A1 — *AWS Well-Architected Framework*
- **Cobertura conceptual:** seis pilares: excelencia operacional, seguridad, confiabilidad, eficiencia de rendimiento, optimización de costos y sostenibilidad (añadido en 2021).
- **Cobertura práctica:** evaluar y mejorar arquitecturas AWS contra las mejores prácticas de Amazon.
- **Valor como guía para el LLM:** el framework oficial de mejores prácticas de AWS; vocabulario canónico para evaluar arquitecturas.
- **Conocimiento que aporta:** el estándar de la industria para evaluar arquitecturas en AWS; referencia de todos los arquitectos cloud.
- **Vocabulario técnico:** *pillar*, *trade-off*, *design principle*, *best practice*, *lens*, *workload*, *runbook*, *immutable infrastructure*.
- **Razonamiento que aporta:** evaluación de arquitecturas contra los seis pilares, identificación de áreas de mejora.

#### A2 — *Terraform: Up & Running*
- **Cobertura conceptual:** Terraform básico y avanzado, módulos, estado, backends remotos, workspaces, testing de IaC.
- **Cobertura práctica:** provisionar infraestructura AWS con Terraform — el estándar de la industria para IaC.
- **Valor como guía para el LLM:** el mejor texto de Terraform con ejemplos reales de AWS; referencia cruzada con `iac`.
- **Conocimiento que aporta:** cómo gestionar infraestructura AWS como código con la herramienta más adoptada del mercado.
- **Vocabulario técnico:** *resource*, *module*, *state file*, *remote backend*, *workspace*, *data source*, *output*, *variable*.
- **Razonamiento que aporta:** diseño de módulos reutilizables, gestión de estado, estrategias de actualización segura.

#### A3 — *Cloud Native Patterns*
- **Cobertura conceptual:** microservicios, configuración dinámica, service discovery, circuit breaker, event-driven — en contexto cloud.
- **Cobertura práctica:** diseñar aplicaciones que aprovechen las características de la nube.
- **Valor como guía para el LLM:** patrones de diseño para aplicaciones cloud-native con vocabulario moderno de la industria.
- **Conocimiento que aporta:** los patrones de diseño específicos de cloud que maximizan los beneficios de AWS.
- **Vocabulario técnico:** *circuit breaker*, *service mesh*, *sidecar*, *configuration server*, *event sourcing*, *CQRS*, *strangler fig*.
- **Razonamiento que aporta:** selección de patrones de diseño por requisitos de resiliencia y escalabilidad.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | AWS Lambda in Action | D. Poccia | 2017 | 2 | 4 | Media | 4 | 1 |
| P2 | Data Engineering with AWS | G. Eagar | 2021 | 3 | 5 | Alta | 4 | 2 |
| P3 | Serverless Architectures on AWS (2ª ed.) | P. Sbarski, Y. Cui, A. Nair | 2022 | 3 | 4 | Media | 4 | 1 |

#### P1 — *AWS Lambda in Action*
- **Cobertura conceptual:** Lambda fundamentals, triggers (S3, API Gateway, DynamoDB Streams), patrones serverless, testing.
- **Cobertura práctica:** construir aplicaciones serverless completas con Lambda.
- **Valor como guía para el LLM:** texto práctico de Lambda con vocabulario de serverless en AWS; referencia cruzada con `serverless`.
- **Conocimiento que aporta:** el patrón serverless de AWS desde sus fundamentos hasta arquitecturas completas.
- **Vocabulario técnico:** *handler*, *event source mapping*, *cold start*, *execution role*, *deployment package*, *Layers*, *provisioned concurrency*.
- **Razonamiento que aporta:** diseño de funciones Lambda eficientes, manejo de errores y retries, optimización de cold starts.

#### P2 — *Data Engineering with AWS*
- **Cobertura conceptual:** S3 data lake, Glue, Athena, Redshift, Kinesis, Lake Formation, EMR — el stack de datos de AWS.
- **Cobertura práctica:** construir pipelines de datos completos en AWS — relevante para la Etapa 2 (el pipeline actual del repo es local y no usa AWS).
- **Valor como guía para el LLM:** el stack de datos AWS con vocabulario de ingeniería de datos; referencia cruzada con `data_engineering`.
- **Conocimiento que aporta:** la arquitectura de datos moderna en AWS: desde ingestión hasta análisis y ML.
- **Vocabulario técnico:** *data lake*, *Glue Crawler*, *Athena*, *Redshift Spectrum*, *Kinesis Firehose*, *Lake Formation*, *Data Catalog*.
- **Razonamiento que aporta:** diseño de arquitecturas de datos en AWS, elección entre servicios de análisis.

#### P3 — *Serverless Architectures on AWS*
- **Cobertura conceptual:** arquitecturas serverless completas: API Gateway + Lambda + DynamoDB, autenticación, seguridad, monitoreo.
- **Cobertura práctica:** construir APIs serverless de producción en AWS.
- **Valor como guía para el LLM:** el texto más completo de arquitecturas serverless en AWS; conecta con los dominios `serverless` y `apis`.
- **Conocimiento que aporta:** el patrón completo de arquitectura serverless en AWS para APIs y procesamiento de eventos.
- **Vocabulario técnico:** *API Gateway*, *Lambda authorizer*, *DynamoDB streams*, *SQS dead letter queue*, *X-Ray tracing*, *SAM template*.
- **Razonamiento que aporta:** diseño de flujos serverless, estrategias de autenticación, observabilidad.

## Papers importantes

- Vogels, W. — *Eventually Consistent* (ACM Queue, 2008). [ACM link](https://dl.acm.org/doi/10.1145/1466443.1466448)
- DeCandia, G. et al. — *Dynamo: Amazon's Highly Available Key-value Store* (SOSP 2007).
- AWS Architecture Team — *The Amazon Builders' Library* (2019–presente). [Link](https://aws.amazon.com/builders-library/)

## Documentación oficial

- [AWS Documentation](https://docs.aws.amazon.com/) — documentación oficial de todos los servicios; la fuente primaria del dominio.
- [AWS Architecture Center](https://aws.amazon.com/architecture/) — patrones y referencias de arquitectura.
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — framework y herramienta de revisión.
- [AWS CLI documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html) — referencia de comandos CLI.

## Blogs técnicos

- [AWS News Blog](https://aws.amazon.com/blogs/aws/) — anuncios y tutoriales oficiales de AWS.
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/) — patrones y casos de uso avanzados.
- [The Burning Monk (Y. Cui)](https://theburningmonk.com/) — serverless y Lambda avanzado.
- [Cloudonaut.io](https://cloudonaut.io/) — best practices en AWS con ejemplos prácticos.
- [Last Week in AWS (C. Quinn)](https://www.lastweekinaws.com/) — análisis crítico de novedades AWS.

## Repositorios GitHub

- [aws/aws-cli](https://github.com/aws/aws-cli) — CLI oficial de AWS (Apache-2.0).
- [aws/aws-cdk](https://github.com/aws/aws-cdk) — Cloud Development Kit (Apache-2.0).
- [localstack/localstack](https://github.com/localstack/localstack) — emulador local de servicios AWS (Apache-2.0).
- [boto/boto3](https://github.com/boto/boto3) — SDK de Python para AWS (Apache-2.0).
- [toniblyx/my-arsenal-of-aws-security-tools](https://github.com/toniblyx/my-arsenal-of-aws-security-tools) — herramientas de seguridad AWS.

## Benchmarks

- **SPEC Cloud IaaS** — benchmark estándar para infraestructura cloud.
- Para evaluar el LLM: preguntas de exámenes de certificación AWS (SAA-C03, DVA-C02); AWS ofrece preguntas de práctica oficiales.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| AWS Documentation full text | AWS Customer Agreement (uso referencial) | Toda la documentación oficial de AWS |
| AWS Architecture Blog posts | Copyright de AWS — verificar licencia | Artículos técnicos del equipo de arquitectura |
| AWS Builders' Library | Copyright de AWS — verificar licencia | Artículos de ingeniería de Amazon |
| AWS re:Invent session transcripts | Verificar licencia | Transcripciones de conferencias técnicas |
| Cloud Custodian policies (GitHub) | Apache-2.0 | Políticas de cumplimiento cloud como código |
