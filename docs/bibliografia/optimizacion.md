# Bibliografía — Optimización

> Dominio `optimizacion` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Convex Optimization | S. Boyd, L. Vandenberghe | 2004 | 4 | 5 | Alta | 5 | 5 |
| F2 | Numerical Optimization (2ª ed.) | J. Nocedal, S. J. Wright | 2006 | 5 | 5 | Alta | 5 | 5 |
| F3 | An Introduction to Optimization (4ª ed.) | E. K. P. Chong, S. H. Zak | 2013 | 3 | 4 | Alta | 4 | 4 |

#### F1 — *Convex Optimization*
- **Cobertura conceptual:** conjuntos y funciones convexas, problemas de optimización convexa, dualidad de Lagrange, condiciones KKT, algoritmos (gradient, Newton, interior-point).
- **Cobertura práctica:** formular problemas de ML (regresión, SVM, compresión) como programas convexos; usar CVX/CVXPY.
- **Valor como guía para el LLM:** el texto de referencia en optimización convexa; su notación es ubicua en papers de ML y control.
- **Conocimiento que aporta:** el fundamento teórico de la optimización que subyace al entrenamiento de modelos y al control óptimo.
- **Vocabulario técnico:** *función convexa*, *cono*, *dualidad fuerte*, *condiciones KKT*, *subgradiente*, *programa cuadrático*, *SOCP*, *SDP*.
- **Razonamiento que aporta:** formulación de problemas como programas convexos, verificación de optimalidad con KKT, análisis de sensibilidad dual.

#### F2 — *Numerical Optimization*
- **Cobertura conceptual:** métodos de gradiente, quasi-Newton (BFGS, L-BFGS), gradiente conjugado, trust-region, SQP, optimización sin restricciones y con restricciones.
- **Cobertura práctica:** implementar y elegir optimizadores para ML; entender la base de SGD, Adam y sus variantes.
- **Valor como guía para el LLM:** el texto estándar en optimización numérica; explica en detalle los algoritmos base de los optimizadores de DL.
- **Conocimiento que aporta:** la base numérica de todos los optimizadores de redes neuronales, incluyendo Adam y sus variantes.
- **Vocabulario técnico:** *dirección de descenso*, *línea de búsqueda*, *curvatura*, *BFGS*, *Armijo condition*, *Wolfe conditions*, *convergencia superlineal*.
- **Razonamiento que aporta:** análisis de convergencia de algoritmos iterativos, elección de métodos por costo/precisión.

#### F3 — *An Introduction to Optimization*
- **Cobertura conceptual:** optimización sin restricciones y con restricciones, programación lineal, condiciones de optimalidad, introducción a programación no-lineal.
- **Cobertura práctica:** el texto más accesible del dominio para ingenieros; buen balance entre rigor y aplicabilidad.
- **Valor como guía para el LLM:** nivel introductorio/intermedio que cubre los conceptos base sin la profundidad de Boyd o Nocedal.
- **Conocimiento que aporta:** la base de optimización para ingenieros: gradiente, Lagrange, Hessiano, programación lineal.
- **Vocabulario técnico:** *gradiente*, *hessiano*, *punto estacionario*, *método de multiplicadores de Lagrange*, *programación lineal*, *simplex*, *dualidad*.
- **Razonamiento que aporta:** verificación de condiciones de optimalidad, formulación de problemas de ingeniería como problemas de optimización.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Optimization for Machine Learning | S. Sra, S. Nowozin, S. J. Wright (eds.) | 2011 | 5 | 5 | Alta | 5 | 5 |
| A2 | Introduction to Linear Optimization | D. Bertsimas, J. N. Tsitsiklis | 1997 | 4 | 4 | Media | 5 | 5 |
| A3 | First-Order Methods in Optimization | A. Beck | 2017 | 5 | 5 | Alta | 5 | 5 |

#### A1 — *Optimization for Machine Learning*
- **Cobertura conceptual:** métodos de primer orden para ML, descenso estocástico, métodos en línea, regularización, optimización distribuida.
- **Cobertura práctica:** los fundamentos teóricos de los optimizadores modernos de redes neuronales.
- **Valor como guía para el LLM:** colección de capítulos de expertos; cubre el espacio entre optimización teórica y ML aplicado.
- **Conocimiento que aporta:** la conexión directa entre teoría de optimización y los algoritmos SGD/Adam/Adagrad (el repo entrena con AdamW).
- **Vocabulario técnico:** *regret*, *online learning*, *proximal gradient*, *mirror descent*, *ADMM*, *varianza de gradiente*, *convergencia en expectativa*.
- **Razonamiento que aporta:** análisis de convergencia estocástica, trade-offs entre métodos de primer y segundo orden.

