# Corpus semilla — dominio: programacion

## Complejidad algorítmica y notación Big-O
<!-- subcategoria: algoritmos | dificultad: introductorio | idioma: es -->
La notación Big-O describe cómo crece el tiempo o el espacio de un algoritmo en función del tamaño de la entrada n, ignorando constantes y términos de menor orden. O(1) es constante, O(log n) logarítmica (búsqueda binaria), O(n) lineal, O(n log n) típica de ordenamientos eficientes (mergesort, heapsort), O(n²) cuadrática (algoritmos ingenuos de comparación de pares) y O(2ⁿ) exponencial (fuerza bruta sobre subconjuntos). Elegir la estructura de datos adecuada cambia la complejidad: buscar en una lista es O(n), en un conjunto hash O(1) promedio. El análisis asintótico guía decisiones de diseño antes de medir.

## Estructuras de datos fundamentales
<!-- subcategoria: estructuras_datos | dificultad: intermedio | idioma: es -->
Las estructuras de datos organizan la información para operaciones eficientes. Los arreglos ofrecen acceso O(1) por índice pero inserción costosa; las listas enlazadas, lo contrario. Las tablas hash dan búsqueda, inserción y borrado O(1) promedio a costa de orden. Los árboles balanceados (AVL, rojo-negro) mantienen operaciones O(log n) y orden, base de los índices B-tree de las bases de datos. Las pilas (LIFO) y colas (FIFO) modelan procesamiento secuencial; los montículos (heaps) dan acceso O(1) al mínimo/máximo y son la base de las colas de prioridad y de algoritmos como Dijkstra.
