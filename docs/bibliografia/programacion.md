# Bibliografía — Programación

> Dominio `programacion` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Structure and Interpretation of Computer Programs (2ª ed.) | H. Abelson, G. J. Sussman | 1996 | 4 | 4 | Alta | 5 | 3 |
| F2 | The Pragmatic Programmer (20th Anniversary Ed.) | D. Thomas, A. Hunt | 2019 | 2 | 5 | Alta | 5 | 1 |
| F3 | Introduction to Algorithms (4ª ed.) | T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein | 2022 | 4 | 4 | Alta | 5 | 4 |

#### F1 — *Structure and Interpretation of Computer Programs* (SICP)
- **Cobertura conceptual:** abstracción procedimental, recursión, tipos de datos, secuencias, streams, intérpretes, metalingüística.
- **Cobertura práctica:** pensar computacionalmente desde primeros principios; construir intérpretes y compiladores básicos.
- **Valor como guía para el LLM:** texto fundacional de ciencias de la computación; guía del registro "pensamiento computacional profundo".
- **Conocimiento que aporta:** los fundamentos conceptuales de la programación: abstracción, composición, evaluación, continuaciones.
- **Vocabulario técnico:** *abstracción*, *clausura*, *entorno léxico*, *continuación*, *streams*, *macros*, *evaluador metacircular*.
- **Razonamiento que aporta:** razonamiento sobre evaluación de programas, construcción inductiva de abstracciones, análisis de complejidad recursiva.

#### F2 — *The Pragmatic Programmer*
- **Cobertura conceptual:** filosofía del programador profesional: DRY, ortogonalidad, automatización, testing, equipos, carrera.
- **Cobertura práctica:** hábitos y prácticas para escribir código más mantenible, robusto y profesional.
- **Valor como guía para el LLM:** vocabulario de ingeniería de software profesional; guía del registro "best practices".
- **Conocimiento que aporta:** la filosofía pragmática del desarrollo de software — principios que trascienden lenguajes y tecnologías.
- **Vocabulario técnico:** *DRY*, *código ortogonal*, *acoplamiento temporal*, *programming by coincidence*, *broken windows*, *rubber ducking*.
- **Razonamiento que aporta:** razonamiento sobre calidad de código, decisiones de diseño pragmáticas, gestión de deuda técnica.

#### F3 — *Introduction to Algorithms* (CLRS)
- **Cobertura conceptual:** algoritmos de ordenamiento, estructuras de datos, grafos, programación dinámica, algoritmos voraces, NP-completitud.
- **Cobertura práctica:** implementar y analizar algoritmos fundamentales; base de entrevistas técnicas y diseño de sistemas.
- **Valor como guía para el LLM:** el texto de referencia de algoritmos; notación y razonamiento que aparecen en papers de sistemas y ML.
- **Conocimiento que aporta:** el arsenal completo de algoritmos y estructuras de datos que usa todo ingeniero de software.
- **Vocabulario técnico:** *complejidad temporal/espacial*, *O grande*, *árbol AVL*, *tabla hash*, *BFS/DFS*, *relajación*, *subestructura óptima*, *corte mínimo*.
- **Razonamiento que aporta:** análisis de complejidad, demostración de correctitud, diseño por inducción.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Clean Code | R. C. Martin | 2008 | 2 | 5 | Alta | 4 | 1 |
| A2 | Refactoring (2ª ed.) | M. Fowler | 2018 | 3 | 4 | Media | 5 | 1 |
| A3 | Programming Language Pragmatics (4ª ed.) | M. L. Scott | 2015 | 5 | 3 | Baja | 5 | 3 |

#### A1 — *Clean Code*
- **Cobertura conceptual:** nombres significativos, funciones pequeñas, comentarios, formato, objetos vs. estructuras, manejo de errores, testing.
- **Cobertura práctica:** refactorizar código real para hacerlo más limpio y mantenible.
- **Valor como guía para el LLM:** el vocabulario de "código limpio" más citado en la industria; guía del registro de revisión de código.
- **Conocimiento que aporta:** los principios de codificación limpia que dominan la cultura de ingeniería de software moderna.
- **Vocabulario técnico:** *magic number*, *función pura*, *side effect*, *cohesión*, *acoplamiento*, *test unitario*, *SRP*, *función de un nivel de abstracción*.
- **Razonamiento que aporta:** razonamiento sobre legibilidad, decisiones de naming, diseño de funciones.

