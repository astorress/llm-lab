# Corpus semilla — dominio: matematicas

## Descomposición en valores singulares (SVD)
<!-- subcategoria: algebra_lineal | dificultad: avanzado | idioma: es -->
La descomposición en valores singulares factoriza cualquier matriz A de m×n como A = UΣVᵀ, donde U (m×m) y V (n×n) son ortogonales y Σ (m×n) es diagonal con los valores singulares σ1 ≥ σ2 ≥ … ≥ 0. Los valores singulares son las raíces de los autovalores de AᵀA. La SVD revela el rango de la matriz (número de σ no nulos), su norma espectral (σ máximo) y su mejor aproximación de rango k (teorema de Eckart-Young): truncar a los k mayores σ minimiza el error de Frobenius. Esto sustenta PCA, sistemas de recomendación, compresión y la pseudoinversa de Moore-Penrose.

## El gradiente y la matriz jacobiana
<!-- subcategoria: calculo | dificultad: intermedio | idioma: es -->
Para una función escalar f(x) de varias variables, el gradiente ∇f es el vector de derivadas parciales; apunta en la dirección de máximo crecimiento y su norma mide la pendiente máxima. Para una función vectorial F: Rⁿ → Rᵐ, la matriz jacobiana J recoge todas las derivadas parciales ∂Fᵢ/∂xⱼ y representa la mejor aproximación lineal local de F. La regla de la cadena multivariable expresa la jacobiana de una composición como el producto de jacobianas, que es exactamente lo que la retropropagación calcula capa por capa en una red neuronal.
