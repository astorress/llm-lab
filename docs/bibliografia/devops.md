# Bibliografía — DevOps

> Dominio `devops` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | The DevOps Handbook (2ª ed.) | G. Kim, J. Humble, P. Debois, J. Willis, N. Forsgren | 2021 | 2 | 5 | Alta | 5 | 1 |
| F2 | Site Reliability Engineering | Google (Beyer, Jones, Petoff, Murphy) | 2016 | 3 | 5 | Alta | 5 | 1 |
| F3 | Accelerate | N. Forsgren, J. Humble, G. Kim | 2018 | 2 | 4 | Alta | 5 | 2 |

#### F1 — *The DevOps Handbook*
- **Cobertura conceptual:** las Tres Vías (flujo, feedback, aprendizaje), CI/CD, telemetría, cultura, value stream.
- **Cobertura práctica:** implementar prácticas DevOps end-to-end en una organización.
- **Valor como guía para el LLM:** el texto de referencia del campo; vocabulario y principios canónicos.
- **Conocimiento que aporta:** el marco conceptual unificado de DevOps.
- **Vocabulario técnico:** *deployment pipeline*, *value stream*, *lead time*, *deployment frequency*, *blameless culture*.
- **Razonamiento que aporta:** razonamiento sobre flujo de valor y mejora continua.

#### F2 — *Site Reliability Engineering*
- **Cobertura conceptual:** SLO/SLI, error budgets, monitoring, alerting, gestión de incidentes, eliminación de toil.
- **Cobertura práctica:** operar sistemas a escala con fiabilidad medible (la implementación de DevOps de Google).
- **Valor como guía para el LLM:** casos reales de operación a escala; vocabulario SRE compartido con sistemas distribuidos.
- **Conocimiento que aporta:** la disciplina cuantitativa de fiabilidad.
- **Vocabulario técnico:** *SLO*, *SLI*, *error budget*, *toil*, *postmortem*, *cascading failure*, *golden signals*.
- **Razonamiento que aporta:** decisiones operativas basadas en presupuestos de error y datos.

#### F3 — *Accelerate*
- **Cobertura conceptual:** las métricas DORA, investigación empírica sobre qué prácticas predicen rendimiento.
- **Cobertura práctica:** medir y mejorar el rendimiento de entrega de software con rigor estadístico.
- **Valor como guía para el LLM:** combina ingeniería con metodología de investigación — registro poco común.
- **Conocimiento que aporta:** la evidencia cuantitativa detrás de las prácticas DevOps.
- **Vocabulario técnico:** *DORA metrics*, *deployment frequency*, *MTTR*, *change failure rate*, *lead time for changes*.
- **Razonamiento que aporta:** razonamiento basado en evidencia y métricas predictivas.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Continuous Delivery | J. Humble, D. Farley | 2010 | 3 | 4 | Alta | 5 | 1 |
| A2 | Kubernetes Up & Running (3ª ed.) | B. Burns, J. Beda, K. Hightower, L. Evenson | 2022 | 3 | 4 | Alta | 5 | 1 |
| A3 | The Site Reliability Workbook | Google (Beyer et al.) | 2018 | 3 | 3 | Media | 5 | 1 |

#### A1 — *Continuous Delivery*
- **Cobertura conceptual:** deployment pipeline, automatización de builds/tests/releases, gestión de configuración, estrategias de despliegue.
- **Cobertura práctica:** construir un pipeline de entrega continua robusto.
- **Valor como guía para el LLM:** el origen del concepto de pipeline de despliegue.
- **Conocimiento que aporta:** la base teórica de CI/CD.
- **Vocabulario técnico:** *deployment pipeline*, *blue-green*, *canary*, *feature toggle*, *artifact repository*.
- **Razonamiento que aporta:** diseño de procesos de release de bajo riesgo.

#### A2 — *Kubernetes Up & Running*
- **Cobertura conceptual:** pods, deployments, services, ingress, configmaps, operators, autoscaling.
- **Cobertura práctica:** desplegar y operar aplicaciones en Kubernetes.
- **Valor como guía para el LLM:** vocabulario de orquestación de contenedores omnipresente; conecta con IaC y AWS.
- **Conocimiento que aporta:** el sistema de orquestación dominante.
- **Vocabulario técnico:** *pod*, *deployment*, *StatefulSet*, *ingress*, *HPA*, *operator*, *namespace*.
- **Razonamiento que aporta:** diseño declarativo de infraestructura y reconciliación de estado.

