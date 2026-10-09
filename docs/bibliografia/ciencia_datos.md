# Bibliografía — Ciencia de Datos

> Dominio `ciencia_datos` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Python for Data Analysis (3ª ed.) | W. McKinney | 2022 | 2 | 5 | Alta | 5 | 2 |
| F2 | Data Science from Scratch (2ª ed.) | J. Grus | 2019 | 2 | 4 | Alta | 4 | 3 |
| F3 | Practical Statistics for Data Scientists (2ª ed.) | P. Bruce, A. Bruce, P. Gedeck | 2020 | 2 | 4 | Alta | 4 | 3 |

#### F1 — *Python for Data Analysis*
- **Cobertura conceptual:** pandas, NumPy, matplotlib, manipulación de datos tabulares, series temporales, limpieza y transformación.
- **Cobertura práctica:** el manual de referencia de pandas; manejo de DataFrames, merges, groupby, rolling windows.
- **Valor como guía para el LLM:** la densidad más alta de código pandas idiomático + comentarios explicativos del dominio.
- **Conocimiento que aporta:** el flujo de trabajo de análisis de datos real: desde ingestión hasta visualización exploratoria.
- **Vocabulario técnico:** *DataFrame*, *Series*, *groupby*, *pivot table*, *reindex*, *merge*, *resample*, *vectorización*.
- **Razonamiento que aporta:** decisiones de limpieza de datos, elección de joins, estrategias de manejo de valores faltantes.

#### F2 — *Data Science from Scratch*
- **Cobertura conceptual:** estadística básica, álgebra lineal, visualización, ML desde cero en Python puro (sin librerías).
- **Cobertura práctica:** implementar KNN, regresión, naive Bayes y redes neuronales pequeñas sin dependencias.
- **Valor como guía para el LLM:** código pedagógico línea a línea sin abstracciones — enseña el "por qué" detrás de cada función.
- **Conocimiento que aporta:** la capa conceptual subyacente a las librerías de ciencia de datos; excelente guía de nivel introductorio.
- **Vocabulario técnico:** *correlación*, *normalización*, *gradient descent*, *feature matrix*, *loss*, *precision*, *recall*.
- **Razonamiento que aporta:** construcción incremental de herramientas; razonamiento desde primeros principios hacia librerías.

#### F3 — *Practical Statistics for Data Scientists*
- **Cobertura conceptual:** estadística aplicada a DS: muestreo, distribuciones, tests de hipótesis, regresión, clasificación.
- **Cobertura práctica:** cuándo usar qué test estadístico; aplicación directa con R/Python.
- **Valor como guía para el LLM:** texto puente entre estadística formal y decisiones prácticas de un analista.
- **Conocimiento que aporta:** el razonamiento estadístico que falta en los libros puramente técnicos de ML.
- **Vocabulario técnico:** *p-value*, *bootstrap*, *effect size*, *ANOVA*, *chi-squared*, *regression to the mean*, *confounding variable*.
- **Razonamiento que aporta:** interpretación de resultados estadísticos, diseño de experimentos, análisis de A/B testing.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Fundamentals of Data Engineering | J. Reis, M. Housley | 2022 | 3 | 4 | Media | 5 | 1 |
| A2 | Designing Data-Intensive Applications | M. Kleppmann | 2017 | 4 | 4 | Media | 5 | 2 |
| A3 | Feature Engineering for Machine Learning | A. Zheng, A. Casari | 2018 | 3 | 5 | Alta | 4 | 2 |

#### A1 — *Fundamentals of Data Engineering*
- **Cobertura conceptual:** ciclo de vida del dato: generación, almacenamiento, ingestión, transformación, serving; arquitecturas modernas.
- **Cobertura práctica:** diseñar pipelines de datos, elegir herramientas (lakes, warehouses, streaming vs. batch).
- **Valor como guía para el LLM:** vocabulario de ingeniería de datos moderno; prosa de arquitectura de sistemas con decisiones razonadas.
- **Conocimiento que aporta:** la capa de infraestructura de datos que precede a todo análisis o entrenamiento de modelos.
- **Vocabulario técnico:** *data lake*, *data warehouse*, *batch ingestion*, *streaming*, *data mesh*, *orchestration*, *data lineage*.
- **Razonamiento que aporta:** trade-offs de arquitectura (batch vs. stream, SQL vs. NoSQL), evaluación de madurez de datos.

