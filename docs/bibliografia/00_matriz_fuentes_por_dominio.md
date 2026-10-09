# Matriz de fuentes por dominio

> Nota: esta es una matriz de **lecturas de referencia** que guían temas y vocabulario; **no es la lista de fuentes del corpus**. El texto de los libros no se ingiere; las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml). Los dominios que no aparecen aquí (estadística, metaheurísticas, analítica, LLM, full stack, filosofía, música) tienen su propia ficha en esta carpeta.

Esta matriz prioriza lecturas de referencia para definir los temas y el vocabulario del corpus tecnico. Cada libro debe convertirse en una ficha extendida con: titulo, autores, ano, dificultad, relevancia, prioridad, calidad tecnica, densidad matematica, cobertura conceptual, cobertura practica, utilidad para entrenar un LLM, vocabulario aportado y tipo de razonamiento.

Escala sugerida: baja, media, alta, muy alta.

## Machine Learning

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Pattern Recognition and Machine Learning | Christopher Bishop | 2006 | alta | muy alta | probabilistico, algebraico, inferencia |
| Fundamental | The Elements of Statistical Learning | Hastie, Tibshirani, Friedman | 2009 | alta | muy alta | estadistico, geometrico, model selection |
| Fundamental | Mathematics for Machine Learning | Deisenroth, Faisal, Ong | 2020 | media | alta | algebra lineal, calculo, probabilidad |
| Avanzado | Probabilistic Machine Learning: An Introduction | Kevin Murphy | 2022 | alta | muy alta | modelos probabilisticos modernos |
| Avanzado | Probabilistic Machine Learning: Advanced Topics | Kevin Murphy | 2023 | muy alta | alta | inferencia avanzada y deep generative models |
| Avanzado | Information Theory, Inference, and Learning Algorithms | David MacKay | 2003 | alta | alta | informacion, compresion, Bayesian reasoning |
| Practico | Hands-On Machine Learning | Aurelien Geron | 2022 | media | alta | implementacion, scikit-learn, TensorFlow |
| Practico | Designing Machine Learning Systems | Chip Huyen | 2022 | media | alta | sistemas reales, datos, evaluacion |
| Practico | Machine Learning Engineering | Andriy Burkov | 2020 | media | media | despliegue conceptual y decisiones de producto |

## Deep Learning

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Deep Learning | Goodfellow, Bengio, Courville | 2016 | alta | muy alta | backprop, optimizacion, representaciones |
| Fundamental | Neural Networks and Deep Learning | Michael Nielsen | 2015 | media | alta | intuicion de gradientes y redes |
| Fundamental | Understanding Deep Learning | Simon Prince | 2023 | alta | alta | derivaciones modernas y visuales |
| Avanzado | Dive into Deep Learning | Zhang et al. | 2023 | media | alta | implementacion detallada en notebooks |
| Avanzado | Deep Learning with Python | Francois Chollet | 2021 | media | media | practica y conceptualizacion |
| Avanzado | Speech and Language Processing | Jurafsky, Martin | 2024 | alta | muy alta | NLP, transformers, evaluacion |
| Practico | Natural Language Processing with Transformers | Tunstall, von Werra, Wolf | 2022 | media | muy alta | HuggingFace, fine-tuning, datasets |
| Practico | Build a Large Language Model From Scratch | Sebastian Raschka | 2024 | media | muy alta | GPT educativo desde cero |
| Practico | Machine Learning with PyTorch and Scikit-Learn | Raschka, Liu, Mirjalili | 2022 | media | alta | PyTorch y experimentacion |

## Ciencia de Datos

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Python for Data Analysis | Wes McKinney | 2022 | media | alta | pandas, limpieza, datos tabulares |
| Fundamental | R for Data Science | Wickham, Cetinkaya-Rundel, Grolemund | 2023 | media | media | pensamiento tidy y analisis reproducible |
| Fundamental | Practical Statistics for Data Scientists | Bruce, Bruce, Gedeck | 2020 | media | alta | estadistica aplicada |
| Avanzado | Feature Engineering and Selection | Kuhn, Johnson | 2019 | alta | alta | representacion de variables |
| Avanzado | Data Science from Scratch | Joel Grus | 2019 | media | media | implementacion conceptual |
| Avanzado | Fundamentals of Data Visualization | Claus Wilke | 2019 | media | alta | comunicacion visual |
| Practico | Effective Pandas | Matt Harrison | 2021 | media | media | idioms de pandas |
| Practico | Storytelling with Data | Cole Nussbaumer Knaflic | 2015 | baja | media | explicacion y visualizacion |
| Practico | Data Pipelines Pocket Reference | James Densmore | 2021 | media | alta | pipelines y ETL |

