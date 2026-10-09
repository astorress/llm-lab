# Bibliografía — Matemáticas

> Dominio `matematicas` · peso 1.2 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Introduction to Linear Algebra (5ª ed.) | G. Strang | 2016 | 3 | 5 | Alta | 5 | 4 |
| F2 | Calculus (8ª ed.) | J. Stewart | 2015 | 2 | 4 | Alta | 5 | 3 |
| F3 | Linear Algebra Done Right (3ª ed.) | S. Axler | 2015 | 4 | 5 | Alta | 5 | 4 |

#### F1 — *Introduction to Linear Algebra*
- **Cobertura conceptual:** espacios vectoriales, transformaciones lineales, autovalores y autovectores, SVD, mínimos cuadrados, aplicaciones.
- **Cobertura práctica:** resolver sistemas, calcular SVD, analizar datos con PCA — la base computacional del ML.
- **Valor como guía para el LLM:** el texto de álgebra lineal más referenciado en ML; notación directamente usada en papers y libros de DL.
- **Conocimiento que aporta:** el álgebra lineal completa que usa todo el stack de ML/DL: desde regresión hasta attention.
- **Vocabulario técnico:** *espacio columna*, *espacio nulo*, *proyección*, *ortogonalización*, *descomposición SVD*, *PCA*, *pseudoinversa*.
- **Razonamiento que aporta:** razonamiento geométrico sobre transformaciones, interpretación de autovalores, análisis de rango.

#### F2 — *Calculus* (Stewart)
- **Cobertura conceptual:** límites, derivadas, integrales, series, cálculo multivariable, ecuaciones diferenciales básicas.
- **Cobertura práctica:** cálculo de gradientes, regla de la cadena, integrales de probabilidad — base matemática del entrenamiento de redes.
- **Valor como guía para el LLM:** el texto de cálculo más usado en ingeniería en América Latina; muchos ejemplos resueltos.
- **Conocimiento que aporta:** el cálculo que subyace a backpropagation, optimización y teoría de probabilidad continua.
- **Vocabulario técnico:** *derivada parcial*, *regla de la cadena*, *gradiente*, *hessiano*, *serie de Taylor*, *límite*, *continuidad*.
- **Razonamiento que aporta:** diferenciación de funciones compuestas, optimización por derivadas, análisis de convergencia de series.

#### F3 — *Linear Algebra Done Right*
- **Cobertura conceptual:** álgebra lineal abstracta desde subespacios hasta operadores: espectro, formas bilineales, operadores normales.
- **Cobertura práctica:** demostrar propiedades de transformaciones lineales; base para entender los fundamentos de redes neuronales.
- **Valor como guía para el LLM:** texto teórico formal — aporta el registro matemático riguroso de definición-lema-teorema-prueba.
- **Conocimiento que aporta:** el fundamento algebraico abstracto que justifica las propiedades de las operaciones matriciales usadas en DL.
- **Vocabulario técnico:** *espacio vectorial*, *transformación lineal*, *operador adjunto*, *operador normal*, *forma de Jordan*, *producto interno*.
- **Razonamiento que aporta:** pruebas formales, razonamiento abstracto sin coordenadas, generalización de conceptos concretos.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Mathematics for Machine Learning | M. P. Deisenroth, A. A. Faisal, C. S. Ong | 2020 | 4 | 5 | Alta | 5 | 5 |
| A2 | Principles of Mathematical Analysis (3ª ed.) | W. Rudin ("Baby Rudin") | 1976 | 5 | 3 | Baja | 5 | 5 |
| A3 | Numerical Analysis (10ª ed.) | R. L. Burden, J. D. Faires | 2015 | 4 | 4 | Media | 5 | 4 |

#### A1 — *Mathematics for Machine Learning*
- **Cobertura conceptual:** álgebra lineal, cálculo multivariable, probabilidad y estadística, optimización — todo orientado a ML con ejemplos directos.
- **Cobertura práctica:** derivar las matemáticas detrás de regresión, PCA, SVM, redes neuronales — disponible gratis en PDF.
- **Valor como guía para el LLM:** el puente explícito entre matemáticas abstractas y ML; notación unificada con los libros de DL.
- **Conocimiento que aporta:** la conexión directa entre conceptos matemáticos y algoritmos ML que los textos tradicionales no hacen.
- **Vocabulario técnico:** *Jacobiano*, *Hessiano*, *descenso de gradiente*, *cadena de Markov*, *kernel*, *función objetivo*, *verosimilitud*.
- **Razonamiento que aporta:** derivación de algoritmos desde primeros principios matemáticos; conexión conceptual entre subdisciplinas.

