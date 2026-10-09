"""Documentos semilla del corpus — contenido técnico curado a mano (Etapa 1).

Cada entrada es un documento técnico real (no relleno) de uno de los 26 dominios
del laboratorio. Es el material fuente hand-curated del corpus: ``build_corpus.py``
lo escribe como Markdown en ``datasets/raw/seed/`` y luego lo procesa con el
pipeline de ``llm_lab.data`` (limpieza, calidad, dedup, chunking, splits).

Formato de cada documento:
    (titulo, subcategoria, dificultad, idioma, contenido)

dificultad ∈ {introductorio, intermedio, avanzado}.

Es un CORPUS SEMILLA pequeño pero genuino, calibrado para el perfil SMALL.
Para escalar, añade más documentos aquí o conecta fuentes externas con licencia
(ver docs/02_libros_y_fuentes.md).
"""

from __future__ import annotations

# Estructura: DOMAIN -> list[(titulo, subcategoria, dificultad, lang, contenido)]
SEED: dict[str, list[tuple[str, str, str, str, str]]] = {}

SEED["ingenieria_electrica"] = [
    ("Leyes de Kirchhoff y análisis de circuitos", "circuitos", "introductorio", "es",
     "Las leyes de Kirchhoff son la base del análisis de circuitos. La ley de corrientes (LCK) establece "
     "que la suma algebraica de las corrientes que entran a un nodo es cero, consecuencia de la "
     "conservación de la carga. La ley de voltajes (LVK) establece que la suma algebraica de las "
     "diferencias de potencial en cualquier lazo cerrado es cero, consecuencia de la conservación de la "
     "energía. Combinadas con la ley de Ohm (V = I·R), permiten plantear sistemas de ecuaciones lineales "
     "que se resuelven con análisis nodal (incógnitas: voltajes de nodo) o análisis de malla (incógnitas: "
     "corrientes de lazo). Para circuitos lineales se aplican además los teoremas de superposición, "
     "Thévenin y Norton, que simplifican una red compleja a una fuente equivalente con su impedancia."),
    ("Análisis fasorial en régimen sinusoidal permanente", "corriente_alterna", "intermedio", "es",
     "En régimen sinusoidal permanente, una señal v(t) = Vm·cos(ωt + φ) se representa como un fasor "
     "complejo V = Vm∠φ, lo que convierte ecuaciones diferenciales en ecuaciones algebraicas complejas. "
     "La impedancia generaliza la resistencia: para un resistor Z = R, para un inductor Z = jωL y para un "
     "capacitor Z = 1/(jωC). La potencia compleja S = V·I* = P + jQ separa la potencia activa P (vatios, "
     "trabajo útil) de la reactiva Q (voltamperios reactivos, intercambio con campos). El factor de "
     "potencia cos(φ) mide la eficiencia del uso de la corriente; su corrección con bancos de capacitores "
     "reduce pérdidas y mejora la capacidad de la red."),
    ("Máquinas eléctricas: el motor de inducción", "maquinas", "intermedio", "es",
     "El motor de inducción trifásico es el caballo de batalla de la industria. Su estator genera un campo "
     "magnético rotativo a la velocidad síncrona ns = 120·f/p, donde f es la frecuencia y p el número de "
     "polos. El rotor gira a una velocidad ligeramente menor; el deslizamiento s = (ns − n)/ns es la "
     "fracción de diferencia. Las corrientes inducidas en el rotor (de ahí el nombre) crean el par "
     "motor. El circuito equivalente por fase, similar al de un transformador con la resistencia del "
     "rotor R2/s, permite calcular par, corriente y eficiencia. El par máximo (par de ruptura) ocurre a "
     "un deslizamiento que depende de la relación entre la resistencia y la reactancia del rotor."),
]

SEED["machine_learning"] = [
    ("Descenso de gradiente y la función de pérdida", "optimizacion", "introductorio", "es",
     "El aprendizaje supervisado ajusta los parámetros θ de un modelo para minimizar una función de "
     "pérdida L(θ) que mide el error sobre los datos de entrenamiento. El descenso de gradiente actualiza "
     "los parámetros en la dirección opuesta al gradiente: θ ← θ − η·∇L(θ), donde η es la tasa de "
     "aprendizaje. El gradiente ∇L apunta en la dirección de máximo crecimiento, así que su negativo "
     "reduce la pérdida localmente. En la práctica se usa el descenso de gradiente estocástico (SGD), que "
     "estima el gradiente sobre minibatches en lugar de todo el dataset, introduciendo ruido que ayuda a "
     "escapar de mínimos locales pobres. La elección de η es crítica: demasiado grande diverge, demasiado "
     "pequeño converge lentamente."),
    ("El compromiso sesgo-varianza", "teoria", "intermedio", "es",
     "El error de generalización de un modelo se descompone en sesgo, varianza y ruido irreducible. El "
     "sesgo mide el error por suposiciones simplificadoras: un modelo demasiado simple (p.ej. regresión "
     "lineal para datos no lineales) tiene alto sesgo y subajusta (underfitting). La varianza mide la "
     "sensibilidad del modelo a fluctuaciones del conjunto de entrenamiento: un modelo demasiado complejo "
     "memoriza el ruido, tiene alta varianza y sobreajusta (overfitting). El compromiso sesgo-varianza "
     "explica por qué aumentar la complejidad reduce el sesgo pero aumenta la varianza. Técnicas como la "
     "regularización, el dropout y el aumento de datos controlan la varianza sin disparar el sesgo."),
    ("Regularización L1 y L2", "regularizacion", "intermedio", "es",
     "La regularización añade un término de penalización a la función de pérdida para evitar el "
     "sobreajuste. La regularización L2 (ridge) suma λ·||w||² y empuja todos los pesos hacia valores "
     "pequeños sin anularlos, favoreciendo soluciones suaves; equivale a una prior gaussiana sobre los "
     "pesos en la interpretación bayesiana. La regularización L1 (lasso) suma λ·||w||₁ e induce "
     "esparsidad: muchos pesos se vuelven exactamente cero, realizando selección de características. El "
     "hiperparámetro λ controla la fuerza de la penalización y se elige por validación cruzada. Elastic "
     "Net combina ambas penalizaciones."),
    ("Validación cruzada y fuga de datos", "evaluacion", "intermedio", "es",
     "La validación cruzada estima el rendimiento de generalización de un modelo particionando los datos. "
     "En k-fold, los datos se dividen en k pliegues; el modelo se entrena en k−1 y se evalúa en el "
     "restante, rotando k veces y promediando. Esto usa los datos de forma eficiente y reduce la varianza "
     "de la estimación frente a un único split train/test. Un error grave a evitar es la fuga de datos "
     "(data leakage): que información del conjunto de prueba contamine el entrenamiento, por ejemplo al "
     "escalar características con estadísticas calculadas sobre todo el dataset antes de partir, o al "
     "tener duplicados entre train y test. La fuga infla artificialmente las métricas."),
]

