# Corpus semilla — dominio: deep_learning

## Retropropagación y la regla de la cadena
<!-- subcategoria: fundamentos | dificultad: intermedio | idioma: es -->
La retropropagación (backpropagation) calcula eficientemente el gradiente de la función de pérdida respecto a todos los parámetros de una red neuronal aplicando la regla de la cadena del cálculo diferencial sobre el grafo computacional. En la pasada hacia adelante se computan y almacenan las activaciones de cada capa; en la pasada hacia atrás se propaga el gradiente desde la salida hacia la entrada, reutilizando los resultados intermedios. Su costo es del mismo orden que la pasada hacia adelante, lo que hace viable entrenar redes profundas. Es una instancia de la diferenciación automática en modo reverso, el motor de frameworks como PyTorch y TensorFlow.

## Funciones de activación y el gradiente que se desvanece
<!-- subcategoria: arquitecturas | dificultad: intermedio | idioma: es -->
Las funciones de activación introducen no linealidad, sin la cual una red de muchas capas colapsaría a una transformación lineal. La sigmoide y la tangente hiperbólica saturan en sus extremos, donde su derivada tiende a cero; en redes profundas esto provoca el problema del gradiente que se desvanece: los gradientes se vuelven minúsculos al retropropagarse muchas capas y las capas iniciales dejan de aprender. ReLU(x) = max(0, x) mitiga el problema al tener derivada constante 1 para entradas positivas, aunque puede 'morir' para entradas negativas. Variantes como Leaky ReLU, GELU y SiLU ofrecen mejor comportamiento del gradiente y son estándar en transformers modernos.

## Normalización por lotes y por capa
<!-- subcategoria: regularizacion | dificultad: avanzado | idioma: es -->
La normalización estabiliza y acelera el entrenamiento al controlar la distribución de las activaciones. Batch Normalization normaliza cada característica usando la media y varianza del minibatch, y aprende parámetros de escala y desplazamiento; reduce el desplazamiento de covariables interno pero depende del tamaño de lote y es problemática en secuencias. Layer Normalization normaliza sobre las características de cada ejemplo individual, independiente del lote, por lo que es la elección estándar en NLP y transformers. RMSNorm simplifica LayerNorm omitiendo el centrado de la media, conservando solo el reescalado por la raíz del promedio de cuadrados; es más barata y se usa en Llama y Qwen.