#### A2 — *Principles of Mathematical Analysis* (Rudin)
- **Cobertura conceptual:** sucesiones y series, topología métrica, continuidad, diferenciación, integración de Riemann-Stieltjes, funciones de varias variables.
- **Cobertura práctica:** base rigurosa de análisis real; fundamento de la teoría de probabilidad y optimización.
- **Valor como guía para el LLM:** texto matemático de máximo rigor; referencia del estilo teorema-demostración más exigente.
- **Conocimiento que aporta:** los fundamentos de análisis real que justifican la convergencia de algoritmos y resultados de probabilidad.
- **Vocabulario técnico:** *norma*, *compacidad*, *completitud*, *espacio de Banach*, *uniforme continuidad*, *diferenciabilidad*, *serie de Cauchy*.
- **Razonamiento que aporta:** pruebas épsilon-delta, razonamiento topológico, demostraciones de convergencia.

#### A3 — *Numerical Analysis*
- **Cobertura conceptual:** solución de ecuaciones, interpolación, integración numérica, ecuaciones diferenciales, álgebra lineal numérica.
- **Cobertura práctica:** implementar algoritmos numéricos; entender errores de redondeo y estabilidad numérica — crítico en entrenamiento de redes.
- **Valor como guía para el LLM:** el puente entre matemáticas analíticas y cómputo; vocabulario de métodos numéricos del campo.
- **Conocimiento que aporta:** los fundamentos de los solucionadores numéricos usados en optimización y simulación.
- **Vocabulario técnico:** *error de truncamiento*, *estabilidad numérica*, *condicionamiento*, *número de condición*, *pivoteo*, *Runge-Kutta*, *iteración de punto fijo*.
- **Razonamiento que aporta:** análisis de errores, elección de métodos por estabilidad/precisión/costo, análisis de convergencia numérica.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Linear Algebra and Its Applications (5ª ed.) | D. C. Lay, S. R. Lay, J. J. McDonald | 2015 | 2 | 5 | Alta | 5 | 3 |
| P2 | Applied Mathematics (4ª ed.) | J. D. Logan | 2013 | 4 | 4 | Media | 4 | 4 |
| P3 | The Matrix Cookbook | K. B. Petersen, M. S. Pedersen | 2012 | 3 | 5 | Alta | 5 | 5 |

#### P1 — *Linear Algebra and Its Applications*
- **Cobertura conceptual:** sistemas lineales, determinantes, espacios vectoriales, autovalores, factorizaciones — con aplicaciones en cada capítulo.
- **Cobertura práctica:** el texto de álgebra lineal más usado en primer y segundo año de ingeniería en América Latina.
- **Valor como guía para el LLM:** nivel introductorio/intermedio con muchos ejemplos resueltos; aporta texto de transición entre bachillerato e ingeniería.
- **Conocimiento que aporta:** la base de álgebra lineal que conoce todo ingeniero; complementa a Strang con perspectiva más clásica.
- **Vocabulario técnico:** *eliminación gaussiana*, *espacio fila*, *transformación lineal*, *valor propio*, *diagonalización*, *descomposición LU*.
- **Razonamiento que aporta:** resolución sistemática de sistemas lineales, interpretación geométrica, aplicaciones a modelos de red.

#### P2 — *Applied Mathematics*
- **Cobertura conceptual:** EDOs, ecuaciones en diferencias, transformadas, sistemas dinámicos, métodos variacionales.
- **Cobertura práctica:** modelar sistemas dinámicos físicos; base para entender sistemas de control y redes neuronales recurrentes.
- **Valor como guía para el LLM:** matemáticas aplicadas con perspectiva de ingeniería; complementa el álgebra lineal y el cálculo con dinámica.
- **Conocimiento que aporta:** el análisis de sistemas dinámicos que conecta matemáticas con ingeniería eléctrica y control.
- **Vocabulario técnico:** *ecuación diferencial ordinaria*, *solución homogénea/particular*, *transformada de Laplace*, *bifurcación*, *estabilidad de Lyapunov*.
- **Razonamiento que aporta:** modelado de sistemas físicos, análisis de estabilidad, clasificación de equilibrios.

