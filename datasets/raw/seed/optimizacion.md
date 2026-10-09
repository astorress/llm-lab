# Corpus semilla — dominio: optimizacion

## Optimización convexa y condiciones KKT
<!-- subcategoria: convexa | dificultad: avanzado | idioma: es -->
Un problema de optimización es convexo si la función objetivo y la región factible lo son; su gran ventaja es que todo mínimo local es global. Para problemas con restricciones, las condiciones de Karush-Kuhn-Tucker (KKT) generalizan los multiplicadores de Lagrange: en el óptimo, el gradiente del objetivo es combinación lineal de los gradientes de las restricciones activas, con multiplicadores no negativos para las desigualdades y holgura complementaria. Para problemas convexos con cualificación de restricciones, las KKT son necesarias y suficientes. La dualidad de Lagrange proporciona cotas inferiores y, sin brecha de dualidad, resuelve el problema vía su dual.

## Optimizadores adaptativos: Adam
<!-- subcategoria: primer_orden | dificultad: intermedio | idioma: es -->
Adam (Adaptive Moment Estimation) combina momentum y tasas de aprendizaje adaptativas por parámetro. Mantiene una media móvil exponencial del gradiente (primer momento m) y de su cuadrado (segundo momento v), aplica corrección de sesgo para los primeros pasos, y actualiza cada parámetro dividiendo m por la raíz de v más epsilon. Esto da pasos grandes en direcciones de gradiente consistente y pequeños en direcciones ruidosas. AdamW desacopla el weight decay del gradiente adaptativo, aplicándolo directamente a los pesos, lo que mejora la generalización y es el estándar para entrenar transformers.