SEED["deep_learning"] = [
    ("Retropropagación y la regla de la cadena", "fundamentos", "intermedio", "es",
     "La retropropagación (backpropagation) calcula eficientemente el gradiente de la función de pérdida "
     "respecto a todos los parámetros de una red neuronal aplicando la regla de la cadena del cálculo "
     "diferencial sobre el grafo computacional. En la pasada hacia adelante se computan y almacenan las "
     "activaciones de cada capa; en la pasada hacia atrás se propaga el gradiente desde la salida hacia "
     "la entrada, reutilizando los resultados intermedios. Su costo es del mismo orden que la pasada hacia "
     "adelante, lo que hace viable entrenar redes profundas. Es una instancia de la diferenciación "
     "automática en modo reverso, el motor de frameworks como PyTorch y TensorFlow."),
    ("Funciones de activación y el gradiente que se desvanece", "arquitecturas", "intermedio", "es",
     "Las funciones de activación introducen no linealidad, sin la cual una red de muchas capas colapsaría "
     "a una transformación lineal. La sigmoide y la tangente hiperbólica saturan en sus extremos, donde su "
     "derivada tiende a cero; en redes profundas esto provoca el problema del gradiente que se desvanece: "
     "los gradientes se vuelven minúsculos al retropropagarse muchas capas y las capas iniciales dejan de "
     "aprender. ReLU(x) = max(0, x) mitiga el problema al tener derivada constante 1 para entradas "
     "positivas, aunque puede 'morir' para entradas negativas. Variantes como Leaky ReLU, GELU y SiLU "
     "ofrecen mejor comportamiento del gradiente y son estándar en transformers modernos."),
    ("Normalización por lotes y por capa", "regularizacion", "avanzado", "es",
     "La normalización estabiliza y acelera el entrenamiento al controlar la distribución de las "
     "activaciones. Batch Normalization normaliza cada característica usando la media y varianza del "
     "minibatch, y aprende parámetros de escala y desplazamiento; reduce el desplazamiento de covariables "
     "interno pero depende del tamaño de lote y es problemática en secuencias. Layer Normalization "
     "normaliza sobre las características de cada ejemplo individual, independiente del lote, por lo que es "
     "la elección estándar en NLP y transformers. RMSNorm simplifica LayerNorm omitiendo el centrado de "
     "la media, conservando solo el reescalado por la raíz del promedio de cuadrados; es más barata y se "
     "usa en Llama y Qwen."),
]

SEED["inteligencia_artificial"] = [
    ("Búsqueda informada y la heurística A*", "busqueda", "intermedio", "es",
     "Los algoritmos de búsqueda resuelven problemas modelados como espacios de estados con un estado "
     "inicial, acciones, y un objetivo. La búsqueda no informada (BFS, DFS, costo uniforme) explora sin "
     "conocimiento del dominio. La búsqueda informada usa una heurística h(n) que estima el costo desde un "
     "nodo al objetivo. A* combina el costo acumulado g(n) y la heurística en f(n) = g(n) + h(n), "
     "expandiendo siempre el nodo de menor f. A* es óptimo y completo si la heurística es admisible (nunca "
     "sobreestima) y consistente. La calidad de la heurística determina la eficiencia: una heurística "
     "perfecta llevaría directo al objetivo, mientras que h(n)=0 reduce A* a costo uniforme."),
    ("Aprendizaje por refuerzo: MDP y la ecuación de Bellman", "rl", "avanzado", "es",
     "El aprendizaje por refuerzo formaliza la toma de decisiones secuencial como un proceso de decisión "
     "de Markov (MDP): estados, acciones, una función de transición P(s'|s,a) y una recompensa r(s,a). El "
     "objetivo es hallar una política π que maximice la recompensa acumulada esperada con descuento γ. La "
     "función de valor V^π(s) y la función acción-valor Q^π(s,a) satisfacen las ecuaciones de Bellman, que "
     "expresan el valor de un estado en términos de los valores de sus sucesores. Algoritmos como "
     "Q-learning aprenden Q óptima por iteración de punto fijo, y los métodos de gradiente de política "
     "(REINFORCE, PPO) optimizan π directamente. RLHF aplica estas ideas para alinear LLMs."),
]

SEED["ciencia_datos"] = [
    ("El proceso de ciencia de datos y EDA", "metodologia", "introductorio", "es",
     "Un proyecto de ciencia de datos sigue un ciclo: definición del problema, obtención y limpieza de "
     "datos, análisis exploratorio (EDA), modelado, evaluación y comunicación. El EDA examina "
     "distribuciones, correlaciones, valores faltantes y atípicos antes de modelar, usando estadística "
     "descriptiva y visualización (histogramas, boxplots, scatter, mapas de calor de correlación). La "
     "limpieza —imputación de faltantes, codificación de categóricas, escalado de numéricas— suele "
     "consumir la mayor parte del tiempo. La calidad de las características (feature engineering) impacta "
     "el rendimiento más que la elección del algoritmo en muchos problemas tabulares."),
    ("Pandas: manipulación de datos tabulares", "herramientas", "intermedio", "es",
     "Pandas es la librería estándar de Python para datos tabulares. Su estructura central, el DataFrame, "
     "es una tabla bidimensional con índices etiquetados. Operaciones clave: filtrado booleano "
     "(df[df.x > 0]), agregación con groupby (df.groupby('dominio').size()), combinación con merge y "
     "concat, y reformateo con pivot y melt. El método apply aplica funciones por fila o columna, aunque "
     "las operaciones vectorizadas son mucho más rápidas. Para datos grandes, formatos columnar como "
     "Parquet y herramientas como Polars o Dask superan a Pandas en memoria y velocidad."),
]

