# Bibliografía — Machine Learning

> Dominio `machine_learning` · peso 1.2 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Pattern Recognition and Machine Learning | C. M. Bishop | 2006 | 4 | 5 | Alta | 5 | 5 |
| F2 | The Elements of Statistical Learning (2ª ed.) | T. Hastie, R. Tibshirani, J. Friedman | 2009 | 4 | 5 | Alta | 5 | 5 |
| F3 | An Introduction to Statistical Learning (2ª ed., versión Python 2023) | G. James, D. Witten, T. Hastie, R. Tibshirani (+ J. Taylor en la ed. Python) | 2021 | 2 | 4 | Alta | 5 | 3 |

#### F1 — *Pattern Recognition and Machine Learning*
- **Cobertura conceptual:** inferencia bayesiana, modelos lineales, kernels, SVM, modelos gráficos, EM, variational inference, mixturas.
- **Cobertura práctica:** derivar y justificar la elección de modelos probabilísticos; implementar EM y regresión bayesiana desde las ecuaciones.
- **Valor como guía para el LLM:** prosa matemática densa y consistente, ideal para que el modelo aprenda el patrón "definición → derivación → interpretación".
- **Conocimiento que aporta:** el núcleo probabilístico del ML clásico que sustenta el vocabulario de todo el dominio.
- **Vocabulario técnico:** *posterior*, *likelihood*, *prior conjugado*, *kernel trick*, *margen*, *evidencia*, *latent variable*, *responsabilidades (EM)*.
- **Razonamiento que aporta:** derivaciones paso a paso, maximización de verosimilitud, argumentos de convexidad y trade-off sesgo-varianza.

#### F2 — *The Elements of Statistical Learning*
- **Cobertura conceptual:** regresión regularizada (ridge/lasso), árboles, boosting, random forests, métodos aditivos, selección de modelos.
- **Cobertura práctica:** elegir y ajustar modelos tabulares con criterio estadístico; diagnosticar overfitting con teoría real.
- **Valor como guía para el LLM:** combina ecuaciones, algoritmos en pseudocódigo y discusión comparativa — tres registros textuales valiosos.
- **Conocimiento que aporta:** el puente estadística ↔ ML; la visión "frecuentista" que complementa a Bishop.
- **Vocabulario técnico:** *shrinkage*, *degrees of freedom*, *bagging*, *gradient boosting*, *curse of dimensionality*, *cross-validation*.
- **Razonamiento que aporta:** comparación rigurosa de métodos, análisis de error de generalización, trade-offs sesgo-varianza-cómputo.

#### F3 — *An Introduction to Statistical Learning*
- **Cobertura conceptual:** versión accesible de ESL: regresión, clasificación, resampling, árboles, SVM, deep learning introductorio.
- **Cobertura práctica:** labs completos en Python/R reproducibles de punta a punta.
- **Valor como guía para el LLM:** texto introductorio con código intercalado — enseña el registro "explicación pedagógica + snippet".
- **Conocimiento que aporta:** guía para el nivel `introductorio` del esquema de dificultad.
- **Vocabulario técnico:** *training/test error*, *bootstrap*, *validation set*, *ROC*, *odds*, *interaction term*.
- **Razonamiento que aporta:** interpretación de resultados y diagnósticos; cómo justificar decisiones de modelado simples.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Probabilistic Machine Learning: An Introduction | K. P. Murphy | 2022 | 4 | 5 | Alta | 5 | 5 |
| A2 | Understanding Machine Learning: From Theory to Algorithms | S. Shalev-Shwartz, S. Ben-David | 2014 | 5 | 4 | Media | 5 | 5 |
| A3 | Foundations of Machine Learning (2ª ed.) | M. Mohri, A. Rostamizadeh, A. Talwalkar | 2018 | 5 | 3 | Media | 5 | 5 |

