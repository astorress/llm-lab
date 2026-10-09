# Bibliografía — Python

> Dominio `python` · peso 1.2 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Fluent Python (2ª ed.) | L. Ramalho | 2022 | 3 | 5 | Alta | 5 | 2 |
| F2 | Python Cookbook (3ª ed.) | D. Beazley, B. K. Jones | 2013 | 3 | 4 | Alta | 5 | 2 |
| F3 | Learning Python (5ª ed.) | M. Lutz | 2013 | 2 | 4 | Alta | 4 | 2 |

#### F1 — *Fluent Python*
- **Cobertura conceptual:** modelo de datos de Python, secuencias, dicts/sets, funciones como objetos, decoradores, generadores, concurrencia, metaprogramación.
- **Cobertura práctica:** escribir Python verdaderamente idiomático; entender el protocolo dunder y cómo lo usa el intérprete.
- **Valor como guía para el LLM:** el texto de referencia para Python avanzado idiomático; la densidad de patrones de uso correcto es excepcional.
- **Conocimiento que aporta:** Python profundo: cómo el intérprete ejecuta el código, los protocolos de secuencia, iteración y contexto.
- **Vocabulario técnico:** *dunder methods*, *descriptor*, *generator*, *context manager*, *decorator*, *coroutine*, *dataclass*, *metaclass*.
- **Razonamiento que aporta:** diseño de clases Python idiomáticas, uso correcto de los protocolos del lenguaje, debugging de código avanzado.

#### F2 — *Python Cookbook*
- **Cobertura conceptual:** recetas para estructuras de datos, algoritmos, strings, archivos, funciones, clases, metaprogramación, redes, concurrencia.
- **Cobertura práctica:** soluciones a problemas Python reales organizadas como recetas; referencia en el trabajo diario.
- **Valor como guía para el LLM:** alta densidad de soluciones Python idiomáticas con explicaciones — el formato "problema-solución-discusión" es valioso.
- **Conocimiento que aporta:** el conocimiento tácito del experto Python: cómo se resuelven problemas reales con las herramientas del lenguaje.
- **Vocabulario técnico:** *collections.Counter*, *defaultdict*, *heapq*, *functools.partial*, *itertools*, *contextlib*, *threading.local*.
- **Razonamiento que aporta:** elección de la solución más Pythónica para un problema dado; análisis de trade-offs entre alternativas.

#### F3 — *Learning Python*
- **Cobertura conceptual:** tipos de datos, sentencias, funciones, módulos, OOP, excepciones, herramientas avanzadas — cobertura completa del lenguaje.
- **Cobertura práctica:** el manual de referencia más completo del lenguaje; cubre todos los aspectos con detalle.
- **Valor como guía para el LLM:** cobertura enciclopédica del lenguaje con ejemplos en cada sección; ideal para texto de nivel intermedio.
- **Conocimiento que aporta:** la cobertura completa del lenguaje Python que ningún otro libro iguala en profundidad.
- **Vocabulario técnico:** *scope LEGB*, *MRO*, *property*, *class method*, *static method*, *slots*, *pickling*, *bytecode*.
- **Razonamiento que aporta:** resolución de problemas de scope, herencia múltiple, depuración de errores comunes.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Python in a Nutshell (4ª ed.) | A. Martelli, A. Martelli Ravenscroft, S. Holden, P. McGuire | 2023 | 3 | 4 | Media | 5 | 2 |
| A2 | High Performance Python (2ª ed.) | M. Gorelick, I. Ozsvald | 2020 | 4 | 5 | Alta | 5 | 3 |
| A3 | CPython Internals | A. Shaw | 2021 | 5 | 4 | Media | 5 | 3 |

#### A1 — *Python in a Nutshell*
- **Cobertura conceptual:** referencia rápida del lenguaje: tipos, sentencias, funciones, clases, I/O, redes — actualizada a Python 3.11+.
- **Cobertura práctica:** referencia de escritorio para uso diario; complementa a Fluent Python con cobertura de stdlib.
- **Valor como guía para el LLM:** referencia concisa y precisa; alta densidad de información por página.
- **Conocimiento que aporta:** la cobertura actualizada del lenguaje y la stdlib estándar de Python moderno.
- **Vocabulario técnico:** *typing module*, *asyncio*, *dataclasses*, *pathlib*, *match-case*, *walrus operator*, *type hints*.
- **Razonamiento que aporta:** elección de la herramienta correcta de la stdlib, uso de tipos para documentar intenciones.

