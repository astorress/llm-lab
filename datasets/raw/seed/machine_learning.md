# Corpus semilla — dominio: machine_learning

## Descenso de gradiente y la función de pérdida
<!-- subcategoria: optimizacion | dificultad: introductorio | idioma: es -->
El aprendizaje supervisado ajusta los parámetros θ de un modelo para minimizar una función de pérdida L(θ) que mide el error sobre los datos de entrenamiento. El descenso de gradiente actualiza los parámetros en la dirección opuesta al gradiente: θ ← θ − η·∇L(θ), donde η es la tasa de aprendizaje. El gradiente ∇L apunta en la dirección de máximo crecimiento, así que su negativo reduce la pérdida localmente. En la práctica se usa el descenso de gradiente estocástico (SGD), que estima el gradiente sobre minibatches en lugar de todo el dataset, introduciendo ruido que ayuda a escapar de mínimos locales pobres. La elección de η es crítica: demasiado grande diverge, demasiado pequeño converge lentamente.

## El compromiso sesgo-varianza
<!-- subcategoria: teoria | dificultad: intermedio | idioma: es -->
El error de generalización de un modelo se descompone en sesgo, varianza y ruido irreducible. El sesgo mide el error por suposiciones simplificadoras: un modelo demasiado simple (p.ej. regresión lineal para datos no lineales) tiene alto sesgo y subajusta (underfitting). La varianza mide la sensibilidad del modelo a fluctuaciones del conjunto de entrenamiento: un modelo demasiado complejo memoriza el ruido, tiene alta varianza y sobreajusta (overfitting). El compromiso sesgo-varianza explica por qué aumentar la complejidad reduce el sesgo pero aumenta la varianza. Técnicas como la regularización, el dropout y el aumento de datos controlan la varianza sin disparar el sesgo.

## Regularización L1 y L2
<!-- subcategoria: regularizacion | dificultad: intermedio | idioma: es -->
La regularización añade un término de penalización a la función de pérdida para evitar el sobreajuste. La regularización L2 (ridge) suma λ·||w||² y empuja todos los pesos hacia valores pequeños sin anularlos, favoreciendo soluciones suaves; equivale a una prior gaussiana sobre los pesos en la interpretación bayesiana. La regularización L1 (lasso) suma λ·||w||₁ e induce esparsidad: muchos pesos se vuelven exactamente cero, realizando selección de características. El hiperparámetro λ controla la fuerza de la penalización y se elige por validación cruzada. Elastic Net combina ambas penalizaciones.

## Validación cruzada y fuga de datos
<!-- subcategoria: evaluacion | dificultad: intermedio | idioma: es -->
La validación cruzada estima el rendimiento de generalización de un modelo particionando los datos. En k-fold, los datos se dividen en k pliegues; el modelo se entrena en k−1 y se evalúa en el restante, rotando k veces y promediando. Esto usa los datos de forma eficiente y reduce la varianza de la estimación frente a un único split train/test. Un error grave a evitar es la fuga de datos (data leakage): que información del conjunto de prueba contamine el entrenamiento, por ejemplo al escalar características con estadísticas calculadas sobre todo el dataset antes de partir, o al tener duplicados entre train y test. La fuga infla artificialmente las métricas.