#### A2 — *Designing Data-Intensive Applications*
- **Cobertura conceptual:** sistemas distribuidos de datos: replicación, particionamiento, transacciones, streams, consistencia.
- **Cobertura práctica:** diseñar sistemas confiables y escalables; entender las garantías y limitaciones de cada base de datos.
- **Valor como guía para el LLM:** uno de los mejores textos técnicos en términos de claridad explicativa — prosa de alta calidad.
- **Conocimiento que aporta:** la teoría de sistemas detrás de las decisiones de infraestructura de datos.
- **Vocabulario técnico:** *ACID*, *CAP theorem*, *replication lag*, *event log*, *idempotency*, *exactly-once semantics*.
- **Razonamiento que aporta:** análisis de fallos, garantías de consistencia, trade-offs de disponibilidad.

#### A3 — *Feature Engineering for Machine Learning*
- **Cobertura conceptual:** transformaciones de features: encoding categórico, scaling, interacciones, features de texto e imagen.
- **Cobertura práctica:** técnicas concretas de transformación de variables para mejorar modelos ML.
- **Valor como guía para el LLM:** conecta la ciencia de datos exploratoria con el ML aplicado; vocabulario específico del proceso de features.
- **Conocimiento que aporta:** la fase crítica entre EDA y entrenamiento que más impacta el rendimiento del modelo.
- **Vocabulario técnico:** *one-hot encoding*, *target encoding*, *binning*, *log transform*, *feature crossing*, *interaction term*.
- **Razonamiento que aporta:** diagnóstico de distribuciones, manejo de outliers, estrategias de imputación.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Storytelling with Data | C. Nussbaumer Knaflic | 2015 | 1 | 3 | Media | 5 | 1 |
| P2 | Python Data Science Handbook | J. VanderPlas | 2016 | 2 | 5 | Alta | 4 | 2 |
| P3 | Applied Predictive Modeling | M. Kuhn, K. Johnson | 2013 | 3 | 4 | Media | 5 | 3 |

#### P1 — *Storytelling with Data*
- **Cobertura conceptual:** principios de visualización efectiva, elección de gráficos, diseño de dashboards, narrativa con datos.
- **Cobertura práctica:** transformar tablas y gráficos mediocres en visualizaciones claras y accionables.
- **Valor como guía para el LLM:** vocabulario de comunicación de datos, registro no técnico pero riguroso, complemento de estilo.
- **Conocimiento que aporta:** la capa de comunicación del científico de datos, ausente en los libros técnicos.
- **Vocabulario técnico:** *pre-attentive attributes*, *data-ink ratio*, *chart junk*, *sparkline*, *small multiples*, *gestalt principles*.
- **Razonamiento que aporta:** justificación de elecciones visuales, adaptación de visualizaciones a la audiencia.

#### P2 — *Python Data Science Handbook*
- **Cobertura conceptual:** IPython, NumPy, pandas, Matplotlib, scikit-learn — el stack completo de ciencia de datos en Python.
- **Cobertura práctica:** referencia rápida y notebooks ejecutables para cada herramienta del stack.
- **Valor como guía para el LLM:** cobertura exhaustiva con código ejecutable; disponible completo en GitHub bajo CC BY-NC-ND.
- **Conocimiento que aporta:** el stack técnico concreto que usa el 80 % de los data scientists en la práctica.
- **Vocabulario técnico:** *broadcasting*, *ufunc*, *fancy indexing*, *mask*, *MultiIndex*, *figure*, *axes*, *estimator API*.
- **Razonamiento que aporta:** resolución de problemas con herramientas del stack; patrones idiomáticos de NumPy/pandas.

