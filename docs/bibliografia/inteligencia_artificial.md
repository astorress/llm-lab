# Bibliografía — Inteligencia Artificial

> Dominio `inteligencia_artificial` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Artificial Intelligence: A Modern Approach (4ª ed.) | S. Russell, P. Norvig | 2020 | 3 | 5 | Alta | 5 | 3 |
| F2 | Artificial Intelligence: A Guide for Thinking Humans | M. Mitchell | 2019 | 1 | 4 | Alta | 5 | 1 |
| F3 | Human Compatible: Artificial Intelligence and the Problem of Control | S. Russell | 2019 | 2 | 4 | Media | 5 | 1 |

#### F1 — *Artificial Intelligence: A Modern Approach*
- **Cobertura conceptual:** búsqueda, planificación, representación del conocimiento, razonamiento bajo incertidumbre, aprendizaje, percepción, NLP, robótica.
- **Cobertura práctica:** implementar agentes de búsqueda, CSPs, lógica proposicional, redes bayesianas y aprendizaje por refuerzo básico.
- **Valor como guía para el LLM:** el texto de referencia más citado en IA; cubre el espectro completo con vocabulario canónico del campo.
- **Conocimiento que aporta:** la arquitectura conceptual completa de la IA: desde sistemas basados en reglas hasta aprendizaje.
- **Vocabulario técnico:** *agente racional*, *PEAS*, *búsqueda heurística*, *A\**, *CSP*, *inferencia bayesiana*, *MDP*, *policy*, *utility function*.
- **Razonamiento que aporta:** formulación de problemas como problemas de búsqueda o decisión; análisis de optimalidad y completitud.

#### F2 — *Artificial Intelligence: A Guide for Thinking Humans*
- **Cobertura conceptual:** historia de la IA, ML, visión, NLP, redes neuronales; crítica de las afirmaciones exageradas del campo.
- **Cobertura práctica:** contextualizar desarrollos recientes con rigor histórico y crítico.
- **Valor como guía para el LLM:** prosa accesible de alta calidad que contextualiza el dominio; aporta el registro "divulgación rigurosa".
- **Conocimiento que aporta:** la historia y el contexto del campo que los textos técnicos omiten; fundamental para razonar sobre limitaciones.
- **Vocabulario técnico:** *deep learning*, *inductive bias*, *brittleness*, *bias in AI*, *transfer learning*, *Turing test*, *narrow AI*.
- **Razonamiento que aporta:** pensamiento crítico sobre afirmaciones del campo; analogías y límites conceptuales de los sistemas actuales.

#### F3 — *Human Compatible*
- **Cobertura conceptual:** el problema del control en IA, alineación, incertidumbre de preferencias, IRL (Inverse Reinforcement Learning).
- **Cobertura práctica:** pensar sobre diseño de sistemas de IA con objetivos humanos incompletos o ambiguos.
- **Valor como guía para el LLM:** vocabulario de alineación y seguridad en IA, área transversal cada vez más citada en papers técnicos.
- **Conocimiento que aporta:** el marco teórico para entender el problema de la alineación; conecta con RL, teoría de juegos y ética.
- **Vocabulario técnico:** *value alignment*, *inverse reinforcement learning*, *corrigibility*, *AI safety*, *reward misspecification*, *CIRL*.
- **Razonamiento que aporta:** análisis de consecuencias no previstas de objetivos mal especificados; razonamiento bajo incertidumbre de valores.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Reinforcement Learning: An Introduction (2ª ed.) | R. Sutton, A. Barto | 2018 | 4 | 5 | Alta | 5 | 4 |
| A2 | Probabilistic Graphical Models | D. Koller, N. Friedman | 2009 | 5 | 4 | Media | 5 | 5 |
| A3 | Planning Algorithms | S. M. LaValle | 2006 | 5 | 3 | Baja | 5 | 5 |

