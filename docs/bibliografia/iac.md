# Bibliografía — Infraestructura como Código

> Dominio `iac` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Terraform: Up & Running (3ª ed.) | Y. Brikman | 2022 | 3 | 5 | Alta | 5 | 2 |
| F2 | Infrastructure as Code (2ª ed.) | K. Morris | 2020 | 3 | 5 | Alta | 5 | 2 |
| F3 | Ansible: Up and Running (3ª ed.) | B. Meijer, L. Hochstein, R. Moser | 2022 | 2 | 4 | Media | 4 | 1 |

#### F1 — *Terraform: Up & Running*
- **Cobertura conceptual:** Terraform básico, variables, outputs, módulos, estado remoto, workspaces, testing, integración CI/CD.
- **Cobertura práctica:** el texto de referencia para Terraform; desde primeros recursos hasta módulos reutilizables de producción.
- **Valor como guía para el LLM:** el texto más completo del dominio IaC para AWS/Terraform; vocabulario canónico de la herramienta líder.
- **Conocimiento que aporta:** el ciclo completo de gestión de infraestructura con Terraform: desde recursos simples hasta módulos de equipo.
- **Vocabulario técnico:** *resource*, *data source*, *module*, *state*, *remote backend*, *workspace*, *variable*, *output*, *provider*, *plan/apply/destroy*.
- **Razonamiento que aporta:** diseño de módulos reutilizables, gestión de entornos múltiples, estrategias de actualización segura.

#### F2 — *Infrastructure as Code*
- **Cobertura conceptual:** principios de IaC, herramientas (Terraform, CloudFormation, Ansible, Puppet), patrones, testing, pipelines.
- **Cobertura práctica:** marco conceptual y práctico para elegir herramientas y aplicar principios de IaC en cualquier organización.
- **Valor como guía para el LLM:** el texto conceptual más completo de IaC; aporta los principios agnósticos de herramientas.
- **Conocimiento que aporta:** los principios fundamentales de IaC: idempotencia, código versionado, infraestructura inmutable.
- **Vocabulario técnico:** *idempotencia*, *infraestructura inmutable*, *snowflake server*, *drift*, *declarativo vs imperativo*, *pipeline de infraestructura*.
- **Razonamiento que aporta:** elección entre herramientas IaC, diseño de pipelines de infraestructura, gestión de configuración vs. provisioning.

#### F3 — *Ansible: Up and Running*
- **Cobertura conceptual:** inventarios, playbooks, roles, variables, templates, módulos, handlers, tags, vault, testing.
- **Cobertura práctica:** automatizar la configuración de servidores y el despliegue de aplicaciones con Ansible.
- **Valor como guía para el LLM:** Ansible como complemento a Terraform; vocabulario de gestión de configuración con el enfoque agentless.
- **Conocimiento que aporta:** la gestión de configuración con Ansible, complementaria al provisioning de Terraform.
- **Vocabulario técnico:** *inventory*, *playbook*, *role*, *task*, *handler*, *template (Jinja2)*, *vault*, *idempotent module*, *gathering facts*.
- **Razonamiento que aporta:** diseño de roles reutilizables, idempotencia en gestión de configuración, separación de concerns IaC.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Cloud Native Infrastructure | J. Garrison, K. Nova | 2017 | 4 | 4 | Media | 4 | 2 |
| A2 | Kubernetes: Up and Running (3ª ed.) | B. Burns, J. Beda, K. Hightower, L. Evenson | 2022 | 3 | 4 | Media | 5 | 2 |
| A3 | GitOps and Kubernetes | B. Yuen, A. Matyushentsev, T. Ekenstam, J. Suen | 2021 | 4 | 4 | Media | 4 | 2 |