SEED["matematicas"] = [
    ("Descomposición en valores singulares (SVD)", "algebra_lineal", "avanzado", "es",
     "La descomposición en valores singulares factoriza cualquier matriz A de m×n como A = UΣVᵀ, donde U "
     "(m×m) y V (n×n) son ortogonales y Σ (m×n) es diagonal con los valores singulares σ1 ≥ σ2 ≥ … ≥ 0. "
     "Los valores singulares son las raíces de los autovalores de AᵀA. La SVD revela el rango de la "
     "matriz (número de σ no nulos), su norma espectral (σ máximo) y su mejor aproximación de rango k "
     "(teorema de Eckart-Young): truncar a los k mayores σ minimiza el error de Frobenius. Esto sustenta "
     "PCA, sistemas de recomendación, compresión y la pseudoinversa de Moore-Penrose."),
    ("El gradiente y la matriz jacobiana", "calculo", "intermedio", "es",
     "Para una función escalar f(x) de varias variables, el gradiente ∇f es el vector de derivadas "
     "parciales; apunta en la dirección de máximo crecimiento y su norma mide la pendiente máxima. Para "
     "una función vectorial F: Rⁿ → Rᵐ, la matriz jacobiana J recoge todas las derivadas parciales "
     "∂Fᵢ/∂xⱼ y representa la mejor aproximación lineal local de F. La regla de la cadena multivariable "
     "expresa la jacobiana de una composición como el producto de jacobianas, que es exactamente lo que "
     "la retropropagación calcula capa por capa en una red neuronal."),
]

SEED["estadistica"] = [
    ("Estimación por máxima verosimilitud", "inferencia", "avanzado", "es",
     "La estimación por máxima verosimilitud (MLE) elige los parámetros θ que maximizan la probabilidad de "
     "los datos observados bajo el modelo: θ_MLE = argmax L(θ; datos), donde L es la función de "
     "verosimilitud. En la práctica se maximiza el logaritmo (log-verosimilitud), que convierte productos "
     "en sumas y es numéricamente estable. Para muchos modelos, minimizar la entropía cruzada equivale a "
     "MLE: entrenar un clasificador con cross-entropy es estimar por máxima verosimilitud una "
     "distribución categórica. Bajo condiciones de regularidad, el MLE es consistente y asintóticamente "
     "eficiente, alcanzando la cota de Cramér-Rao."),
    ("Teorema de Bayes e inferencia bayesiana", "bayesiana", "intermedio", "es",
     "El teorema de Bayes actualiza creencias ante evidencia: P(θ|datos) ∝ P(datos|θ)·P(θ), es decir, el "
     "posterior es proporcional a la verosimilitud por el prior. La inferencia bayesiana trata los "
     "parámetros como variables aleatorias con distribución, en contraste con el enfoque frecuentista que "
     "los considera fijos pero desconocidos. El prior codifica conocimiento previo; con priors conjugados "
     "el posterior tiene forma cerrada. Cuando no, se recurre a métodos de Monte Carlo (MCMC) o inferencia "
     "variacional. El posterior permite cuantificar incertidumbre con intervalos de credibilidad."),
]

SEED["optimizacion"] = [
    ("Optimización convexa y condiciones KKT", "convexa", "avanzado", "es",
     "Un problema de optimización es convexo si la función objetivo y la región factible lo son; su gran "
     "ventaja es que todo mínimo local es global. Para problemas con restricciones, las condiciones de "
     "Karush-Kuhn-Tucker (KKT) generalizan los multiplicadores de Lagrange: en el óptimo, el gradiente del "
     "objetivo es combinación lineal de los gradientes de las restricciones activas, con multiplicadores "
     "no negativos para las desigualdades y holgura complementaria. Para problemas convexos con "
     "cualificación de restricciones, las KKT son necesarias y suficientes. La dualidad de Lagrange "
     "proporciona cotas inferiores y, sin brecha de dualidad, resuelve el problema vía su dual."),
    ("Optimizadores adaptativos: Adam", "primer_orden", "intermedio", "es",
     "Adam (Adaptive Moment Estimation) combina momentum y tasas de aprendizaje adaptativas por parámetro. "
     "Mantiene una media móvil exponencial del gradiente (primer momento m) y de su cuadrado (segundo "
     "momento v), aplica corrección de sesgo para los primeros pasos, y actualiza cada parámetro dividiendo "
     "m por la raíz de v más epsilon. Esto da pasos grandes en direcciones de gradiente consistente y "
     "pequeños en direcciones ruidosas. AdamW desacopla el weight decay del gradiente adaptativo, "
     "aplicándolo directamente a los pesos, lo que mejora la generalización y es el estándar para "
     "entrenar transformers."),
]

