# Bibliografía — Metaheurísticas

> Dominio `metaheuristica` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

**Alcance:** Búsqueda aproximada para problemas NP-difíciles, de caja negra o multiobjetivo: algoritmos evolutivos, de trayectoria y de enjambre.

## Libros

### Fundamentales

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Essentials of Metaheuristics (2ª ed.) | S. Luke | 2013 | Gratis en línea; la mejor introducción compacta |
| Introduction to Evolutionary Computing (2ª ed.) | A. E. Eiben, J. E. Smith | 2015 | Marco unificado de algoritmos evolutivos |
| Metaheuristics: From Design to Implementation | E.-G. Talbi | 2009 | Diseño sistemático de metaheurísticas de trayectoria y poblacionales |

### Avanzados

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Handbook of Metaheuristics (3ª ed.) | M. Gendreau, J.-Y. Potvin (eds.) | 2019 | Capítulos de referencia por método |
| Multi-Objective Optimization using Evolutionary Algorithms | K. Deb | 2001 | Frentes de Pareto, NSGA, métricas multiobjetivo |
| Genetic Algorithms in Search, Optimization, and Machine Learning | D. E. Goldberg | 1989 | Clásico fundacional; teorema de esquemas |

### Prácticos

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Tabu Search | F. Glover, M. Laguna | 1997 | Memoria adaptativa, listas tabú, aspiración |
| Ant Colony Optimization | M. Dorigo, T. Stützle | 2004 | ACO para ruteo y combinatoria |
| Swarm Intelligence | J. Kennedy, R. Eberhart | 2001 | Origen de PSO |

## Papers clave

- Kirkpatrick, Gelatt, Vecchi (1983) — Optimization by Simulated Annealing
- Storn & Price (1997) — Differential Evolution
- Wolpert & Macready (1997) — No Free Lunch Theorems for Optimization
- Deb et al. (2002) — NSGA-II
- Hansen (2016) — The CMA Evolution Strategy: A Tutorial
- Snoek, Larochelle, Adams (2012) — Practical Bayesian Optimization of ML Algorithms

## Datos, librerías y fuentes de texto

Librerías y benchmarks: DEAP, pymoo, Optuna, Nevergrad; CEC benchmark suites, TSPLIB, OR-Library.

## Vocabulario que debe dominar el modelo

*metaheurística*, *función de aptitud*, *cruce*, *mutación*, *elitismo*, *frente de Pareto*, *crowding distance*, *temperatura*, *lista tabú*, *exploración/explotación*

> Licencias: los libros guían temas y vocabulario y su texto no se ingiere; el texto del corpus sale solo de las fuentes de [configs/data.yaml](../../configs/data.yaml) (ver índice maestro).