#### A2 — *Introduction to Linear Optimization*
- **Cobertura conceptual:** programación lineal, método simplex, dualidad, análisis de sensibilidad, programación entera, algoritmos de flujo en redes.
- **Cobertura práctica:** formulación y resolución de problemas de optimización lineal; despacho económico de energía es un LP.
- **Valor como guía para el LLM:** el texto estándar de programación lineal con rigor matemático completo.
- **Conocimiento que aporta:** el marco de PL que sustenta el despacho económico, la planificación de expansión y los mercados eléctricos.
- **Vocabulario técnico:** *vértice*, *solución básica factible*, *tableau simplex*, *dual*, *precio sombra*, *cortes de Gomory*, *relajación LP*.
- **Razonamiento que aporta:** formulación de problemas como LP/IP, interpretación de precios duales, análisis de sensibilidad.

#### A3 — *First-Order Methods in Optimization*
- **Cobertura conceptual:** descenso de gradiente, descenso de subgradiente, métodos proximales, métodos acelerados (Nesterov), splitting methods.
- **Cobertura práctica:** los fundamentos de los optimizadores modernos de DL desde la perspectiva teórica más rigurosa.
- **Valor como guía para el LLM:** texto monográfico sobre métodos de primer orden — la familia de algoritmos usada en el entrenamiento de LLMs.
- **Conocimiento que aporta:** la teoría rigurosa detrás del gradient descent y sus variantes, incluyendo las tasas de convergencia.
- **Vocabulario técnico:** *operador proximal*, *suavizado de Moreau*, *L-smoothness*, *fuertemente convexo*, *método de Nesterov*, *tasa de convergencia O(1/k²)*.
- **Razonamiento que aporta:** pruebas de convergencia de gradient descent, diseño de algoritmos de optimización eficientes.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Convex Optimization: Algorithms and Complexity | S. Bubeck | 2015 | 5 | 4 | Media | 5 | 5 |
| P2 | Engineering Optimization: Theory and Practice (4ª ed.) | S. S. Rao | 2009 | 3 | 4 | Media | 4 | 4 |
| P3 | Algorithms for Optimization | M. J. Kochenderfer, T. A. Wheeler | 2019 | 3 | 5 | Alta | 5 | 4 |

#### P1 — *Convex Optimization: Algorithms and Complexity*
- **Cobertura conceptual:** descenso de gradiente, método del punto interior, algoritmos estocásticos — con cotas de complejidad.
- **Cobertura práctica:** entender por qué SGD escala y cuándo los métodos de segundo orden son preferibles.
- **Valor como guía para el LLM:** monografía rigurosa disponible libremente (arXiv); complementa Boyd con perspectiva algorítmica y de complejidad.
- **Conocimiento que aporta:** las cotas de complejidad computacional de los optimizadores — crucial para elegir algoritmos a escala.
- **Vocabulario técnico:** *complejidad de oráculo*, *lower bounds*, *aceleración de Nesterov*, *optimización estocástica*, *variance reduction*.
- **Razonamiento que aporta:** análisis de complejidad, pruebas de optimalidad de algoritmos, razonamiento sobre escalabilidad.

#### P2 — *Engineering Optimization*
- **Cobertura conceptual:** optimización no-lineal, métodos genéticos, enjambre de partículas, programación dinámica — perspectiva de ingeniería.
- **Cobertura práctica:** aplicar optimización a problemas de ingeniería mecánica, eléctrica y civil.
- **Valor como guía para el LLM:** perspectiva de ingeniería de la optimización; vocabulario de metaheurísticas y optimización aplicada.
- **Conocimiento que aporta:** la capa de heurísticas y optimización evolutiva usada en problemas de ingeniería no convexos.
- **Vocabulario técnico:** *algoritmo genético*, *función de aptitud*, *operador de cruce*, *PSO*, *recocido simulado*, *programación dinámica estocástica*.
- **Razonamiento que aporta:** formulación de problemas de ingeniería como problemas de optimización, comparación de heurísticas.