SEED["python"] = [
    ("Generadores e iteradores perezosos", "lenguaje", "intermedio", "es",
     "Un generador en Python es una función que usa yield para producir valores uno a uno, manteniendo su "
     "estado entre llamadas. A diferencia de una lista, no materializa todos los valores en memoria, lo que "
     "permite procesar secuencias enormes o infinitas con consumo constante. Las expresiones generadoras "
     "(x*x for x in range(n)) son su forma compacta. El protocolo de iteración (__iter__ y __next__) "
     "sustenta los bucles for. Combinados con itertools, los generadores permiten construir pipelines de "
     "datos eficientes y componibles, fundamentales para el streaming de corpus en entrenamiento de LLMs."),
    ("Decoradores y funciones de orden superior", "lenguaje", "intermedio", "es",
     "Un decorador es una función que recibe otra función y devuelve una versión modificada, aprovechando "
     "que en Python las funciones son objetos de primera clase. La sintaxis @decorador antepuesta a una "
     "definición es azúcar para func = decorador(func). Se usan para añadir comportamiento transversal sin "
     "modificar el cuerpo: logging, medición de tiempo, caché (@functools.lru_cache), validación o "
     "registro. functools.wraps preserva los metadatos de la función original. Los decoradores con "
     "argumentos requieren un nivel adicional de anidamiento de funciones."),
    ("Type hints y tipado gradual", "lenguaje", "intermedio", "es",
     "Las anotaciones de tipo (type hints, PEP 484) permiten declarar los tipos esperados de variables, "
     "parámetros y retornos sin afectar la ejecución: Python sigue siendo de tipado dinámico. Herramientas "
     "como mypy o pyright verifican estáticamente la consistencia de tipos, detectando errores antes de "
     "ejecutar. El módulo typing aporta genéricos (list[int], dict[str, float]), uniones (int | None), "
     "Protocol para tipado estructural y TypeVar para genéricos. El tipado gradual mejora la "
     "mantenibilidad y la autocompletación en bases de código grandes."),
]

SEED["programacion"] = [
    ("Complejidad algorítmica y notación Big-O", "algoritmos", "introductorio", "es",
     "La notación Big-O describe cómo crece el tiempo o el espacio de un algoritmo en función del tamaño "
     "de la entrada n, ignorando constantes y términos de menor orden. O(1) es constante, O(log n) "
     "logarítmica (búsqueda binaria), O(n) lineal, O(n log n) típica de ordenamientos eficientes "
     "(mergesort, heapsort), O(n²) cuadrática (algoritmos ingenuos de comparación de pares) y O(2ⁿ) "
     "exponencial (fuerza bruta sobre subconjuntos). Elegir la estructura de datos adecuada cambia la "
     "complejidad: buscar en una lista es O(n), en un conjunto hash O(1) promedio. El análisis asintótico "
     "guía decisiones de diseño antes de medir."),
    ("Estructuras de datos fundamentales", "estructuras_datos", "intermedio", "es",
     "Las estructuras de datos organizan la información para operaciones eficientes. Los arreglos ofrecen "
     "acceso O(1) por índice pero inserción costosa; las listas enlazadas, lo contrario. Las tablas hash "
     "dan búsqueda, inserción y borrado O(1) promedio a costa de orden. Los árboles balanceados (AVL, "
     "rojo-negro) mantienen operaciones O(log n) y orden, base de los índices B-tree de las bases de "
     "datos. Las pilas (LIFO) y colas (FIFO) modelan procesamiento secuencial; los montículos (heaps) dan "
     "acceso O(1) al mínimo/máximo y son la base de las colas de prioridad y de algoritmos como Dijkstra."),
]

SEED["postgresql"] = [
    ("Índices B-tree y planificación de consultas", "rendimiento", "intermedio", "es",
     "PostgreSQL crea por defecto índices B-tree, eficientes para búsquedas por igualdad y rango en "
     "O(log n). Un índice acelera las lecturas pero ralentiza las escrituras y ocupa espacio, por lo que "
     "se crean selectivamente sobre columnas usadas en WHERE, JOIN y ORDER BY. El planificador de "
     "consultas estima el costo de planes alternativos (escaneo secuencial vs. por índice) usando "
     "estadísticas de la tabla; EXPLAIN ANALYZE muestra el plan elegido y los tiempos reales. Otros tipos "
     "de índice: GIN para búsqueda de texto completo y arrays, GiST para datos geométricos, y BRIN para "
     "tablas grandes con correlación física."),
    ("Transacciones ACID y control de concurrencia MVCC", "transacciones", "avanzado", "es",
     "PostgreSQL garantiza las propiedades ACID: atomicidad (todo o nada), consistencia, aislamiento y "
     "durabilidad. La durabilidad se logra con el Write-Ahead Log (WAL): los cambios se registran antes de "
     "aplicarse a los datos. El aislamiento se implementa con control de concurrencia multiversión (MVCC): "
     "cada transacción ve una instantánea consistente de los datos sin bloquear a los lectores, ya que las "
     "actualizaciones crean nuevas versiones de las filas en lugar de sobrescribirlas. Los niveles de "
     "aislamiento (read committed, repeatable read, serializable) equilibran consistencia y concurrencia, "
     "previniendo fenómenos como lecturas sucias o fantasma."),
]

SEED["mongodb"] = [
    ("Modelo de documentos y diseño de esquema", "modelado", "intermedio", "es",
     "MongoDB es una base de datos NoSQL orientada a documentos: almacena registros como documentos BSON "
     "(JSON binario) flexibles, agrupados en colecciones. A diferencia del modelo relacional normalizado, "
     "MongoDB favorece la desnormalización y el embebido de datos relacionados en un solo documento cuando "
     "se leen juntos, evitando JOINs. La regla práctica: 'los datos que se acceden juntos se almacenan "
     "juntos'. Para relaciones uno-a-muchos de alta cardinalidad o datos compartidos se usan referencias. "
     "El diseño del esquema se guía por los patrones de consulta de la aplicación, no por la estructura "
     "de los datos en sí."),
    ("El pipeline de agregación", "consultas", "intermedio", "es",
     "El framework de agregación de MongoDB procesa documentos a través de una secuencia de etapas (un "
     "pipeline), cada una transformando el flujo. Etapas comunes: $match filtra (como WHERE), $group "
     "agrupa y agrega (como GROUP BY con sum, avg, count), $project remodela los campos, $sort ordena, "
     "$lookup hace una unión con otra colección, y $unwind descompone arrays. El orden importa para el "
     "rendimiento: filtrar con $match temprano reduce los documentos procesados aguas abajo. Es el "
     "equivalente analítico de las consultas SQL complejas, ejecutado del lado del servidor."),
]