#### P3 — *Applied Predictive Modeling*
- **Cobertura conceptual:** preprocesamiento, regresión, clasificación, selección de features, evaluación de modelos — con R.
- **Cobertura práctica:** workflow completo de modelado predictivo con ejemplos de datos reales.
- **Valor como guía para el LLM:** perspectiva estadística del ML aplicado; complementa el enfoque Python con rigor estadístico.
- **Conocimiento que aporta:** metodología disciplinada de preprocesamiento y evaluación, fundamental para trabajo en producción.
- **Vocabulario técnico:** *near-zero variance*, *within-fold preprocessing*, *resampling*, *ROC AUC*, *lift curve*, *confusion matrix*.
- **Razonamiento que aporta:** diseño de pipelines de evaluación sin data leakage, selección de métricas por tipo de problema.

## Papers importantes

- Donoho, D. — *50 Years of Data Science* (Journal of Computational and Graphical Statistics, 2017). [DOI:10.1080/10618600.2017.1384734](https://doi.org/10.1080/10618600.2017.1384734)
- Cleveland, W. S. — *Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics* (ISI Review, 2001).
- Wickham, H. — *Tidy Data* (Journal of Statistical Software, 2014). [DOI:10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10)
- Sculley, D. et al. — *Hidden Technical Debt in Machine Learning Systems* (NeurIPS 2015).
- Breck, E. et al. — *The ML Test Score: A Rubric for ML Production Readiness* (BigData 2017).

## Documentación oficial

- [pandas documentation](https://pandas.pydata.org/docs/) — BSD-3, la referencia más usada del dominio.
- [NumPy documentation](https://numpy.org/doc/) — BSD-3.
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html) — PSF-like license.
- [Seaborn documentation](https://seaborn.pydata.org/) — BSD-3.

## Blogs técnicos

- [Towards Data Science (Medium)](https://towardsdatascience.com/) — artículos prácticos del dominio (verificar licencia por artículo).
- [Randy Olson — blog](http://www.randalolson.com/blog/) — visualización y análisis de datos rigurosos.
- [Joel Grus — joelgrus.com](https://joelgrus.com/) — autor de F2; reflexiones sobre ciencia de datos.
- [Eugene Yan — eugeneyan.com](https://eugeneyan.com/) — ML aplicado a producción y sistemas de recomendación.
- [Vicki Boykis — vickiboykis.com](https://vickiboykis.com/) — reflexiones críticas sobre la práctica de ciencia de datos.

## Repositorios GitHub

- [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) — notebooks del libro P2 (CC BY-NC-ND).
- [pandas-dev/pandas](https://github.com/pandas-dev/pandas) — código fuente con docstrings de referencia.
- [numpy/numpy](https://github.com/numpy/numpy) — código fuente con documentación técnica densa.
- [altair-viz/altair](https://github.com/altair-viz/altair) — gramática de gráficos en Python (BSD-3).
- [joelgrus/data-science-from-scratch](https://github.com/joelgrus/data-science-from-scratch) — código del libro F2 (MIT).

## Benchmarks

- **Kaggle competitions** — referencia de facto para ciencia de datos aplicada; leaderboards y kernels públicos.
- **DrivenData** — competencias de datos con impacto social; soluciones públicas documentadas.
- Para evaluar el LLM en este dominio: preguntas de examen de cursos públicos (Data 100 UC Berkeley, CS109 Harvard).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| Kaggle datasets | Varía — verificar por dataset | Descripciones, kernels y discusiones (candidata, no ingerida) |
| DrivenData competitions | Verificar por competencia | Soluciones y reportes públicos de alta calidad |
| FiveThirtyEight data (GitHub) | CC BY 4.0 | Datos periodísticos con análisis narrativos |
| CKAN / datos.gov.co | Abierto — verificar por dataset | Datos gubernamentales Colombia (relevante para Sebastian) |
| Stack Overflow annual survey | ODbL 1.0 | Encuesta anual sobre herramientas y tecnologías |
