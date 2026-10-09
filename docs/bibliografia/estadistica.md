# Bibliografía — Estadística

> Dominio `estadistica` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Statistical Inference (2ª ed.) | G. Casella, R. L. Berger | 2002 | 5 | 5 | Alta | 5 | 5 |
| F2 | All of Statistics: A Concise Course in Statistical Inference | L. Wasserman | 2004 | 4 | 5 | Alta | 5 | 4 |
| F3 | Introduction to Probability (2ª ed.) | D. P. Bertsekas, J. N. Tsitsiklis | 2008 | 3 | 5 | Alta | 5 | 4 |

#### F1 — *Statistical Inference*
- **Cobertura conceptual:** probabilidad, variables aleatorias, familias exponenciales, estimación puntual, tests de hipótesis, regresión, análisis bayesiano.
- **Cobertura práctica:** derivar estimadores, realizar tests estadísticos rigurosos, entender propiedades asintóticas.
- **Valor como guía para el LLM:** el texto de inferencia estadística más riguroso a nivel de maestría; notación canónica del campo.
- **Conocimiento que aporta:** la inferencia estadística formal que fundamenta todo el análisis de datos y ML probabilístico.
- **Vocabulario técnico:** *UMVUE*, *Cramér-Rao*, *suficiencia*, *completitud*, *prueba UMP*, *razón de verosimilitud*, *bootstrap paramétrico*.
- **Razonamiento que aporta:** derivación de estimadores óptimos, construcción de tests estadísticos, análisis de propiedades de estimadores.

#### F2 — *All of Statistics*
- **Cobertura conceptual:** probabilidad, distribuciones, estimación, hipótesis, modelos lineales, bootstrap, no-paramétrico, selección de modelos, causalidad.
- **Cobertura práctica:** visión unificada de estadística para ciencia de datos; más accesible que Casella-Berger con resultados completos.
- **Valor como guía para el LLM:** el mejor balance entre rigor y amplitud; cubre la estadística que necesita un científico de datos o investigador de ML.
- **Conocimiento que aporta:** el puente explícito entre estadística clásica y las herramientas modernas de ciencia de datos.
- **Vocabulario técnico:** *intervalos de confianza*, *p-value*, *potencia*, *FDR*, *estimador kernel*, *selección de modelos*, *BIC/AIC*.
- **Razonamiento que aporta:** razonamiento estadístico completo: diseño, estimación, inferencia y diagnóstico.

#### F3 — *Introduction to Probability*
- **Cobertura conceptual:** modelos de probabilidad, variables aleatorias, esperanza, cadenas de Markov, inferencia bayesiana básica.
- **Cobertura práctica:** el texto de probabilidad más pedagógico para ML; muy usado en cursos de ML de MIT y otros.
- **Valor como guía para el LLM:** texto claro y bien estructurado con muchos ejemplos; aporta el registro pedagógico del dominio probabilístico.
- **Conocimiento que aporta:** los fundamentos de probabilidad que subyacen a todo modelo estadístico y generativo.
- **Vocabulario técnico:** *espacio muestral*, *regla de Bayes*, *independencia condicional*, *función generatriz de momentos*, *ley de los grandes números*, *TCL*.
- **Razonamiento que aporta:** modelado probabilístico, cálculo de probabilidades condicionales, análisis de convergencia estocástica.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Bayesian Data Analysis (3ª ed.) | A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, D. B. Rubin | 2013 | 5 | 5 | Alta | 5 | 5 |
| A2 | The Elements of Statistical Learning (2ª ed.) | T. Hastie, R. Tibshirani, J. Friedman | 2009 | 4 | 5 | Alta | 5 | 5 |
| A3 | Time Series Analysis: Forecasting and Control (5ª ed.) | G. E. P. Box, G. M. Jenkins, G. C. Reinsel, G. M. Ljung | 2015 | 4 | 5 | Alta | 5 | 5 |

