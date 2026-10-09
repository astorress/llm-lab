# Corpus semilla — dominio: data_engineering

## Pipelines ETL/ELT y orquestación
<!-- subcategoria: pipelines | dificultad: intermedio | idioma: es -->
Un pipeline de datos mueve y transforma datos desde las fuentes hasta su destino analítico. ETL (extraer, transformar, cargar) transforma antes de cargar; ELT carga datos crudos en un almacén o lago y los transforma allí, aprovechando la potencia del destino (patrón dominante con la nube y herramientas como dbt). La orquestación (Airflow, Dagster) modela el pipeline como un grafo acíclico dirigido (DAG) de tareas con dependencias, programación, reintentos y backfills. Principios clave: idempotencia (re-ejecutar produce el mismo resultado), particionamiento por fecha y validación de calidad de datos en cada etapa.

## Formatos columnar: Parquet y Arrow
<!-- subcategoria: almacenamiento | dificultad: intermedio | idioma: es -->
Los formatos columnar almacenan los datos por columna en lugar de por fila, lo que beneficia a las cargas analíticas: solo se leen las columnas necesarias y la compresión es muy eficiente al agrupar valores del mismo tipo. Apache Parquet es el formato de archivo columnar estándar para almacenamiento, con compresión y esquema embebido. Apache Arrow define un formato columnar en memoria que permite intercambiar datos entre sistemas sin serialización y procesarlos de forma vectorizada. En este laboratorio, el corpus se guarda en Parquet por su compresión (5-10x menor que JSONL) y en Arrow para iterar datasets mayores que la RAM mediante memory-mapping.