#### A1 — *Reinforcement Learning: An Introduction*
- **Cobertura conceptual:** MDPs, métodos tabulares (Q-learning, SARSA, TD), función de valor, aproximación de funciones, policy gradients.
- **Cobertura práctica:** implementar agentes RL desde cero; entender el fundamento teórico de algoritmos como PPO y RLHF.
- **Valor como guía para el LLM:** texto fundamental para comprender RLHF (usado en el fine-tuning de LLMs modernos); notación canónica.
- **Conocimiento que aporta:** el marco teórico completo del aprendizaje por refuerzo que subyace a RLHF y alineación.
- **Vocabulario técnico:** *return*, *discount factor*, *Bellman equation*, *policy gradient*, *on-policy*, *off-policy*, *exploration-exploitation*.
- **Razonamiento que aporta:** derivación de convergencia de algoritmos, análisis de trade-offs exploración-explotación.

#### A2 — *Probabilistic Graphical Models*
- **Cobertura conceptual:** redes bayesianas, modelos de Markov, inferencia exacta/aproximada, aprendizaje de parámetros y estructura.
- **Cobertura práctica:** modelar incertidumbre en dominios complejos; base para entender variational autoencoders y modelos generativos.
- **Valor como guía para el LLM:** texto teórico profundo que cubre modelos gráficos, base matemática de muchos algoritmos modernos.
- **Conocimiento que aporta:** la teoría probabilística unificada detrás de modelos de lenguaje, difusión y modelos generativos.
- **Vocabulario técnico:** *d-separation*, *Markov blanket*, *belief propagation*, *junction tree*, *variational inference*, *EM algorithm*.
- **Razonamiento que aporta:** razonamiento formal sobre independencia condicional, pruebas de convergencia de inferencia.

#### A3 — *Planning Algorithms*
- **Cobertura conceptual:** planificación clásica, planificación bajo incertidumbre (POMDPs), planificación de movimiento, algoritmos geométricos.
- **Cobertura práctica:** diseño de sistemas de planificación para robots y agentes autónomos.
- **Valor como guía para el LLM:** cubre un nicho de la IA ausente en otros textos; amplía la cobertura del nivel avanzado.
- **Conocimiento que aporta:** algoritmos de planificación y búsqueda en espacios de estados continuos y discretos.
- **Vocabulario técnico:** *POMDP*, *configuration space*, *RRT*, *sampling-based planning*, *information space*, *belief state*.
- **Razonamiento que aporta:** formulación de problemas en espacios de estados, análisis de complejidad de planificación.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | Grokking Artificial Intelligence Algorithms | R. Hurbans | 2020 | 1 | 3 | Baja | 3 | 2 |
| P2 | AI and Machine Learning for Coders | L. Moroney | 2020 | 2 | 4 | Media | 4 | 1 |
| P3 | Paradigms of Artificial Intelligence Programming | P. Norvig | 1992 | 4 | 4 | Media | 5 | 2 |

#### P1 — *Grokking Artificial Intelligence Algorithms*
- **Cobertura conceptual:** búsqueda, lógica, redes neuronales, algoritmos genéticos, enjambres — con ilustraciones.
- **Cobertura práctica:** implementaciones simples de algoritmos clásicos de IA con visualizaciones.
- **Valor como guía para el LLM:** registro introductorio con lenguaje accesible; guía para el nivel "introductorio".
- **Conocimiento que aporta:** resúmenes visuales de algoritmos fundamentales, útiles para documentos de introducción al dominio.
- **Vocabulario técnico:** *heuristic search*, *fitness function*, *pheromone*, *minimax*, *alpha-beta pruning*.
- **Razonamiento que aporta:** analogías y explicaciones intuitivas de algoritmos complejos.

#### P2 — *AI and Machine Learning for Coders*
- **Cobertura conceptual:** visión, NLP, series temporales, ética en IA — usando TensorFlow/Keras de forma práctica.
- **Cobertura práctica:** proyectos completos de IA aplicada con código ejecutable.
- **Valor como guía para el LLM:** código práctico con narrativa técnica accesible; estilo práctico distinto al académico.
- **Conocimiento que aporta:** la aplicación práctica de la IA en áreas específicas (visión, NLP) para practicantes.
- **Vocabulario técnico:** *tokenization*, *embedding*, *conv layer*, *sentiment analysis*, *time series forecasting*, *bias*.
- **Razonamiento que aporta:** razonamiento sobre elección de arquitecturas por tipo de datos y tarea.