#### A1 — *Probabilistic Machine Learning: An Introduction*
- **Cobertura conceptual:** actualización moderna de Bishop: deep learning, transformers introductorios, inferencia variacional, decisión bayesiana.
- **Cobertura práctica:** notebooks JAX/Python públicos (probml) que acompañan cada capítulo.
- **Valor como guía para el LLM:** notación unificada y moderna; conecta ML clásico con deep learning con el vocabulario actual del campo.
- **Conocimiento que aporta:** estado del arte 2022 del ML probabilístico, el complemento contemporáneo de F1/F2.
- **Vocabulario técnico:** *ELBO*, *reparameterization trick*, *exponential family*, *calibration*, *conformal prediction*.
- **Razonamiento que aporta:** derivación de objetivos de entrenamiento (ELBO, NLL) y conexión entre familias de modelos.

#### A2 — *Understanding Machine Learning*
- **Cobertura conceptual:** teoría del aprendizaje: PAC, dimensión VC, complejidad de Rademacher, convex learning, boosting teórico.
- **Cobertura práctica:** demostrar cotas de generalización y entender cuándo un algoritmo puede aprender.
- **Valor como guía para el LLM:** texto teorema-demostración, escaso en la web; enseña estructura lógica formal.
- **Conocimiento que aporta:** los fundamentos teóricos que casi ningún blog cubre — temas poco cubiertos por las fuentes web del corpus.
- **Vocabulario técnico:** *PAC-learnable*, *VC dimension*, *Rademacher complexity*, *uniform convergence*, *agnostic learning*.
- **Razonamiento que aporta:** demostraciones formales, argumentos de cotas, contraejemplos (no-free-lunch).

#### A3 — *Foundations of Machine Learning*
- **Cobertura conceptual:** teoría de generalización, kernels, ranking, on-line learning, aprendizaje por refuerzo teórico.
- **Cobertura práctica:** análisis formal de algoritmos concretos (AdaBoost, SVM, perceptron).
- **Valor como guía para el LLM:** segundo registro teórico con notación distinta a A2 — robustece la generalización del modelo entre notaciones.
- **Conocimiento que aporta:** ranking y on-line learning, ausentes en los otros ocho libros.
- **Vocabulario técnico:** *regret*, *mistake bound*, *margin theory*, *stability*, *Rademacher averages*.
- **Razonamiento que aporta:** análisis de algoritmos con garantías; razonamiento adversarial (on-line learning).

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3ª ed.) | A. Géron | 2022 | 2 | 5 | Alta | 5 | 2 |
| P2 | The Hundred-Page Machine Learning Book | A. Burkov | 2019 | 2 | 3 | Media | 4 | 3 |
| P3 | Designing Machine Learning Systems | C. Huyen | 2022 | 3 | 4 | Alta | 5 | 1 |

#### P1 — *Hands-On Machine Learning*
- **Cobertura conceptual:** pipeline completo de ML: preprocesamiento, modelos sklearn, redes con Keras, tuning, despliegue básico.
- **Cobertura práctica:** construir proyectos ML end-to-end reales; el libro práctico de referencia del campo.
- **Valor como guía para el LLM:** la mayor densidad de pares "explicación + código Python idiomático" del dominio.
- **Conocimiento que aporta:** el flujo de trabajo real de un ML engineer, no solo los modelos.
- **Vocabulario técnico:** *pipeline*, *ColumnTransformer*, *grid search*, *early stopping*, *feature scaling*, *stratified split*.
- **Razonamiento que aporta:** debugging de modelos, decisiones de preprocesamiento, lectura de curvas de aprendizaje.

#### P2 — *The Hundred-Page Machine Learning Book*
- **Cobertura conceptual:** panorama condensado de todo el ML supervisado/no supervisado en notación mínima.
- **Cobertura práctica:** referencia rápida para repasar definiciones y elegir algoritmos.
- **Valor como guía para el LLM:** texto de alta densidad conceptual por token — buena guía del vocabulario base.
- **Conocimiento que aporta:** resúmenes "canónicos" de cada técnica, útiles como referencia de temas para documentos `summary`.
- **Vocabulario técnico:** todo el glosario base del dominio en 100 páginas.
- **Razonamiento que aporta:** síntesis y comparación rápida entre algoritmos.