#### A1 — *Cloud Native Infrastructure*
- **Cobertura conceptual:** infraestructura cloud-native, patrones de gestión de infraestructura, ciclo de vida de APIs de infraestructura, observabilidad.
- **Cobertura práctica:** diseñar infraestructura que responda a las necesidades de aplicaciones cloud-native.
- **Valor como guía para el LLM:** vocabulario y principios de infraestructura cloud-native desde la perspectiva de ingenieros de infraestructura cloud-native.
- **Conocimiento que aporta:** el marco conceptual de infraestructura diseñada para la nube, no solo migrada a ella.
- **Vocabulario técnico:** *infrastructure API*, *reconciliation loop*, *desired state*, *actual state*, *operator pattern*, *custom resource*.
- **Razonamiento que aporta:** diseño de sistemas de infraestructura con principios de software, gestión de estado declarativo.

#### A2 — *Kubernetes: Up and Running*
- **Cobertura conceptual:** Pods, Services, Deployments, ConfigMaps, Secrets, StatefulSets, DaemonSets, Helm, RBAC.
- **Cobertura práctica:** desplegar y operar aplicaciones en Kubernetes — la plataforma de orquestación de referencia.
- **Valor como guía para el LLM:** el texto de Kubernetes más referenciado; vocabulario de contenedores y orquestación.
- **Conocimiento que aporta:** Kubernetes como plataforma de IaC para aplicaciones: declarativo, reconciliación, autoscaling.
- **Vocabulario técnico:** *Pod*, *Deployment*, *Service*, *Ingress*, *ConfigMap*, *Secret*, *PersistentVolume*, *Helm chart*, *namespace*.
- **Razonamiento que aporta:** diseño de despliegues Kubernetes seguros y escalables, gestión de estado con StatefulSets.

#### A3 — *GitOps and Kubernetes*
- **Cobertura conceptual:** principios GitOps, flujo de trabajo, herramientas (Flux, ArgoCD), testing, seguridad, escalado.
- **Cobertura práctica:** implementar GitOps para gestionar infraestructura Kubernetes desde Git.
- **Valor como guía para el LLM:** el paradigma GitOps como evolución de IaC; vocabulario de la práctica más moderna del campo.
- **Conocimiento que aporta:** GitOps como la práctica que unifica IaC, CI/CD y Kubernetes en un flujo coherente.
- **Vocabulario técnico:** *GitOps operator*, *reconciliation*, *pull-based deployment*, *ArgoCD application*, *Flux kustomization*, *drift detection*.
- **Razonamiento que aporta:** diseño de pipelines GitOps, gestión de secretos, estrategias de rollback automatizado.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Pulumi documentation (conceptos y guías) | Pulumi Corp. | Continuo | 3 | 3 | Baja | 4 | 2 |
| P2 | AWS CloudFormation User Guide | AWS | Continuo | 2 | 4 | Media | 5 | 1 |
| P3 | The DevOps Handbook (caps. de IaC) | G. Kim, P. Debois, J. Willis, J. Humble | 2016 | 2 | 4 | Alta | 5 | 1 |

#### P1 — *Pulumi documentation*
- **Cobertura conceptual:** IaC con lenguajes reales (Python, TypeScript, Go), componentes, stacks, backends, testing, políticas.
- **Cobertura práctica:** la alternativa a Terraform que usa código real en lugar de HCL.
- **Valor como guía para el LLM:** IaC con Python real — directamente relevante para el stack del laboratorio.
- **Conocimiento que aporta:** la perspectiva de IaC con lenguajes de programación completos; el futuro de la práctica.
- **Vocabulario técnico:** *stack*, *component*, *resource output*, *dynamic provider*, *policy pack*, *Pulumi Cloud*, *automation API*.
- **Razonamiento que aporta:** diseño de abstracciones de infraestructura con lenguajes completos, testing de IaC.

#### P2 — *AWS CloudFormation User Guide*
- **Cobertura conceptual:** templates, stacks, nested stacks, change sets, drift detection, macros, custom resources.
- **Cobertura práctica:** el IaC nativo de AWS; obligatorio para entender SAM y CDK que lo usan como base.
- **Valor como guía para el LLM:** documentación técnica oficial con ejemplos YAML/JSON de CloudFormation.
- **Conocimiento que aporta:** el sistema nativo de IaC de AWS que subyace a SAM, CDK y muchas integraciones.
- **Vocabulario técnico:** *template*, *stack*, *change set*, *DependsOn*, *Outputs*, *Mappings*, *Conditions*, *Custom Resource*, *macro*.
- **Razonamiento que aporta:** diseño de templates CloudFormation, gestión de dependencias entre recursos, rollback de stacks.

