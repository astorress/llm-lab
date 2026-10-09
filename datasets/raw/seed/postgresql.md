# Corpus semilla — dominio: postgresql

## Índices B-tree y planificación de consultas
<!-- subcategoria: rendimiento | dificultad: intermedio | idioma: es -->
PostgreSQL crea por defecto índices B-tree, eficientes para búsquedas por igualdad y rango en O(log n). Un índice acelera las lecturas pero ralentiza las escrituras y ocupa espacio, por lo que se crean selectivamente sobre columnas usadas en WHERE, JOIN y ORDER BY. El planificador de consultas estima el costo de planes alternativos (escaneo secuencial vs. por índice) usando estadísticas de la tabla; EXPLAIN ANALYZE muestra el plan elegido y los tiempos reales. Otros tipos de índice: GIN para búsqueda de texto completo y arrays, GiST para datos geométricos, y BRIN para tablas grandes con correlación física.

## Transacciones ACID y control de concurrencia MVCC
<!-- subcategoria: transacciones | dificultad: avanzado | idioma: es -->
PostgreSQL garantiza las propiedades ACID: atomicidad (todo o nada), consistencia, aislamiento y durabilidad. La durabilidad se logra con el Write-Ahead Log (WAL): los cambios se registran antes de aplicarse a los datos. El aislamiento se implementa con control de concurrencia multiversión (MVCC): cada transacción ve una instantánea consistente de los datos sin bloquear a los lectores, ya que las actualizaciones crean nuevas versiones de las filas en lugar de sobrescribirlas. Los niveles de aislamiento (read committed, repeatable read, serializable) equilibran consistencia y concurrencia, previniendo fenómenos como lecturas sucias o fantasma.
