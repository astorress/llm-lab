# Corpus semilla — dominio: aws

## AWS Lambda y el cómputo serverless
<!-- subcategoria: computo | dificultad: intermedio | idioma: es -->
AWS Lambda ejecuta código en respuesta a eventos sin que el desarrollador gestione servidores. Se factura por número de invocaciones y por la duración de ejecución (en milisegundos) multiplicada por la memoria asignada. Escala automáticamente de cero a miles de ejecuciones concurrentes. Es ideal para APIs (con API Gateway), procesamiento de eventos (S3, DynamoDB Streams, SQS) y tareas programadas. Limitaciones a considerar: tiempo máximo de ejecución (15 minutos), arranques en frío (latencia al inicializar un contenedor nuevo) y tamaño del paquete de despliegue. El modelo de concurrencia y los timeouts deben dimensionarse según la carga.

## Almacenamiento S3 y clases de almacenamiento
<!-- subcategoria: almacenamiento | dificultad: introductorio | idioma: es -->
Amazon S3 (Simple Storage Service) ofrece almacenamiento de objetos altamente durable (99,999999999% de durabilidad) y escalable prácticamente sin límite. Los objetos se organizan en buckets con claves únicas. Las clases de almacenamiento optimizan el costo según el patrón de acceso: S3 Standard para datos de acceso frecuente, S3 Intelligent-Tiering que mueve objetos automáticamente, S3 Standard-IA y One Zone-IA para acceso infrecuente, y Glacier para archivado a largo plazo con recuperación más lenta y barata. Las políticas de ciclo de vida automatizan la transición entre clases para reducir costos.