#### A2 — *Refactoring*
- **Cobertura conceptual:** catálogo de refactorizaciones: Extract Method, Move Field, Replace Conditional with Polymorphism, etc.
- **Cobertura práctica:** mejorar código existente sin cambiar su comportamiento; usar tests para guiar el proceso.
- **Valor como guía para el LLM:** catálogo canónico de técnicas de refactorización con código Java/JavaScript antes-después.
- **Conocimiento que aporta:** el vocabulario de transformaciones de código que usa cualquier desarrollador profesional.
- **Vocabulario técnico:** *code smell*, *Extract Method/Variable*, *Rename*, *Pull Up Method*, *Replace Conditional with Strategy*, *Decompose Conditional*.
- **Razonamiento que aporta:** identificación de code smells, elección de refactorización apropiada, razonamiento sobre diseño emergente.

#### A3 — *Programming Language Pragmatics*
- **Cobertura conceptual:** compiladores, intérpretes, sistemas de tipos, concurrencia, paradigmas: funcional, lógico, orientado a objetos.
- **Cobertura práctica:** entender cómo funcionan los lenguajes que se usan; base para diseño de DSLs y analizadores léxicos.
- **Valor como guía para el LLM:** el texto de lenguajes de programación más completo — cubre análisis léxico (lexers) y parsers.
- **Conocimiento que aporta:** los fundamentos de lenguajes de programación (el análisis léxico clásico es distinto del tokenizador BPE estadístico del repo).
- **Vocabulario técnico:** *lexer*, *parser*, *AST*, *type inference*, *garbage collection*, *coroutine*, *continuation*, *closure*.
- **Razonamiento que aporta:** razonamiento sobre semántica de lenguajes, diseño de sistemas de tipos, análisis de programas.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | The Art of Computer Programming (Vol 1-4, selección) | D. E. Knuth | 1968–2011 | 5 | 3 | Baja | 5 | 5 |
| P2 | Code Complete (2ª ed.) | S. McConnell | 2004 | 2 | 4 | Media | 5 | 1 |
| P3 | Competitive Programmer's Handbook | A. Laaksonen | 2017 | 3 | 3 | Baja | 4 | 3 |

#### P1 — *The Art of Computer Programming*
- **Cobertura conceptual:** algoritmos fundamentales, estructuras de datos, generación de números aleatorios, ordenamiento, búsqueda, aritmética seminumérica.
- **Cobertura práctica:** el nivel más profundo de comprensión algorítmica disponible.
- **Valor como guía para el LLM:** la obra monumental de la programación; aporta texto técnico de máxima densidad y rigor.
- **Conocimiento que aporta:** el análisis algorítmico más profundo disponible; cubre temas que ningún otro texto aborda con igual rigor.
- **Vocabulario técnico:** *análisis de algoritmos*, *recurrencias*, *generación de permutaciones*, *análisis amortizado*, *notación O, Ω, Θ*, *MIX assembly*.
- **Razonamiento que aporta:** análisis matemático profundo de algoritmos; razonamiento combinatorio y probabilístico.

#### P2 — *Code Complete*
- **Cobertura conceptual:** diseño de software, construcción de código, variables, sentencias, módulos, colaboración, testing, rendimiento.
- **Cobertura práctica:** la enciclopedia de buenas prácticas de construcción de software.
- **Valor como guía para el LLM:** amplia cobertura del proceso completo de construcción de software con ejemplos y evidencia empírica.
- **Conocimiento que aporta:** las prácticas de ingeniería de software respaldadas por evidencia; complementa a Clean Code con mayor amplitud.
- **Vocabulario técnico:** *pseudocódigo*, *tabla de verdad*, *complejidad ciclomática*, *acoplamiento aferente/eferente*, *cohesión funcional*.
- **Razonamiento que aporta:** decisiones de diseño respaldadas por datos, medición de calidad de código, gestión de complejidad.

