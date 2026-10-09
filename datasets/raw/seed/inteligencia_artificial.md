# Corpus semilla — dominio: inteligencia_artificial

## Búsqueda informada y la heurística A*
<!-- subcategoria: busqueda | dificultad: intermedio | idioma: es -->
Los algoritmos de búsqueda resuelven problemas modelados como espacios de estados con un estado inicial, acciones, y un objetivo. La búsqueda no informada (BFS, DFS, costo uniforme) explora sin conocimiento del dominio. La búsqueda informada usa una heurística h(n) que estima el costo desde un nodo al objetivo. A* combina el costo acumulado g(n) y la heurística en f(n) = g(n) + h(n), expandiendo siempre el nodo de menor f. A* es óptimo y completo si la heurística es admisible (nunca sobreestima) y consistente. La calidad de la heurística determina la eficiencia: una heurística perfecta llevaría directo al objetivo, mientras que h(n)=0 reduce A* a costo uniforme.

## Aprendizaje por refuerzo: MDP y la ecuación de Bellman
<!-- subcategoria: rl | dificultad: avanzado | idioma: es -->
El aprendizaje por refuerzo formaliza la toma de decisiones secuencial como un proceso de decisión de Markov (MDP): estados, acciones, una función de transición P(s'|s,a) y una recompensa r(s,a). El objetivo es hallar una política π que maximice la recompensa acumulada esperada con descuento γ. La función de valor V^π(s) y la función acción-valor Q^π(s,a) satisfacen las ecuaciones de Bellman, que expresan el valor de un estado en términos de los valores de sus sucesores. Algoritmos como Q-learning aprenden Q óptima por iteración de punto fijo, y los métodos de gradiente de política (REINFORCE, PPO) optimizan π directamente. RLHF aplica estas ideas para alinear LLMs.