#### A3 — *The Site Reliability Workbook*
- **Cobertura conceptual:** aplicación práctica de los principios SRE, ejemplos de implementación de SLOs.
- **Cobertura práctica:** llevar la teoría SRE a la práctica en organizaciones no-Google.
- **Valor como guía para el LLM:** complemento aplicado del libro SRE; ejemplos concretos.
- **Conocimiento que aporta:** la implementación práctica de SRE.
- **Vocabulario técnico:** *SLO engineering*, *alerting on SLOs*, *capacity planning*, *load testing*.
- **Razonamiento que aporta:** traducción de principios a prácticas medibles.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | The Phoenix Project | G. Kim, K. Behr, G. Spafford | 2013 | 1 | 4 | Alta | 4 | 1 |
| P2 | Docker Deep Dive | N. Poulton | 2023 | 2 | 4 | Alta | 4 | 1 |
| P3 | Learning GitHub Actions | B. Laster | 2023 | 2 | 3 | Media | 4 | 1 |

#### P1 — *The Phoenix Project*
- **Cobertura conceptual:** novela que ilustra DevOps a través de una transformación organizacional (basada en Teoría de Restricciones).
- **Cobertura práctica:** entender el *por qué* cultural de DevOps mediante narrativa.
- **Valor como guía para el LLM:** registro narrativo técnico — diversidad textual valiosa.
- **Conocimiento que aporta:** la motivación y el contexto organizacional de DevOps.
- **Vocabulario técnico:** *WIP*, *bottleneck*, *Theory of Constraints*, *unplanned work*, *four types of work*.
- **Razonamiento que aporta:** razonamiento sistémico sobre flujo y cuellos de botella.

#### P2 — *Docker Deep Dive*
- **Cobertura conceptual:** imágenes, contenedores, registries, networking, volúmenes, Swarm, buenas prácticas de Dockerfile.
- **Cobertura práctica:** containerizar aplicaciones correctamente.
- **Valor como guía para el LLM:** vocabulario de contenedores base; conecta con Kubernetes y CI/CD.
- **Conocimiento que aporta:** los fundamentos de containerización.
- **Vocabulario técnico:** *image layer*, *registry*, *bind mount*, *multi-stage build*, *entrypoint*.
- **Razonamiento que aporta:** optimización de imágenes y aislamiento de procesos.

#### P3 — *Learning GitHub Actions*
- **Cobertura conceptual:** workflows, jobs, runners, secrets, matrices, reusable workflows.
- **Cobertura práctica:** construir pipelines CI/CD en GitHub Actions (este repo aún no tiene CI configurado).
- **Valor como guía para el LLM:** YAML de CI/CD concreto y muy frecuente en repos públicos.
- **Conocimiento que aporta:** la mecánica de CI/CD en la plataforma dominante.
- **Vocabulario técnico:** *workflow*, *job*, *runner*, *matrix build*, *artifact*, *secret*.
- **Razonamiento que aporta:** automatización declarativa de pipelines.

## Papers y artículos clave

- Forsgren, Humble, Kim (2018). Estudios *State of DevOps / DORA* (anuales). [DORA](https://dora.dev/research/).
- Google. *Borg, Omega, and Kubernetes* (2016). ACM Queue.
- Burns, Oppenheimer (2016). *Design Patterns for Container-based Distributed Systems*.

## Documentación oficial / referencia

- [Docker docs](https://docs.docker.com/), [Kubernetes docs](https://kubernetes.io/docs/), [GitHub Actions](https://docs.github.com/actions).
- [Prometheus](https://prometheus.io/docs/) y [Grafana](https://grafana.com/docs/) — monitoreo.
- [DORA — DevOps Research and Assessment](https://dora.dev/).

## Blogs técnicos

- [Google Cloud — DevOps & SRE](https://cloud.google.com/blog/products/devops-sre).
- [Honeycomb blog](https://www.honeycomb.io/blog) — observabilidad.
- [Gruntwork blog](https://blog.gruntwork.io/) — IaC y DevOps.
- [Julia Evans (jvns.ca)](https://jvns.ca/) — sistemas y debugging.

## Repositorios GitHub

- [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises).
- [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way).
- [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge).

## Benchmarks / proxy

- **Métricas DORA** (deployment frequency, lead time, MTTR, change failure rate) como proxy de madurez.
- No hay benchmarks numéricos de "calidad de texto"; proxy = presencia de pipelines reales (YAML) y postmortems.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

- **Documentación oficial** de Docker/Kubernetes/Prometheus (Apache 2.0 / permisivas).
- **GitHub Actions workflows** públicos (filtrar por licencia).
- **Stack Exchange — DevOps / Server Fault** (CC BY-SA, *verificar atribución*).