#### P3 — *Competitive Programmer's Handbook*
- **Cobertura conceptual:** algoritmos de competencia: grafos, DP, teoría de números, geometría, estructuras de datos avanzadas.
- **Cobertura práctica:** resolver problemas algorítmicos complejos con eficiencia; preparación para entrevistas FAANG.
- **Valor como guía para el LLM:** disponible libremente; código C++ idiomático con explicaciones concisas y muchos problemas tipo LeetCode.
- **Conocimiento que aporta:** el nivel avanzado de algoritmos y estructuras de datos para ingenieros de software de alto rendimiento.
- **Vocabulario técnico:** *segment tree*, *fenwick tree*, *strongly connected component*, *max flow*, *min cut*, *Dijkstra*, *Bellman-Ford*.
- **Razonamiento que aporta:** razonamiento algorítmico preciso, optimización de soluciones, análisis de casos límite.

## Papers importantes

- Dijkstra, E. W. — *A Note on Two Problems in Connexion with Graphs* (Numerische Mathematik, 1959).
- Hoare, C. A. R. — *Quicksort* (Computer Journal, 1962).
- Backus, J. — *Can Programming Be Liberated from the Von Neumann Style?* (ACM Turing Award, 1978).
- Liskov, B. — *Data Abstraction and Hierarchy* (OOPSLA 1987). [ACM link](https://dl.acm.org/doi/10.1145/62139.62141)
- Lamport, L. — *Paxos Made Simple* (2001). [Link](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)

## Documentación oficial

- [Python Language Reference](https://docs.python.org/3/reference/) — PSF License; documentación del lenguaje.
- [MDN Web Docs](https://developer.mozilla.org/) — CC BY-SA 2.5; referencia web y JavaScript.
- [GNU C Library manual](https://www.gnu.org/software/libc/manual/) — LGPL; referencia de C estándar.
- [Stack Overflow](https://stackoverflow.com/) — preguntas y respuestas de programación (CC BY-SA 4.0).

## Blogs técnicos

- [Joel on Software (J. Spolsky)](https://www.joelonsoftware.com/) — reflexiones clásicas sobre ingeniería de software.
- [Paul Graham — Essays](http://www.paulgraham.com/articles.html) — programación y startups con pensamiento profundo.
- [Martin Fowler — Blog](https://martinfowler.com/bliki/) — patrones de diseño y arquitectura de software.
- [High Scalability](http://highscalability.com/) — casos reales de sistemas de alta escala.
- [dev.to](https://dev.to/) — artículos técnicos de la comunidad (copyright de cada autor — verificar licencia).

## Repositorios GitHub

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) — implementaciones de algoritmos en Python (MIT).
- [kdn251/interviews](https://github.com/kdn251/interviews) — recursos para entrevistas técnicas.
- [donnemartin/interactive-coding-challenges](https://github.com/donnemartin/interactive-coding-challenges) — retos interactivos (Apache-2.0).
- [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) — roadmap de ingeniería de software (verificar licencia).
- [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) — algoritmos con JavaScript (MIT).

## Benchmarks

- **LeetCode** — plataforma de problemas algorítmicos; soluciones en múltiples lenguajes.
- **HackerRank** — evaluaciones de programación por dominio.
- Para evaluar el LLM: **HumanEval** (OpenAI) y **MBPP** — generación de código Python.
- **CodeContests** — competencias de programación competitiva.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| Stack Overflow dump | CC BY-SA 4.0 | Q&A de programación (candidata, no ingerida) |
| GitHub Code (The Stack) | Apache-2.0 (para código permisivo) | Código fuente de GitHub — verificar por lenguaje |
| CodeSearchNet | CC BY 4.0 | Pares función-documentación en 6 lenguajes |
| HumanEval | MIT | 164 problemas de programación con pruebas |
| MBPP (Mostly Basic Programming Problems) | CC BY 4.0 | 1000 problemas Python con soluciones |