#### A1 — *Bayesian Data Analysis*
- **Cobertura conceptual:** inferencia bayesiana completa: modelos jerárquicos, MCMC, evaluación de modelos, regresión bayesiana, modelos generativos.
- **Cobertura práctica:** ajustar modelos bayesianos reales con Stan/PyMC; diagnósticos MCMC, comparación de modelos.
- **Valor como guía para el LLM:** el texto definitivo de estadística bayesiana; notación y vocabulario usado en papers de ML probabilístico.
- **Conocimiento que aporta:** el marco bayesiano completo que subyace a modelos generativos, variational inference y aprendizaje probabilístico.
- **Vocabulario técnico:** *prior*, *posterior*, *predictive distribution*, *MCMC*, *Hamiltonian Monte Carlo*, *WAIC*, *LOO-CV*, *shrinkage*.
- **Razonamiento que aporta:** razonamiento bayesiano completo, diagnóstico de cadenas MCMC, selección y comparación de modelos.

#### A2 — *The Elements of Statistical Learning*
- **Cobertura conceptual:** regresión regularizada, árboles, boosting, random forests, SVM, métodos aditivos, selección de modelos.
- **Cobertura práctica:** comprensión profunda de los métodos de ML desde perspectiva estadística.
- **Valor como guía para el LLM:** el texto que conecta estadística y ML más profundamente; referencia cruzada con `machine_learning`.
- **Conocimiento que aporta:** la visión estadística rigurosa de los algoritmos de ML que justifica su funcionamiento teórico.
- **Vocabulario técnico:** *shrinkage*, *degrees of freedom efectivos*, *ANOVA funcional*, *gradient boosting*, *kernel smoothing*, *additive models*.
- **Razonamiento que aporta:** análisis de sesgo-varianza, selección de hiperparámetros con fundamento estadístico.

#### A3 — *Time Series Analysis*
- **Cobertura conceptual:** modelos ARIMA, procesos estacionarios, identificación y estimación, forecasting, intervención, modelos de transferencia.
- **Cobertura práctica:** ajustar modelos ARIMA a series reales; forecasting de demanda energética — directamente relevante para Sebastian.
- **Valor como guía para el LLM:** el texto canónico de series temporales; vocabulario de pronóstico de series temporales muy relevante en energía.
- **Conocimiento que aporta:** el marco estadístico clásico de pronóstico que complementa los métodos de DL para series temporales.
- **Vocabulario técnico:** *autocorrelación*, *estacionariedad*, *diferenciación*, *ARIMA(p,d,q)*, *ACF/PACF*, *raíz unitaria*, *pronóstico de intervalo*.
- **Razonamiento que aporta:** identificación de modelos con ACF/PACF, diagnóstico de residuos, evaluación de pronósticos.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Naked Statistics | C. Wheelan | 2013 | 1 | 3 | Baja | 4 | 1 |
| P2 | Regression and Other Stories | A. Gelman, J. Hill, A. Vehtari | 2020 | 3 | 5 | Alta | 5 | 3 |
| P3 | Statistical Rethinking (2ª ed.) | R. McElreath | 2020 | 4 | 5 | Alta | 5 | 3 |

#### P1 — *Naked Statistics*
- **Cobertura conceptual:** probabilidad, regresión, test de hipótesis, correlación — explicados sin fórmulas para un público amplio.
- **Cobertura práctica:** comunicar resultados estadísticos a no estadísticos; detectar falacias estadísticas comunes.
- **Valor como guía para el LLM:** registro de divulgación estadística; guía de texto accesible sobre conceptos estadísticos.
- **Conocimiento que aporta:** la capa comunicativa de la estadística; errores comunes de interpretación que un LLM debe reconocer.
- **Vocabulario técnico:** *correlación vs. causalidad*, *sesgo de selección*, *regresión a la media*, *muestra representativa*, *error estándar*.
- **Razonamiento que aporta:** razonamiento crítico sobre afirmaciones estadísticas, identificación de errores comunes.

#### P2 — *Regression and Other Stories*
- **Cobertura conceptual:** regresión lineal y logística, inferencia causal, validación, predicción — con enfoque bayesiano aplicado.
- **Cobertura práctica:** aplicar regresión de forma rigurosa a datos reales; diseño de estudios observacionales.
- **Valor como guía para el LLM:** el mejor texto práctico de regresión moderna con perspectiva causal; prosa directa y ejemplos reales.
- **Conocimiento que aporta:** la regresión aplicada rigurosa con diagnósticos, validación y perspectiva causal.
- **Vocabulario técnico:** *coeficiente de regresión*, *interacción*, *predicción posterior*, *extrapolación*, *estimación de efectos causales*, *controles*.
- **Razonamiento que aporta:** interpretación de coeficientes de regresión, diagnóstico de supuestos, análisis de sensibilidad.