#### A2 — *High Performance Python*
- **Cobertura conceptual:** profiling, estructuras de datos eficientes, NumPy, Cython, compilación JIT (Numba), concurrencia, multiprocessing, asyncio.
- **Cobertura práctica:** optimizar código Python real: identificar cuellos de botella y aplicar la solución correcta.
- **Valor como guía para el LLM:** vocabulario de performance Python directamente relevante para entrenar redes neuronales eficientemente.
- **Conocimiento que aporta:** las técnicas de optimización de Python que el repo necesita para el loop de entrenamiento y el pipeline de datos.
- **Vocabulario técnico:** *profiling*, *GIL*, *memory view*, *ctype*, *Numba JIT*, *zero-copy*, *asyncio event loop*, *multiprocessing.Pool*.
- **Razonamiento que aporta:** diagnóstico de cuellos de botella, elección de técnica de optimización según el tipo de problema.

#### A3 — *CPython Internals*
- **Cobertura conceptual:** arquitectura de CPython: bytecode, evaluación, memoria, GC, C extensions, compilación.
- **Cobertura práctica:** entender cómo Python ejecuta código; base para debugging profundo y escritura de extensiones C.
- **Valor como guía para el LLM:** el registro más técnico del dominio Python; conecta el lenguaje con la implementación de referencia.
- **Conocimiento que aporta:** el nivel de comprensión del intérprete que diferencia a los expertos Python de los practicantes intermedios.
- **Vocabulario técnico:** *bytecode*, *frame object*, *reference counting*, *GC cycle detector*, *PyObject*, *C extension*, *eval loop*.
- **Razonamiento que aporta:** razonamiento sobre rendimiento a nivel de intérprete, debugging de memory leaks, diseño de extensiones.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Python Testing with pytest (2ª ed.) | B. Okken | 2022 | 2 | 4 | Media | 5 | 1 |
| P2 | Automate the Boring Stuff with Python (2ª ed.) | A. Sweigart | 2019 | 1 | 3 | Baja | 4 | 1 |
| P3 | Python for DevOps | N. Gift, K. Behrman, A. Deza, G. Gheorghiu | 2020 | 2 | 4 | Media | 4 | 1 |

#### P1 — *Python Testing with pytest*
- **Cobertura conceptual:** pytest: fixtures, parametrize, markers, plugins, cobertura de código, mocking, TDD.
- **Cobertura práctica:** escribir tests profesionales en Python; el testing de referencia del ecosistema Python.
- **Valor como guía para el LLM:** vocabulario de testing Python idiomático con código antes-después; guía para temas de calidad de software.
- **Conocimiento que aporta:** el estándar de facto de testing en Python; cómo los proyectos de código abierto verifican su corrección.
- **Vocabulario técnico:** *fixture*, *scope*, *parametrize*, *monkeypatch*, *capfd*, *conftest.py*, *mark.skip*, *coverage*.
- **Razonamiento que aporta:** diseño de tests independientes y reproducibles, estrategias de test para código ML.

#### P2 — *Automate the Boring Stuff*
- **Cobertura conceptual:** Python aplicado a tareas de automatización: archivos, Excel, PDFs, web scraping, emails, programación de tareas.
- **Cobertura práctica:** el libro de Python más leído en internet; disponible gratis online.
- **Valor como guía para el LLM:** registro introductorio y muy práctico; el tono "Python para resolver problemas reales" es una buena guía de estilo.
- **Conocimiento que aporta:** el Python de automatización que usan millones de personas; cobertura del nivel introductorio del dominio.
- **Vocabulario técnico:** *shutil*, *os.walk*, *re.compile*, *requests*, *BeautifulSoup*, *openpyxl*, *smtplib*, *schedule*.
- **Razonamiento que aporta:** descomposición de tareas de automatización, manejo de errores en scripts prácticos.