#### P3 — *Algorithms for Optimization*
- **Cobertura conceptual:** descenso de gradiente, momentum, Adam, métodos de segundo orden, evolución, optimización bayesiana — con código Julia.
- **Cobertura práctica:** implementación de algoritmos de optimización desde cero; el más completo en cobertura de métodos modernos.
- **Valor como guía para el LLM:** el único texto que cubre tanto clásicos como Adam y optimización bayesiana con código.
- **Conocimiento que aporta:** el espectro completo de algoritmos de optimización relevantes para ML, con implementaciones.
- **Vocabulario técnico:** *momentum*, *Adam*, *optimización bayesiana*, *acquisition function*, *ES (evolution strategies)*, *Gaussian process surrogate*.
- **Razonamiento que aporta:** elección de algoritmo por tipo de problema, análisis de paisajes de pérdida, HPO.

## Papers importantes

- Kingma, D. & Ba, J. — *Adam: A Method for Stochastic Optimization* (ICLR 2015). [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)
- Duchi, J., Hazan, E., Singer, Y. — *Adaptive Subgradient Methods for Online Learning* (JMLR 2011). [JMLR link](https://jmlr.org/papers/v12/duchi11a.html)
- Nesterov, Y. — *A Method for Solving the Convex Programming Problem with Convergence Rate O(1/k²)* (Soviet Math. Dokl., 1983).
- Loshchilov, I. & Hutter, F. — *Decoupled Weight Decay Regularization* (AdamW, ICLR 2019). [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)
- Dauphin, Y. et al. — *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization* (NeurIPS 2014). [arXiv:1406.2572](https://arxiv.org/abs/1406.2572)
- Liu, L. et al. — *On the Variance of the Adaptive Learning Rate and Beyond* (RAdam, ICLR 2020). [arXiv:1908.03265](https://arxiv.org/abs/1908.03265)

## Documentación oficial

- [CVXPY documentation](https://www.cvxpy.org/) — Apache-2.0; modelado de optimización convexa en Python.
- [SciPy optimize module](https://docs.scipy.org/doc/scipy/reference/optimize.html) — BSD-3.
- [Optuna documentation](https://optuna.readthedocs.io/) — MIT; optimización de hiperparámetros.
- [PyTorch Optim documentation](https://pytorch.org/docs/stable/optim.html) — BSD-3; referencia de optimizadores en DL.

## Blogs técnicos

- [Sebastian Ruder — An Overview of Gradient Descent Optimization Algorithms](https://www.ruder.io/optimizing-gradient-descent/) — referencia clásica y citada.
- [Distill.pub — Why Momentum Really Works](https://distill.pub/2017/momentum/) — visualización interactiva (CC BY).
- [Francis Bach — blog](https://francisbach.com/) — optimización convexa y estadística avanzada.
- [Ben Recht — arg min blog](http://www.argmin.net/) — optimización en ML, ML y control.

## Repositorios GitHub

- [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) — modelado de optimización convexa (Apache-2.0).
- [optuna-org/optuna](https://github.com/optuna-org/optuna) — HPO con optimización bayesiana (MIT).
- [google-deepmind/optax](https://github.com/google-deepmind/optax) — optimizadores para JAX/DL (Apache-2.0).
- [scipy/scipy optimize](https://github.com/scipy/scipy) — solucionadores numéricos (BSD-3).
- [maziarraissi/PINNs](https://github.com/maziarraissi/PINNs) — optimización para física (MIT).

## Benchmarks

- **CUTEst** — suite estándar de funciones de prueba para optimización no-lineal.
- **NEOS Server Benchmark** — problemas de optimización de referencia.
- Para ML: **HPO benchmark** (HPOBench) — benchmark de optimización de hiperparámetros.
- Para energía: **OPF benchmark cases** (IEEE 14/30/118-bus) — flujo de potencia óptimo.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| CUTEst test problems | LGPL-3 | Funciones de prueba estándar para optimización |
| MIPLIB | Verificar por instancia | Instancias de programación entera mixta |
| QPLIB | Verificar por instancia | Instancias de programación cuadrática |
| HPOBench datasets | Apache-2.0 | Benchmarks de HPO con curvas de aprendizaje |
| PGLIB-OPF | CC BY 4.0 | Casos de flujo de potencia óptimo para sistemas eléctricos |
