# Corpus semilla — dominio: ciencia_datos

## El proceso de ciencia de datos y EDA
<!-- subcategoria: metodologia | dificultad: introductorio | idioma: es -->
Un proyecto de ciencia de datos sigue un ciclo: definición del problema, obtención y limpieza de datos, análisis exploratorio (EDA), modelado, evaluación y comunicación. El EDA examina distribuciones, correlaciones, valores faltantes y atípicos antes de modelar, usando estadística descriptiva y visualización (histogramas, boxplots, scatter, mapas de calor de correlación). La limpieza —imputación de faltantes, codificación de categóricas, escalado de numéricas— suele consumir la mayor parte del tiempo. La calidad de las características (feature engineering) impacta el rendimiento más que la elección del algoritmo en muchos problemas tabulares.

## Pandas: manipulación de datos tabulares
<!-- subcategoria: herramientas | dificultad: intermedio | idioma: es -->
Pandas es la librería estándar de Python para datos tabulares. Su estructura central, el DataFrame, es una tabla bidimensional con índices etiquetados. Operaciones clave: filtrado booleano (df[df.x > 0]), agregación con groupby (df.groupby('dominio').size()), combinación con merge y concat, y reformateo con pivot y melt. El método apply aplica funciones por fila o columna, aunque las operaciones vectorizadas son mucho más rápidas. Para datos grandes, formatos columnar como Parquet y herramientas como Polars o Dask superan a Pandas en memoria y velocidad.