## Inteligencia Artificial

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Artificial Intelligence: A Modern Approach | Russell, Norvig | 2020 | alta | muy alta | busqueda, logica, agentes, probabilidades |
| Fundamental | Machine Learning: A Probabilistic Perspective | Kevin Murphy | 2012 | alta | alta | razonamiento probabilistico |
| Fundamental | Pattern Recognition and Machine Learning | Christopher Bishop | 2006 | alta | alta | inferencia y modelos |
| Avanzado | Reinforcement Learning: An Introduction | Sutton, Barto | 2018 | alta | alta | decisiones secuenciales |
| Avanzado | Probabilistic Robotics | Thrun, Burgard, Fox | 2005 | alta | media | incertidumbre y estimacion |
| Avanzado | Algorithms for Decision Making | Kochenderfer et al. | 2022 | alta | alta | decision theory |
| Practico | Artificial Intelligence with Python | Prateek Joshi | 2017 | media | media | implementacion |
| Practico | Grokking Artificial Intelligence Algorithms | Rishal Hurbans | 2020 | baja | media | intuicion algoritimica |
| Practico | Hands-On Large Language Models | Alammar, Grootendorst | 2024 | media | alta | practica moderna de LLMs |

## Ingenieria Electrica

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Electrical Engineering: Principles and Applications | Allan Hambley | 2017 | media | alta | circuitos, senales, potencia |
| Fundamental | Electric Machinery Fundamentals | Stephen Chapman | 2011 | media | media | maquinas electricas |

## Matematicas, Estadistica y Optimizacion

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Linear Algebra Done Right | Sheldon Axler | 2015 | alta | alta | espacios vectoriales y operadores |
| Fundamental | Calculus | Michael Spivak | 2008 | alta | media | rigor de derivadas |
| Fundamental | Introduction to Probability | Blitzstein, Hwang | 2019 | media | alta | probabilidad discreta y continua |
| Avanzado | Convex Optimization | Boyd, Vandenberghe | 2004 | alta | muy alta | dualidad, KKT, descenso |
| Avanzado | Numerical Optimization | Nocedal, Wright | 2006 | muy alta | muy alta | optimizacion numerica |
| Avanzado | All of Statistics | Larry Wasserman | 2004 | alta | alta | inferencia estadistica |
| Practico | Think Stats | Allen Downey | 2014 | baja | media | simulacion e intuicion |
| Practico | Practical Linear Algebra for Data Science | Mike X Cohen | 2022 | media | alta | algebra aplicada |
| Practico | Algorithms for Optimization | Kochenderfer, Wheeler | 2019 | media | alta | implementacion de optimizadores |

## Programacion y Python

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Fluent Python | Luciano Ramalho | 2022 | alta | alta | idioms, data model, iteradores |
| Fundamental | Effective Python | Brett Slatkin | 2019 | media | alta | buenas practicas |
| Fundamental | Python Crash Course | Eric Matthes | 2023 | baja | media | ejemplos claros |
| Avanzado | Architecture Patterns with Python | Percival, Gregory | 2020 | alta | alta | arquitectura y testing |
| Avanzado | High Performance Python | Gorelick, Ozsvald | 2020 | alta | media | profiling, memoria, concurrencia |
| Avanzado | Robust Python | Patrick Viafore | 2021 | media | media | tipos y mantenibilidad |
| Practico | Automate the Boring Stuff with Python | Al Sweigart | 2019 | baja | media | scripting util |
| Practico | Python Testing with pytest | Brian Okken | 2022 | media | alta | testing |
| Practico | Serious Python | Julien Danjou | 2018 | media | media | empaquetado y practica profesional |

## PostgreSQL y MongoDB

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | PostgreSQL: Up and Running | Obe, Hsu | 2017 | media | alta | SQL, extensiones, administracion |
| Fundamental | SQL Antipatterns | Bill Karwin | 2010 | media | alta | patrones y errores |
| Fundamental | Designing Data-Intensive Applications | Martin Kleppmann | 2017 | alta | muy alta | datos distribuidos |
| Avanzado | PostgreSQL 14 Internals | Egor Rogov | 2022 | alta | alta | storage, planner, WAL |
| Avanzado | The Art of PostgreSQL | Dimitri Fontaine | 2020 | alta | alta | SQL avanzado |
| Avanzado | MongoDB: The Definitive Guide | Shannon Bradshaw et al. | 2019 | media | alta | documentos, indices, agregaciones |
| Practico | SQL Performance Explained | Markus Winand | 2012 | media | alta | indices y planes |
| Practico | Practical MongoDB Aggregations | Paul Done | 2023 | media | media | pipelines |
| Practico | Database Internals | Alex Petrov | 2019 | alta | alta | estructuras internas |