SEED["aws"] = [
    ("AWS Lambda y el cómputo serverless", "computo", "intermedio", "es",
     "AWS Lambda ejecuta código en respuesta a eventos sin que el desarrollador gestione servidores. Se "
     "factura por número de invocaciones y por la duración de ejecución (en milisegundos) multiplicada por "
     "la memoria asignada. Escala automáticamente de cero a miles de ejecuciones concurrentes. Es ideal "
     "para APIs (con API Gateway), procesamiento de eventos (S3, DynamoDB Streams, SQS) y tareas "
     "programadas. Limitaciones a considerar: tiempo máximo de ejecución (15 minutos), arranques en frío "
     "(latencia al inicializar un contenedor nuevo) y tamaño del paquete de despliegue. El modelo de "
     "concurrencia y los timeouts deben dimensionarse según la carga."),
    ("Almacenamiento S3 y clases de almacenamiento", "almacenamiento", "introductorio", "es",
     "Amazon S3 (Simple Storage Service) ofrece almacenamiento de objetos altamente durable (99,999999999% "
     "de durabilidad) y escalable prácticamente sin límite. Los objetos se organizan en buckets con claves "
     "únicas. Las clases de almacenamiento optimizan el costo según el patrón de acceso: S3 Standard para "
     "datos de acceso frecuente, S3 Intelligent-Tiering que mueve objetos automáticamente, S3 "
     "Standard-IA y One Zone-IA para acceso infrecuente, y Glacier para archivado a largo plazo con "
     "recuperación más lenta y barata. Las políticas de ciclo de vida automatizan la transición entre "
     "clases para reducir costos."),
]

SEED["serverless"] = [
    ("Serverless Framework e infraestructura declarativa", "framework", "intermedio", "es",
     "El Serverless Framework define aplicaciones serverless de forma declarativa en un archivo "
     "serverless.yml: funciones, los eventos que las disparan (HTTP, colas, cron), recursos de "
     "infraestructura y permisos IAM. Con un solo comando empaqueta el código y lo despliega, traduciendo "
     "la configuración a CloudFormation en AWS. Abstrae la complejidad de aprovisionar API Gateway, "
     "Lambda, roles y políticas. Soporta múltiples proveedores y un ecosistema de plugins (offline para "
     "desarrollo local, warmup contra arranques en frío). Encaja en flujos de infraestructura como código "
     "y CI/CD, versionando la definición de la arquitectura junto al código."),
]

SEED["iac"] = [
    ("Infraestructura como código con Terraform", "terraform", "intermedio", "es",
     "La infraestructura como código (IaC) gestiona recursos de cómputo, red y almacenamiento mediante "
     "archivos versionados en lugar de configuración manual. Terraform usa un lenguaje declarativo (HCL): "
     "se describe el estado deseado y Terraform calcula el plan de cambios (terraform plan) para "
     "alcanzarlo, aplicándolo de forma idempotente (terraform apply). Mantiene un archivo de estado que "
     "mapea los recursos reales con la configuración. Los módulos encapsulan y reutilizan componentes; los "
     "proveedores abstraen las APIs de AWS, Azure, GCP y otros. El estado remoto compartido y el bloqueo "
     "evitan conflictos en equipos."),
]

SEED["apis"] = [
    ("Diseño de APIs REST y semántica HTTP", "rest", "intermedio", "es",
     "REST es un estilo arquitectónico que modela la API como recursos identificados por URLs, manipulados "
     "con los métodos HTTP según su semántica: GET (leer, seguro e idempotente), POST (crear), PUT "
     "(reemplazar, idempotente), PATCH (actualizar parcial), DELETE (borrar, idempotente). Los códigos de "
     "estado comunican el resultado: 2xx éxito, 4xx error del cliente (400 petición inválida, 401 no "
     "autenticado, 404 no encontrado), 5xx error del servidor. Buenas prácticas: nombrar recursos con "
     "sustantivos en plural, versionar la API, paginar colecciones, y devolver errores con estructura "
     "consistente. La idempotencia permite reintentos seguros."),
    ("Autenticación con JWT y OAuth 2.0", "seguridad", "avanzado", "es",
     "OAuth 2.0 es un marco de autorización delegada: permite a una aplicación acceder a recursos en nombre "
     "del usuario sin manejar sus credenciales, mediante tokens de acceso emitidos por un servidor de "
     "autorización. Los JSON Web Tokens (JWT) son un formato compacto y autocontenido de token: codifican "
     "claims (emisor, sujeto, expiración, permisos) firmados criptográficamente, de modo que el servidor "
     "puede validarlos sin consultar una base de datos (stateless). El servidor verifica la firma con la "
     "clave correspondiente. Riesgos a mitigar: expiración corta, rotación de claves, almacenamiento "
     "seguro del token y validación estricta de la firma y los claims."),
]

SEED["arquitectura_software"] = [
    ("Principios SOLID y arquitectura limpia", "principios", "intermedio", "es",
     "Los principios SOLID guían el diseño orientado a objetos mantenible: responsabilidad única (una clase "
     "una razón para cambiar), abierto/cerrado (abierto a extensión, cerrado a modificación), sustitución "
     "de Liskov (los subtipos deben ser sustituibles por sus tipos base), segregación de interfaces "
     "(interfaces específicas mejor que una general) e inversión de dependencias (depender de abstracciones, "
     "no de concreciones). La arquitectura limpia aplica la inversión de dependencias a nivel de sistema: "
     "la lógica de negocio en el centro no depende de detalles como la base de datos o el framework web, "
     "que quedan en capas externas; las dependencias apuntan siempre hacia adentro."),
    ("Microservicios frente al monolito", "estilos", "avanzado", "es",
     "Una arquitectura de microservicios descompone una aplicación en servicios pequeños e independientes, "
     "cada uno con su responsabilidad de negocio, base de datos y ciclo de despliegue. Frente al monolito, "
     "ofrece escalado independiente, despliegues autónomos y aislamiento de fallos, a costa de complejidad "
     "operativa: comunicación en red, consistencia distribuida, observabilidad y orquestación. La frontera "
     "de cada servicio se define idealmente alrededor de un bounded context del dominio (DDD). Patrones "
     "clave: API Gateway, circuit breaker para tolerancia a fallos, y sagas para transacciones distribuidas. "
     "No es la opción por defecto: el monolito modular suele ser preferible al inicio."),
]

