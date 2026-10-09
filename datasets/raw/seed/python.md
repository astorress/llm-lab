# Corpus semilla — dominio: python

## Generadores e iteradores perezosos
<!-- subcategoria: lenguaje | dificultad: intermedio | idioma: es -->
Un generador en Python es una función que usa yield para producir valores uno a uno, manteniendo su estado entre llamadas. A diferencia de una lista, no materializa todos los valores en memoria, lo que permite procesar secuencias enormes o infinitas con consumo constante. Las expresiones generadoras (x*x for x in range(n)) son su forma compacta. El protocolo de iteración (__iter__ y __next__) sustenta los bucles for. Combinados con itertools, los generadores permiten construir pipelines de datos eficientes y componibles, fundamentales para el streaming de corpus en entrenamiento de LLMs.

## Decoradores y funciones de orden superior
<!-- subcategoria: lenguaje | dificultad: intermedio | idioma: es -->
Un decorador es una función que recibe otra función y devuelve una versión modificada, aprovechando que en Python las funciones son objetos de primera clase. La sintaxis @decorador antepuesta a una definición es azúcar para func = decorador(func). Se usan para añadir comportamiento transversal sin modificar el cuerpo: logging, medición de tiempo, caché (@functools.lru_cache), validación o registro. functools.wraps preserva los metadatos de la función original. Los decoradores con argumentos requieren un nivel adicional de anidamiento de funciones.

## Type hints y tipado gradual
<!-- subcategoria: lenguaje | dificultad: intermedio | idioma: es -->
Las anotaciones de tipo (type hints, PEP 484) permiten declarar los tipos esperados de variables, parámetros y retornos sin afectar la ejecución: Python sigue siendo de tipado dinámico. Herramientas como mypy o pyright verifican estáticamente la consistencia de tipos, detectando errores antes de ejecutar. El módulo typing aporta genéricos (list[int], dict[str, float]), uniones (int | None), Protocol para tipado estructural y TypeVar para genéricos. El tipado gradual mejora la mantenibilidad y la autocompletación en bases de código grandes.