## AWS, Serverless e Infraestructura como Codigo

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | AWS Certified Solutions Architect Study Guide (4a ed.) | Piper, Clinton | 2022 | media | alta | vocabulario AWS |
| Fundamental | Serverless Architectures on AWS | Peter Sbarski | 2017 | media | alta | Lambda, eventos, trade-offs |
| Fundamental | Infrastructure as Code | Kief Morris | 2020 | media | muy alta | declaratividad, automatizacion |
| Avanzado | Terraform: Up & Running | Yevgeniy Brikman | 2022 | media | alta | IaC practica |
| Avanzado | Cloud Native DevOps with Kubernetes | Arundel, Domingus | 2019 | alta | media | operaciones cloud native |
| Avanzado | Building Secure and Reliable Systems | Google SRE Team | 2020 | alta | alta | confiabilidad y seguridad |
| Practico | AWS Lambda in Action | Danilo Poccia | 2017 | media | media | serverless practico |
| Practico | Production-Ready Serverless (curso) | Yan Cui | 2018 | media | alta | patrones reales |
| Practico | The DevOps Handbook | Kim et al. | 2021 | media | alta | flujo, calidad, automatizacion |

## APIs, Arquitectura, DevOps, Data Engineering y Sistemas Distribuidos

| Tipo | Fuente | Autores | Ano | Dificultad | Prioridad | Aporte al LLM |
|---|---|---:|---:|---|---|---|
| Fundamental | Designing Data-Intensive Applications | Martin Kleppmann | 2017 | alta | muy alta | consistencia, replicacion, streaming |
| Fundamental | Software Architecture: The Hard Parts | Ford, Richards, Sadalage, Dehghani | 2021 | alta | alta | trade-offs arquitectonicos |
| Fundamental | RESTful Web APIs | Richardson, Amundsen, Ruby | 2013 | media | alta | contratos y recursos |
| Avanzado | Site Reliability Engineering | Google SRE Team | 2016 | alta | alta | confiabilidad, SLOs, incidentes |
| Avanzado | Streaming Systems | Akidau, Chernyak, Lax | 2018 | alta | alta | tiempo de evento, ventanas |
| Avanzado | Release It! | Michael Nygard | 2018 | media | alta | resiliencia |
| Practico | API Design Patterns | JJ Geewax | 2021 | media | alta | diseno de APIs |
| Practico | Fundamentals of Data Engineering | Reis, Housley | 2022 | media | muy alta | ciclo de vida de datos |
| Practico | Kubernetes Patterns | Ibryam, Huß | 2019 | media | media | operacion de servicios |

## Papers, documentacion y repositorios prioritarios

- Transformers: Attention Is All You Need; BERT; GPT-1/2/3; T5; LLaMA; RoPE; FlashAttention; Switch Transformers; LoRA; QLoRA; DPO.
- Documentacion oficial: PyTorch, HuggingFace Transformers, Datasets, Tokenizers, Accelerate, PEFT, PostgreSQL, MongoDB, AWS Lambda, Serverless Framework, Terraform.
- Repositorios: karpathy/nanoGPT, karpathy/minGPT, huggingface/transformers, huggingface/tokenizers, huggingface/datasets, Lightning-AI/litgpt.
- Benchmarks: MMLU, HellaSwag, ARC, GSM8K, HumanEval, BigBench, GLUE, SuperGLUE, TruthfulQA.
- Datasets que sí usa el corpus (configs/data.yaml): Wikipedia es/en, FineWeb-2 spa_Latn, FineWeb-Edu sample-10BT, Cosmopedia v2, OpenWebMath, arXiv abstracts y codeparrot-clean, más el corpus personal y el semilla.
- Datasets solo de referencia (no ingeridos): StackExchange, CodeSearchNet, The Pile, OpenWebText, documentación oficial, otros repositorios.

## Como expandir cada ficha de libro

Para cada libro, crea un registro:

```yaml
title:
authors:
year:
difficulty: baja | media | alta | muy alta
relevance: baja | media | alta | muy alta
priority: baja | media | alta | muy alta
technical_quality: baja | media | alta | muy alta
math_density: baja | media | alta | muy alta
conceptual_coverage: baja | media | alta | muy alta
practical_coverage: baja | media | alta | muy alta
why_for_llm_training:
knowledge_added:
technical_vocabulary:
reasoning_type:
license_notes:
corpus_use: metadata_only   # los libros no se ingieren; solo guían temas y vocabulario
```