SEED["devops"] = [
    ("Integración y entrega continua (CI/CD)", "cicd", "intermedio", "es",
     "La integración continua (CI) automatiza la construcción y prueba del código cada vez que se integra "
     "un cambio, detectando errores temprano. La entrega/despliegue continuo (CD) extiende el pipeline "
     "hasta poner los cambios en producción de forma automática y frecuente. Un pipeline típico: checkout, "
     "build, pruebas unitarias e integración, análisis estático, construcción de imagen, despliegue a "
     "staging y a producción. Estrategias de despliegue como blue-green y canary reducen el riesgo "
     "liberando gradualmente. Las métricas DORA (frecuencia de despliegue, lead time, tasa de fallo de "
     "cambios, tiempo de recuperación) miden la madurez del flujo de entrega."),
    ("Contenedores con Docker y orquestación", "contenedores", "intermedio", "es",
     "Docker empaqueta una aplicación con todas sus dependencias en una imagen inmutable que se ejecuta "
     "igual en cualquier entorno, resolviendo el clásico 'en mi máquina funciona'. Una imagen se construye "
     "por capas desde un Dockerfile; los contenedores son instancias en ejecución de una imagen, aislados "
     "pero compartiendo el kernel del host (más ligeros que máquinas virtuales). A escala, un orquestador "
     "como Kubernetes gestiona el despliegue declarativo, el escalado, el balanceo de carga y la "
     "recuperación de contenedores fallidos, reconciliando continuamente el estado real con el deseado."),
]

SEED["data_engineering"] = [
    ("Pipelines ETL/ELT y orquestación", "pipelines", "intermedio", "es",
     "Un pipeline de datos mueve y transforma datos desde las fuentes hasta su destino analítico. ETL "
     "(extraer, transformar, cargar) transforma antes de cargar; ELT carga datos crudos en un almacén o "
     "lago y los transforma allí, aprovechando la potencia del destino (patrón dominante con la nube y "
     "herramientas como dbt). La orquestación (Airflow, Dagster) modela el pipeline como un grafo acíclico "
     "dirigido (DAG) de tareas con dependencias, programación, reintentos y backfills. Principios clave: "
     "idempotencia (re-ejecutar produce el mismo resultado), particionamiento por fecha y validación de "
     "calidad de datos en cada etapa."),
    ("Formatos columnar: Parquet y Arrow", "almacenamiento", "intermedio", "es",
     "Los formatos columnar almacenan los datos por columna en lugar de por fila, lo que beneficia a las "
     "cargas analíticas: solo se leen las columnas necesarias y la compresión es muy eficiente al agrupar "
     "valores del mismo tipo. Apache Parquet es el formato de archivo columnar estándar para "
     "almacenamiento, con compresión y esquema embebido. Apache Arrow define un formato columnar en "
     "memoria que permite intercambiar datos entre sistemas sin serialización y procesarlos de forma "
     "vectorizada. En este laboratorio, el corpus se guarda en Parquet por su compresión (5-10x menor que "
     "JSONL) y en Arrow para iterar datasets mayores que la RAM mediante memory-mapping."),
]

SEED["sistemas_distribuidos"] = [
    ("El teorema CAP y la consistencia", "teoria", "avanzado", "es",
     "El teorema CAP establece que un sistema distribuido no puede garantizar simultáneamente las tres "
     "propiedades: consistencia (todos los nodos ven los mismos datos a la vez), disponibilidad (toda "
     "petición recibe respuesta) y tolerancia a particiones (el sistema sigue operando pese a fallos de "
     "red). Como las particiones son inevitables en la práctica, el diseño elige entre consistencia (CP) "
     "y disponibilidad (AP) ante una partición. Esto se refina con modelos de consistencia: la "
     "linealizabilidad (la más fuerte) hace que las operaciones parezcan instantáneas y ordenadas, "
     "mientras que la consistencia eventual solo garantiza convergencia con el tiempo, ofreciendo mayor "
     "disponibilidad y menor latencia."),
    ("Consenso distribuido: Raft", "consenso", "avanzado", "es",
     "El consenso permite que un conjunto de nodos acuerde un valor pese a fallos, base de la replicación "
     "consistente. Raft es un algoritmo de consenso diseñado para ser comprensible. Elige un líder que "
     "recibe todas las escrituras de los clientes y las replica como entradas de un log a los seguidores; "
     "una entrada se considera comprometida (committed) cuando una mayoría la ha replicado. Si el líder "
     "falla, los seguidores detectan la ausencia de latidos y, tras un timeout aleatorizado, inician una "
     "elección por términos votando por un nuevo líder. Raft separa el problema en elección de líder, "
     "replicación de log y seguridad, garantizando que los logs comprometidos nunca se pierden."),
]


SEED["metaheuristica"] = [
    ("Algoritmos genéticos: selección, cruce y mutación", "evolutivos", "intermedio", "es",
     "Un algoritmo genético es una metaheurística poblacional inspirada en la evolución natural. Cada "
     "individuo codifica una solución candidata (un cromosoma binario, real o una permutación) y se evalúa "
     "con una función de aptitud. En cada generación se seleccionan padres con probabilidad creciente en su "
     "aptitud (ruleta, torneo o ranking), se recombinan mediante un operador de cruce (un punto, uniforme, "
     "SBX para variables reales u OX para permutaciones) y se aplica mutación con baja probabilidad para "
     "mantener diversidad. El elitismo conserva los mejores individuos entre generaciones. El equilibrio "
     "entre exploración y explotación lo controlan la presión de selección y las tasas de cruce y mutación: "
     "demasiada presión provoca convergencia prematura a un óptimo local; demasiada mutación degrada la "
     "búsqueda a un muestreo aleatorio. El teorema No Free Lunch recuerda que ninguna metaheurística supera "
     "a las demás promediando sobre todos los problemas: su ventaja depende de explotar la estructura del "
     "problema concreto."),
    ("Recocido simulado, búsqueda tabú y enjambre de partículas", "trayectoria_y_enjambre", "avanzado", "es",
     "El recocido simulado (simulated annealing) es una búsqueda local que acepta movimientos peores con "
     "probabilidad exp(−Δ/T), donde Δ es el empeoramiento del costo y T una temperatura que decrece según un "
     "esquema de enfriamiento (geométrico T ← αT con α≈0.95, o logarítmico, que garantiza convergencia "
     "asintótica al óptimo global pero es impracticablemente lento). La búsqueda tabú, en cambio, siempre se "
     "mueve al mejor vecino no prohibido y mantiene una lista tabú de movimientos recientes para evitar ciclos; "
     "un criterio de aspiración permite violar la prohibición si se alcanza un nuevo mejor global. La "
     "optimización por enjambre de partículas (PSO) actualiza la velocidad de cada partícula como "
     "v ← w·v + c1·r1·(p_best − x) + c2·r2·(g_best − x): la inercia w favorece la exploración y los términos "
     "cognitivo y social la explotación. Para problemas multiobjetivo, NSGA-II ordena la población por frentes "
     "de Pareto no dominados y usa la distancia de crowding para preservar diversidad a lo largo del frente."),
]