#### P3 — *Designing Machine Learning Systems*
- **Cobertura conceptual:** ML en producción: data drift, feature stores, monitoreo, reentrenamiento, diseño de sistemas.
- **Cobertura práctica:** diseñar la arquitectura de un sistema ML real (muy alineado al trabajo de Sebastian en energía).
- **Valor como guía para el LLM:** prosa de ingeniería de sistemas con vocabulario MLOps, registro distinto al académico.
- **Conocimiento que aporta:** la capa de producción que los libros teóricos omiten.
- **Vocabulario técnico:** *data drift*, *feature store*, *online prediction*, *shadow deployment*, *training-serving skew*.
- **Razonamiento que aporta:** trade-offs de diseño (latencia vs. frescura, batch vs. streaming), análisis de fallos en producción.

## Papers importantes

- Breiman, L. — *Random Forests* (Machine Learning, 2001). [DOI:10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)
- Breiman, L. — *Statistical Modeling: The Two Cultures* (Statistical Science, 2001). [DOI:10.1214/ss/1009213726](https://doi.org/10.1214/ss/1009213726)
- Chen, T. & Guestrin, C. — *XGBoost: A Scalable Tree Boosting System* (KDD 2016). [arXiv:1603.02754](https://arxiv.org/abs/1603.02754)
- Ke, G. et al. — *LightGBM: A Highly Efficient Gradient Boosting Decision Tree* (NeurIPS 2017).
- Pedregosa, F. et al. — *Scikit-learn: Machine Learning in Python* (JMLR 2011). [arXiv:1201.0490](https://arxiv.org/abs/1201.0490)
- Domingos, P. — *A Few Useful Things to Know About Machine Learning* (CACM 2012). [DOI:10.1145/2347736.2347755](https://doi.org/10.1145/2347736.2347755)
- Sculley, D. et al. — *Hidden Technical Debt in Machine Learning Systems* (NeurIPS 2015).

## Documentación oficial

- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — BSD-3, la mejor documentación pedagógica del dominio.
- [XGBoost docs](https://xgboost.readthedocs.io/) — Apache-2.0.
- [LightGBM docs](https://lightgbm.readthedocs.io/) — MIT.

## Blogs técnicos

- [Distill.pub](https://distill.pub/) — visualizaciones interactivas de conceptos ML (CC BY).
- [Sebastian Raschka — Ahead of AI / blog](https://sebastianraschka.com/blog/) — ML/DL riguroso con código.
- [Chip Huyen blog](https://huyenchip.com/blog/) — ML en producción.
- [Machine Learning Mastery (J. Brownlee)](https://machinelearningmastery.com/) — tutoriales prácticos paso a paso.
- [Google Research Blog](https://research.google/blog/) — resultados aplicados.

## Repositorios GitHub

- [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) — código + docstrings de calidad excepcional.
- [ageron/handson-ml3](https://github.com/ageron/handson-ml3) — notebooks del libro P1.
- [dmlc/xgboost](https://github.com/dmlc/xgboost) y [microsoft/LightGBM](https://github.com/microsoft/LightGBM) — boosting de referencia.
- [rasbt/machine-learning-book](https://github.com/rasbt/machine-learning-book) — código del libro de Raschka (PyTorch).
- [probml/pyprobml](https://github.com/probml/pyprobml) — notebooks de Murphy (A1).

## Benchmarks

- **OpenML-CC18** — suite curada de 72 tareas de clasificación tabular.
- **Repositorio UCI** — el conjunto de referencia histórico para ML tabular.
- Para evaluar el LLM en este dominio: subconjuntos de **MMLU** (machine learning) y preguntas estilo examen de cursos públicos (CS229).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| UCI ML Repository | CC BY 4.0 (mayoría; verificar por dataset) | Texto descriptivo de cada dataset también es útil como documento |
| OpenML | CC (metadatos); datasets varían | API programática |
| Kaggle datasets/competitions | Varía por dataset — verificar licencia | Kernels públicos = fuente de código comentado |
| CS229/CS4780 notes (Stanford/Cornell) | Verificar licencia (uso académico) | Apuntes de curso de alta calidad |
| Cross Validated (stats.stackexchange) dump | CC BY-SA 4.0 | Q&A de ML con derivaciones |