#### P3 — *The DevOps Handbook* (capítulos de IaC)
- **Cobertura conceptual:** IaC como práctica DevOps: ambiente idéntico en dev/staging/prod, testing de infraestructura, hardening.
- **Cobertura práctica:** integrar IaC en el flujo de trabajo DevOps; tratar la infraestructura como código de aplicación.
- **Valor como guía para el LLM:** IaC en el contexto cultural y organizacional de DevOps; complementa los textos técnicos.
- **Conocimiento que aporta:** el contexto organizacional de IaC: por qué es importante, cómo se integra en el trabajo de equipo.
- **Vocabulario técnico:** *environment parity*, *infrastructure pipeline*, *blue-green infrastructure*, *chaos engineering*, *immutable infrastructure*.
- **Razonamiento que aporta:** razonamiento sobre beneficios de IaC para equipos, gestión del riesgo en cambios de infraestructura.

## Papers importantes

- Hüttermann, M. — *DevOps for Developers* (capítulo sobre IaC, Apress 2012).
- Humble, J. & Farley, D. — *Continuous Delivery* (Addison-Wesley, 2010) — principios que motivaron IaC.
- Wiggins, A. — *The Twelve-Factor App* (2012). [link](https://12factor.net/) — principios de aplicaciones cloud-native que requieren IaC.

## Documentación oficial

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs) — verificar licencia (Terraform pasó a BSL 1.1 en 2023); la referencia más completa del dominio.
- [Pulumi documentation](https://www.pulumi.com/docs/) — Apache-2.0.
- [Ansible documentation](https://docs.ansible.com/) — GPL-3.0.
- [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/) — Apache-2.0; CDK con TypeScript/Python.

## Blogs técnicos

- [HashiCorp Blog](https://www.hashicorp.com/blog/) — Terraform y el ecosistema HCL.
- [Gruntwork Blog](https://blog.gruntwork.io/) — Terraform avanzado (autores del libro F1).
- [infoq.com — DevOps/IaC](https://www.infoq.com/devops/) — artículos técnicos de la comunidad.
- [thoughtworks.com/radar](https://www.thoughtworks.com/radar) — evaluación de tecnologías IaC (GitOps, Pulumi, etc.).
- [Spacelift Blog](https://spacelift.io/blog) — Terraform y GitOps en profundidad.

## Repositorios GitHub

- [hashicorp/terraform](https://github.com/hashicorp/terraform) — código fuente de Terraform (MPL-2.0 / BSL 1.1).
- [pulumi/pulumi](https://github.com/pulumi/pulumi) — código fuente de Pulumi (Apache-2.0).
- [ansible/ansible](https://github.com/ansible/ansible) — código fuente de Ansible (GPL-3.0).
- [aws/aws-cdk](https://github.com/aws/aws-cdk) — CDK oficial de AWS (Apache-2.0).
- [gruntwork-io/terragrunt](https://github.com/gruntwork-io/terragrunt) — wrapper de Terraform para DRY (MIT).

## Benchmarks

- No existe un benchmark estándar específico para IaC. Proxies útiles:
  - **Tiempo de convergencia** — cuánto tarda en aprovisionar N recursos.
  - **Test coverage de módulos IaC** — cobertura de testing como proxy de calidad.
  - Para evaluar el LLM: preguntas de examen Terraform Associate (HashiCorp Certified).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| Terraform Registry modules | Varía por módulo — verificar licencia | Módulos públicos con código y documentación |
| Ansible Galaxy roles | GPL/Apache (varía) | Roles públicos con tareas y documentación |
| AWS CloudFormation templates (GitHub) | Apache-2.0 (mayoría) | Templates de referencia oficiales de AWS |
| Pulumi examples | Apache-2.0 | Ejemplos oficiales de Pulumi en múltiples lenguajes |
| Stack Overflow [terraform] tag dump | CC BY-SA 4.0 | Preguntas y respuestas de Terraform |