SEED["llm"] = [
    ("Cómo funciona un modelo de lenguaje grande", "fundamentos", "intermedio", "es",
     "Un modelo de lenguaje grande (LLM) es un transformer decoder-only entrenado para predecir el siguiente "
     "token: dado un contexto x_1..x_t, estima p(x_{t+1} | x_1..x_t) y se optimiza minimizando la entropía "
     "cruzada sobre billones de tokens. El texto se convierte en tokens con un tokenizador BPE, cada token se "
     "proyecta a un embedding y una pila de bloques de self-attention causal y redes feed-forward construye "
     "representaciones contextuales. El entrenamiento ocurre en etapas: pre-entrenamiento auto-supervisado "
     "(conocimiento y lenguaje), instruction tuning o SFT con pares instrucción-respuesta (formato de "
     "asistente) y alineación con preferencias humanas mediante RLHF o DPO. Las leyes de escalado muestran "
     "que la pérdida decrece como ley de potencia con parámetros, datos y cómputo; Chinchilla estableció que "
     "el óptimo usa unos 20 tokens por parámetro. En inferencia, el KV cache evita recomputar el prefijo y la "
     "ventana de contexto limita cuánta información puede usar el modelo en una sola consulta."),
    ("RAG, fine-tuning con LoRA y alucinaciones", "aplicaciones", "avanzado", "es",
     "Para especializar un LLM hay dos caminos complementarios. Retrieval-Augmented Generation (RAG) recupera "
     "fragmentos relevantes de una base de datos vectorial mediante similitud de embeddings y los inserta en el "
     "prompt: actualiza el conocimiento sin reentrenar y permite citar fuentes. El fine-tuning ajusta los pesos; "
     "LoRA congela la matriz original W y aprende una actualización de bajo rango ΔW = B·A con r ≪ d, reduciendo "
     "los parámetros entrenables a menos del 1 %, y QLoRA además cuantiza el modelo base a 4 bits para caber en "
     "una sola GPU. Las alucinaciones —respuestas fluidas pero falsas— surgen porque el modelo maximiza "
     "plausibilidad, no veracidad; se mitigan con RAG, instrucciones que permiten responder 'no sé', "
     "chain-of-thought para problemas de varios pasos y evaluación sistemática con conjuntos de prueba propios. "
     "Few-shot e in-context learning permiten adaptar el comportamiento con ejemplos en el prompt, sin tocar "
     "los pesos."),
]

SEED["full_stack"] = [
    ("Arquitectura de una aplicación web full stack", "arquitectura_web", "intermedio", "es",
     "Una aplicación full stack se divide en frontend, backend y persistencia. El frontend (React, Vue o "
     "Angular, usualmente con TypeScript) renderiza la interfaz, gestiona el estado de la aplicación y consume "
     "APIs; frameworks como Next.js añaden renderizado del lado del servidor (SSR) y generación estática para "
     "mejorar el tiempo de carga y el SEO. El backend (Node.js con Express, Python con FastAPI o Django) expone "
     "endpoints REST o GraphQL, valida entradas, aplica reglas de negocio y autenticación (sesiones o JWT con "
     "OAuth). La capa de datos usa un ORM como Prisma o SQLAlchemy sobre PostgreSQL, con migraciones "
     "versionadas. Para tiempo real se usan WebSockets. El diseño responsivo con CSS moderno o Tailwind adapta "
     "la interfaz a móviles. Una buena separación de responsabilidades permite desplegar frontend y backend de "
     "forma independiente y escalar cada capa según su carga."),
    ("Estado, componentes y rendimiento en React", "frontend", "intermedio", "es",
     "En React la interfaz es una función del estado: cada componente recibe props, mantiene estado local con "
     "useState y declara efectos secundarios con useEffect. Cuando el estado cambia, React vuelve a renderizar y "
     "reconcilia el DOM virtual con el real aplicando solo las diferencias. El estado compartido entre muchos "
     "componentes se eleva a un ancestro común o se gestiona con Context, Zustand o Redux; el estado del "
     "servidor (datos remotos) conviene manejarlo con librerías como TanStack Query, que cachean, deduplican y "
     "revalidan peticiones. Para rendimiento: memoizar cálculos costosos con useMemo, estabilizar callbacks "
     "con useCallback, dividir el bundle con carga diferida (lazy) y virtualizar listas largas. Herramientas "
     "como Vite aceleran el desarrollo con recarga en caliente, y las pruebas de componentes con Testing "
     "Library verifican el comportamiento desde la perspectiva del usuario."),
]