#### P3 — *The Matrix Cookbook*
- **Cobertura conceptual:** identidades matriciales, derivadas de matrices, inversas, determinantes, descomposiciones — compendio de referencia.
- **Cobertura práctica:** referencia rápida para derivar expresiones matriciales en ML — usado constantemente en implementación.
- **Valor como guía para el LLM:** alta densidad de identidades con notación consistente; útil para generación de ecuaciones correctas.
- **Conocimiento que aporta:** el arsenal completo de identidades matriciales que todo implementador de ML necesita con frecuencia.
- **Vocabulario técnico:** *traza*, *derivada matricial*, *identidad de Woodbury*, *determinante*, *inversa generalizada*, *producto de Kronecker*.
- **Razonamiento que aporta:** manipulación algebraica de expresiones matriciales, verificación de derivadas.

## Papers importantes

- Strang, G. — *The Fundamental Theorem of Linear Algebra* (American Mathematical Monthly, 1993).
- Tao, T. — *What is Good Mathematics?* (Bulletin AMS, 2007). [arXiv:math/0702396](https://arxiv.org/abs/math/0702396)
- LeCun, Y. et al. — *Efficient BackProp* (Springer, 1998) — análisis numérico de backprop.

## Documentación oficial

- [MIT OpenCourseWare — 18.06 Linear Algebra (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) — videos y materiales libres.
- [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — visualizaciones (YouTube; copyright del autor — verificar licencia).
- [SciPy linear algebra docs](https://docs.scipy.org/doc/scipy/reference/linalg.html) — BSD-3.
- [NumPy linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) — BSD-3.

## Blogs técnicos

- [3Blue1Brown](https://www.3blue1brown.com/) — visualizaciones de álgebra lineal y cálculo (YouTube + artículos).
- [Math StackExchange](https://math.stackexchange.com/) — preguntas y respuestas matemáticas (CC BY-SA 4.0).
- [Better Explained (Kalid Azad)](https://betterexplained.com/) — intuiciones matemáticas accesibles.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) — notas de cálculo y álgebra muy completas.
- [Terence Tao — blog](https://terrytao.wordpress.com/) — análisis y reflexiones matemáticas de alto nivel.

## Repositorios GitHub

- [mitmath/1806](https://github.com/mitmath/1806) — materiales del curso 18.06 de MIT (CC BY-NC-SA).
- [mml-book/mml-book.github.io](https://github.com/mml-book/mml-book.github.io) — libro A1 en PDF (gratis solo para uso personal; sin redistribución).
- [numpy/numpy](https://github.com/numpy/numpy) — álgebra lineal numérica de referencia.
- [scipy/scipy](https://github.com/scipy/scipy) — análisis numérico avanzado en Python.
- [3b1b/manim](https://github.com/3b1b/manim) — animaciones matemáticas de 3Blue1Brown (MIT).

## Benchmarks

- **MATH benchmark** — problemas de matemáticas de competencia (Hendrycks et al., 2021). [arXiv:2103.03874](https://arxiv.org/abs/2103.03874)
- **GSM8K** — problemas de matemáticas de primaria (razonamiento paso a paso).
- **AIME / AMC problems** — problemas de olimpiadas matemáticas, exigentes para LLMs.
- Para evaluar el LLM: preguntas de exámenes de cálculo y álgebra lineal de MIT OpenCourseWare.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| MATH dataset (Hendrycks et al.) | MIT | Problemas de matemáticas con soluciones paso a paso |
| GSM8K | MIT | 8.5K problemas de matemáticas de primaria |
| Khan Academy exercises (datos públicos) | CC BY-NC-SA | Ejercicios con soluciones de múltiples niveles |
| AoPS — Art of Problem Solving forums | Copyright de AoPS — verificar licencia | Discusiones de problemas de competencia con soluciones |
| ProofWiki | CC BY-SA 3.0 | Base de datos de pruebas matemáticas formales |
