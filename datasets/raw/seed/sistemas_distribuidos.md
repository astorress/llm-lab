# Corpus semilla — dominio: sistemas_distribuidos

## El teorema CAP y la consistencia
<!-- subcategoria: teoria | dificultad: avanzado | idioma: es -->
El teorema CAP establece que un sistema distribuido no puede garantizar simultáneamente las tres propiedades: consistencia (todos los nodos ven los mismos datos a la vez), disponibilidad (toda petición recibe respuesta) y tolerancia a particiones (el sistema sigue operando pese a fallos de red). Como las particiones son inevitables en la práctica, el diseño elige entre consistencia (CP) y disponibilidad (AP) ante una partición. Esto se refina con modelos de consistencia: la linealizabilidad (la más fuerte) hace que las operaciones parezcan instantáneas y ordenadas, mientras que la consistencia eventual solo garantiza convergencia con el tiempo, ofreciendo mayor disponibilidad y menor latencia.

## Consenso distribuido: Raft
<!-- subcategoria: consenso | dificultad: avanzado | idioma: es -->
El consenso permite que un conjunto de nodos acuerde un valor pese a fallos, base de la replicación consistente. Raft es un algoritmo de consenso diseñado para ser comprensible. Elige un líder que recibe todas las escrituras de los clientes y las replica como entradas de un log a los seguidores; una entrada se considera comprometida (committed) cuando una mayoría la ha replicado. Si el líder falla, los seguidores detectan la ausencia de latidos y, tras un timeout aleatorizado, inician una elección por términos votando por un nuevo líder. Raft separa el problema en elección de líder, replicación de log y seguridad, garantizando que los logs comprometidos nunca se pierden.
