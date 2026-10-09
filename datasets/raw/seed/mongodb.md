# Corpus semilla — dominio: mongodb

## Modelo de documentos y diseño de esquema
<!-- subcategoria: modelado | dificultad: intermedio | idioma: es -->
MongoDB es una base de datos NoSQL orientada a documentos: almacena registros como documentos BSON (JSON binario) flexibles, agrupados en colecciones. A diferencia del modelo relacional normalizado, MongoDB favorece la desnormalización y el embebido de datos relacionados en un solo documento cuando se leen juntos, evitando JOINs. La regla práctica: 'los datos que se acceden juntos se almacenan juntos'. Para relaciones uno-a-muchos de alta cardinalidad o datos compartidos se usan referencias. El diseño del esquema se guía por los patrones de consulta de la aplicación, no por la estructura de los datos en sí.

## El pipeline de agregación
<!-- subcategoria: consultas | dificultad: intermedio | idioma: es -->
El framework de agregación de MongoDB procesa documentos a través de una secuencia de etapas (un pipeline), cada una transformando el flujo. Etapas comunes: $match filtra (como WHERE), $group agrupa y agrega (como GROUP BY con sum, avg, count), $project remodela los campos, $sort ordena, $lookup hace una unión con otra colección, y $unwind descompone arrays. El orden importa para el rendimiento: filtrar con $match temprano reduce los documentos procesados aguas abajo. Es el equivalente analítico de las consultas SQL complejas, ejecutado del lado del servidor.