#### P3 — *Paradigms of Artificial Intelligence Programming*
- **Cobertura conceptual:** técnicas clásicas de IA en Lisp: búsqueda, razonamiento, sistemas de producción, NLP clásico.
- **Cobertura práctica:** implementaciones de referencia de algoritmos clásicos de IA simbólica.
- **Valor como guía para el LLM:** texto de referencia histórico que conecta IA simbólica con técnicas modernas; prosa técnica de excelente calidad.
- **Conocimiento que aporta:** la tradición de IA simbólica que precede al ML; lenguaje y estructuras de agentes basados en reglas.
- **Vocabulario técnico:** *symbolic AI*, *production rules*, *pattern matching*, *backtracking*, *unification*, *Prolog-style reasoning*.
- **Razonamiento que aporta:** razonamiento simbólico, sistemas de reglas, representación del conocimiento.

## Papers importantes

- Russell, S. — *Research Priorities for Robust and Beneficial Artificial Intelligence* (2015). [arXiv:1602.03506](https://arxiv.org/abs/1602.03506)
- Minsky, M. — *Steps Toward Artificial Intelligence* (Proceedings of the IRE, 1961).
- McCarthy, J. et al. — *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence* (1955).
- Silver, D. et al. — *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm* (AlphaZero, 2017). [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
- Ouyang, L. et al. — *Training language models to follow instructions with human feedback* (RLHF/InstructGPT, 2022). [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)
- Bubeck, S. et al. — *Sparks of Artificial General Intelligence: Early experiments with GPT-4* (2023). [arXiv:2303.12528](https://arxiv.org/abs/2303.12528)

## Documentación oficial

- [OpenAI API documentation](https://platform.openai.com/docs/) — guía de uso y conceptos de LLMs.
- [DeepMind Research](https://deepmind.google/research/) — papers y blog posts técnicos.
- [AI Safety resources — Anthropic](https://www.anthropic.com/research) — investigación de seguridad y alineación.

## Blogs técnicos

- [AI Alignment Forum](https://www.alignmentforum.org/) — discusión técnica profunda sobre alineación y seguridad.
- [Import AI (J. Clark)](https://importai.substack.com/) — newsletter semanal sobre avances en IA.
- [Gary Marcus — The Road to AI We Can Trust](https://garymarcus.substack.com/) — perspectiva crítica equilibrada.
- [Ben Evans — newsletter](https://www.ben-evans.com/newsletter) — IA en contexto de industria y sociedad.
- [Gwern.net](https://www.gwern.net/) — análisis profundos sobre IA, escalado y predicciones.

## Repositorios GitHub

- [aimacode/aima-python](https://github.com/aimacode/aima-python) — código de AIMA (F1) en Python (MIT).
- [openai/gym](https://github.com/openai/gym) / [Farama-Foundation/Gymnasium](https://github.com/Farama-Foundation/Gymnasium) — entornos RL de referencia.
- [google-deepmind/acme](https://github.com/google-deepmind/acme) — biblioteca RL de DeepMind (Apache-2.0).
- [eleutherai/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — evaluación de LLMs (MIT).
- [Farama-Foundation/PettingZoo](https://github.com/Farama-Foundation/PettingZoo) — entornos multi-agente (MIT).

## Benchmarks

- **MMLU** — evaluación de conocimiento en 57 materias incluyendo CS e IA.
- **ARC (AI2 Reasoning Challenge)** — razonamiento de sentido común.
- **BIG-Bench** — tareas más allá del entrenamiento estándar de LLMs.
- Para este dominio específico: preguntas de examen de cursos públicos (CS221 Stanford, 6.034 MIT).

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| OpenAI Gym environments | MIT | Entornos para RL; texto de documentación útil |
| AI2 Reasoning Challenge (ARC) | CC BY-SA 4.0 | Preguntas de razonamiento, útiles para evaluación |
| MMLU | MIT | Preguntas de conocimiento multi-dominio |
| Alignment Forum posts dump | Verificar licencia | Discusiones técnicas de alineación |
| Wikipedia ES/EN — IA y ML articles | CC BY-SA 4.0 | Sí está en el corpus (`wikipedia_es`, `wikipedia_en`) |