#### P3 — *Statistical Rethinking*
- **Cobertura conceptual:** estadística bayesiana aplicada: modelos lineales/multinivel, modelos causales (DAGs), MCMC con Stan/brms.
- **Cobertura práctica:** construir y ajustar modelos bayesianos paso a paso con código R/Python; pensar causalmente.
- **Valor como guía para el LLM:** el mejor texto para aprender a pensar como bayesiano; combina teoría, código y razonamiento causal.
- **Conocimiento que aporta:** el marco bayesiano práctico conectado con causalidad — puente entre estadística y ML moderno.
- **Vocabulario técnico:** *DAG*, *backdoor criterion*, *confounders*, *mediation*, *multilevel model*, *MCMC*, *posterior predictive check*.
- **Razonamiento que aporta:** razonamiento causal estructurado, diseño de modelos jerárquicos, evaluación de supuestos.

## Papers importantes

- Efron, B. & Hastie, T. — *Computer Age Statistical Inference* (Cambridge, 2016 — disponible online).
- Benjamini, Y. & Hochberg, Y. — *Controlling the False Discovery Rate* (JRSS-B, 1995). [DOI:10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)
- Gelman, A. & Loken, E. — *The Statistical Crisis in Science* (American Scientist, 2014).
- Ioannidis, J. P. A. — *Why Most Published Research Findings Are False* (PLoS Medicine, 2005). [DOI:10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124)
- Rubin, D. B. — *Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies* (Journal of Educational Psychology, 1974).

## Documentación oficial

- [statsmodels documentation](https://www.statsmodels.org/stable/index.html) — BSD-3; modelos estadísticos en Python.
- [SciPy stats module](https://docs.scipy.org/doc/scipy/reference/stats.html) — BSD-3; pruebas estadísticas.
- [PyMC documentation](https://www.pymc.io/welcome.html) — Apache-2.0; estadística bayesiana en Python.
- [Stan documentation](https://mc-stan.org/docs/) — código BSD-3, documentación: verificar licencia; lenguaje probabilístico de referencia.

## Blogs técnicos

- [Statistical Modeling, Causal Inference, and Social Science (A. Gelman)](https://statmodeling.stat.columbia.edu/) — reflexiones diarias del co-autor de BDA.
- [Simply Statistics (R. Irizarry, J. Leek, R. Peng)](https://simplystatistics.org/) — estadística moderna y ciencia de datos.
- [Cross Validated — stats.stackexchange.com](https://stats.stackexchange.com/) — preguntas y respuestas estadísticas (CC BY-SA 4.0).
- [Michael Betancourt — blog](https://betanalpha.github.io/writing/) — estadística bayesiana y HMC en profundidad.
- [Andrew Gelman — Statistical Graphics](https://andrewgelman.com/) — visualización y estadística aplicada.

## Repositorios GitHub

- [pymc-devs/pymc](https://github.com/pymc-devs/pymc) — estadística bayesiana (Apache-2.0).
- [arviz-devs/arviz](https://github.com/arviz-devs/arviz) — análisis y diagnóstico bayesiano (Apache-2.0).
- [stan-dev/stan](https://github.com/stan-dev/stan) — lenguaje probabilístico (BSD-3).
- [probml/pyprobml](https://github.com/probml/pyprobml) — notebooks de Murphy que cubren estadística y ML probabilístico.

## Benchmarks

- **MMLU** (subject `high_school_statistics`) — preguntas de estadística y probabilidad.
- **Competition math** — sección de probabilidad y estadística combinatoria.
- Para evaluar el LLM: exámenes de estadística de MIT OpenCourseWare (18.650), problemas de AP Statistics.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| Cross Validated (stats.SE) dump | CC BY-SA 4.0 | Q&A de estadística con respuestas expertas |
| R datasets (built-in) | GPL-2 | Datasets clásicos de estadística: mtcars, iris, etc. |
| ISLR datasets | Verificar licencia | Datasets del libro ISLR (James et al.) |
| UCI ML Repository — estadística | CC BY 4.0 (mayoría) | Datasets clásicos con documentación estadística |
| NIST Statistics datasets | Dominio público (US Gov) | Datos de referencia con soluciones estadísticas verificadas |