#### P3 — *Python for DevOps*
- **Cobertura conceptual:** Python en operaciones: bash scripting con Python, cloud automation, serverless, CI/CD, monitoreo, MLOps.
- **Cobertura práctica:** usar Python para automatizar infraestructura — alineado con la Etapa 2 (automatización de infraestructura).
- **Valor como guía para el LLM:** el vocabulario de operaciones y DevOps en Python; conecta el lenguaje con el stack de infraestructura.
- **Conocimiento que aporta:** Python como pegamento de sistemas: boto3, subprocess, paramiko, click — el Python de la infraestructura.
- **Vocabulario técnico:** *boto3*, *click*, *subprocess*, *paramiko*, *fabric*, *invoke*, *fire*, *typer*, *pydantic*.
- **Razonamiento que aporta:** diseño de CLIs, automatización de tareas de operaciones, interacción con APIs de cloud.

## Papers importantes

- Van Rossum, G. & Drake, F. L. — *Python Reference Manual* (Python Software Foundation, actualizado continuamente).
- Pedregosa, F. et al. — *Scikit-learn: Machine Learning in Python* (JMLR 2011). [arXiv:1201.0490](https://arxiv.org/abs/1201.0490)
- McKinney, W. — *Data Structures for Statistical Computing in Python* (SciPy 2010). [Link](https://conference.scipy.org/proceedings/scipy2010/pdfs/mckinney.pdf)
- Behnel, S. et al. — *Cython: The Best of Both Worlds* (Computing in Science & Engineering, 2011).

## Documentación oficial

- [Python official documentation](https://docs.python.org/3/) — PSF License; la referencia completa del lenguaje.
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/) — diseño del lenguaje; PEP 8, 20, 257, 484.
- [Real Python tutorials](https://realpython.com/) — artículos técnicos (copyright de Real Python — verificar licencia).
- [Python Packaging User Guide](https://packaging.python.org/) — PyPA; gestión de paquetes.

## Blogs técnicos

- [Real Python](https://realpython.com/) — tutoriales de alta calidad del ecosistema Python.
- [Brett Cannon — blog](https://snarky.ca/) — core developer de CPython; internals y diseño del lenguaje.
- [Armin Ronacher — blog](https://lucumr.pocoo.org/) — creador de Flask y Jinja2; Python avanzado.
- [Python Bytes podcast](https://pythonbytes.fm/) — novedades del ecosistema Python.
- [Mouse vs Python (M. Driscoll)](https://www.blog.pythonlibrary.org/) — tutoriales prácticos.

## Repositorios GitHub

- [python/cpython](https://github.com/python/cpython) — implementación de referencia (PSF License).
- [psf/black](https://github.com/psf/black) — formateador de código estándar (MIT).
- [astral-sh/ruff](https://github.com/astral-sh/ruff) — linter ultrarrápido (MIT).
- [pydantic/pydantic](https://github.com/pydantic/pydantic) — validación de datos con type hints (MIT).
- [encode/httpx](https://github.com/encode/httpx) — cliente HTTP moderno (BSD-3).

## Benchmarks

- **Python benchmark suite (pyperformance)** — benchmarks oficiales de CPython.
- **HumanEval** — evaluación de generación de código Python para LLMs (MIT).
- **MBPP** — problemas básicos de Python para evaluación de LLMs (CC BY 4.0).
- Para evaluar el LLM: repositorios de ejercicios públicos de Python (Exercism, Codewars).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| The Stack (Python subset) | Apache-2.0 y similares | Código Python de GitHub con licencias permisivas |
| CodeSearchNet (Python) | CC BY 4.0 | Pares función-docstring para Python |
| HumanEval | MIT | 164 problemas de programación Python con pruebas |
| PyPI metadata | Varía por paquete | Metadatos, READMEs y changelogs de paquetes Python |
| Rosetta Code (Python) | GNU FDL | Implementaciones del mismo algoritmo en muchos lenguajes |