SEED["analitica"] = [
    ("Modelado dimensional y business intelligence", "bi", "intermedio", "es",
     "La analítica de negocio organiza los datos para responder preguntas de forma rápida y consistente. El "
     "modelado dimensional de Kimball separa tablas de hechos —eventos medibles como ventas o visitas, con su "
     "granularidad bien definida— de tablas de dimensiones —cliente, producto, fecha— que dan contexto. El "
     "esquema estrella une cada hecho directamente con sus dimensiones y simplifica las consultas; las "
     "dimensiones lentamente cambiantes (SCD tipo 2) conservan la historia de atributos. Sobre este modelo, "
     "herramientas de business intelligence como Power BI, Tableau, Looker o Metabase construyen dashboards "
     "y cuadros de mando. Un buen KPI está alineado con un objetivo, tiene una definición única y documentada "
     "(una sola fórmula de 'cliente activo' en toda la organización), una meta y un responsable. En Power BI, "
     "DAX permite definir medidas que se recalculan según el contexto de filtro del reporte."),
    ("Análisis de cohortes, embudos y analítica predictiva", "producto", "intermedio", "es",
     "El análisis de cohortes agrupa usuarios por el periodo en que ocurrió un evento común (por ejemplo, el "
     "mes de registro) y sigue su comportamiento en el tiempo; la matriz de retención resultante revela si los "
     "cambios de producto mejoran la permanencia de las cohortes nuevas frente a las antiguas. Un embudo de "
     "conversión mide la proporción de usuarios que avanza entre pasos sucesivos (visita, registro, compra) y "
     "localiza dónde se pierde más gente. La analítica se describe en cuatro niveles: descriptiva (qué pasó), "
     "diagnóstica (por qué pasó), predictiva (qué pasará, con modelos de series de tiempo o clasificación de "
     "churn) y prescriptiva (qué hacer, combinando predicción con optimización). La segmentación de clientes "
     "con RFM o clustering permite personalizar acciones, y las pruebas A/B con un diseño estadístico correcto "
     "—tamaño de muestra calculado a priori y una métrica principal definida de antemano— evitan conclusiones "
     "espurias."),
]

SEED["filosofia"] = [
    ("Epistemología: qué podemos conocer y cómo", "epistemologia", "intermedio", "es",
     "La epistemología estudia la naturaleza, el origen y los límites del conocimiento. Platón propuso la "
     "definición clásica de conocimiento como creencia verdadera justificada, que Edmund Gettier cuestionó en "
     "1963 con casos donde alguien tiene una creencia verdadera y justificada por mera suerte. El racionalismo "
     "de Descartes, Spinoza y Leibniz sostiene que la razón es la fuente principal del conocimiento; el "
     "empirismo de Locke y Hume, que todo conocimiento procede de la experiencia. Hume planteó el problema de "
     "la inducción: ninguna cantidad de observaciones pasadas justifica lógicamente una predicción futura. "
     "Kant intentó una síntesis: los conceptos del entendimiento y las formas de la intuición (espacio y "
     "tiempo) estructuran la experiencia, de modo que conocemos los fenómenos pero no las cosas en sí. En la "
     "filosofía de la ciencia, Popper respondió a Hume con el falsacionismo y Kuhn describió el progreso "
     "científico como sucesión de paradigmas. Estas preguntas reaparecen hoy al discutir qué 'sabe' un modelo "
     "de lenguaje."),
    ("Ética: virtud, deber y consecuencias", "etica", "intermedio", "es",
     "La ética normativa ofrece tres grandes marcos para evaluar acciones. La ética de la virtud de "
     "Aristóteles pregunta qué haría una persona virtuosa: la virtud es un término medio entre extremos "
     "(el valor entre la cobardía y la temeridad) que se cultiva con el hábito y orienta la vida hacia la "
     "eudaimonía o florecimiento humano. La deontología de Kant juzga la acción por su conformidad con el "
     "deber: el imperativo categórico exige actuar solo según máximas que se puedan querer como ley universal "
     "y tratar a la humanidad siempre como fin y nunca solo como medio. El utilitarismo de Bentham y Mill "
     "evalúa por las consecuencias: es correcto lo que produce el mayor bienestar para el mayor número. Los "
     "estoicos, como Epicteto y Marco Aurelio, enseñaron a distinguir lo que depende de nosotros de lo que no. "
     "Nietzsche criticó la moral tradicional como expresión de valores históricos y no de verdades eternas. "
     "Estos marcos son la base de la ética de la inteligencia artificial actual."),
]

SEED["musica"] = [
    ("Fundamentos de teoría musical: escalas, acordes y armonía", "teoria_musical", "introductorio", "es",
     "La teoría musical describe cómo se organizan los sonidos. Una escala mayor sigue el patrón de tonos y "
     "semitonos T-T-S-T-T-T-S; la escala menor natural, T-S-T-T-S-T-T. Un acorde es la superposición de al "
     "menos tres notas: la tríada mayor se forma con la fundamental, una tercera mayor y una quinta justa, y la "
     "menor con una tercera menor. Los acordes construidos sobre cada grado de la escala tienen funciones "
     "armónicas: tónica (I), subdominante (IV) y dominante (V); la cadencia V–I genera la sensación de "
     "resolución que articula gran parte de la música tonal, y la progresión I–V–vi–IV sostiene miles de "
     "canciones populares. El ritmo organiza la música en el tiempo: el compás (4/4, 3/4, 6/8) agrupa los "
     "pulsos y el tempo fija su velocidad en pulsos por minuto. El contrapunto, perfeccionado por Bach, "
     "combina melodías independientes que suenan bien simultáneamente."),
    ("Música, física del sonido y producción digital", "produccion_musical", "intermedio", "es",
     "El sonido es una onda de presión caracterizada por su frecuencia (altura), amplitud (intensidad) y "
     "contenido armónico (timbre). En la afinación temperada de doce tonos, cada semitono multiplica la "
     "frecuencia por 2^(1/12), de modo que la octava duplica la frecuencia y el La de referencia está en 440 Hz. "
     "El timbre de una guitarra, un piano o un violín se explica por la distribución de energía en sus "
     "armónicos, que el análisis de Fourier descompone. La producción musical digital graba y edita en una "
     "estación de trabajo de audio digital (DAW), usa MIDI para representar notas como eventos con altura, "
     "velocidad y duración, y crea timbres por síntesis de sonido sustractiva, aditiva o FM. En la música "
     "latina, la salsa se organiza alrededor de la clave 3-2 o 2-3, la cumbia sobre un patrón binario de "
     "acentos en el contratiempo y el vallenato alrededor del acordeón, la caja y la guacharaca. Hoy los "
     "modelos generativos también componen música aprendiendo de secuencias de tokens de audio o MIDI."),
]
