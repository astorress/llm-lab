# Bibliografía — Ingeniería Eléctrica

> Dominio `ingenieria_electrica` · peso 1.0 · [índice maestro](../02_libros_y_fuentes.md)

> Nota: «Valor como guía para el LLM» describe para qué sirve cada libro como guía de temas y vocabulario; **el texto de los libros no se ingiere**. Las fuentes reales de pre-entrenamiento están en [configs/data.yaml](../../configs/data.yaml).

## Libros

### Fundamentales

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| F1 | Engineering Circuit Analysis (9ª ed.) | W. H. Hayt, J. E. Kemmerly, S. M. Durbin | 2018 | 3 | 5 | Alta | 5 | 4 |
| F2 | Fundamentals of Electric Circuits (6ª ed.) | C. K. Alexander, M. N. O. Sadiku | 2016 | 2 | 5 | Alta | 5 | 3 |
| F3 | Electric Machinery Fundamentals (5ª ed.) | S. J. Chapman | 2011 | 3 | 5 | Alta | 5 | 3 |

#### F1 — *Engineering Circuit Analysis*
- **Cobertura conceptual:** análisis nodal y mallas, fasores, respuesta en frecuencia, cuadripolos, análisis de Fourier y Laplace.
- **Cobertura práctica:** resolver circuitos con métodos sistemáticos; base de todo análisis eléctrico en ingeniería.
- **Valor como guía para el LLM:** texto canónico de análisis de circuitos con derivaciones paso a paso y problemas resueltos.
- **Conocimiento que aporta:** los fundamentos de circuitos eléctricos que subyacen a todo el dominio de ingeniería eléctrica.
- **Vocabulario técnico:** *nodo*, *malla*, *impedancia*, *fasor*, *función de transferencia*, *respuesta transitoria*, *resonancia*, *potencia reactiva*.
- **Razonamiento que aporta:** aplicación sistemática de KVL/KCL, transformadas de Laplace, análisis de estado estable y transitorio.

#### F2 — *Fundamentals of Electric Circuits*
- **Cobertura conceptual:** leyes de Kirchhoff, circuitos de CA/CC, potencia, amplificadores operacionales, filtros, transformadores.
- **Cobertura práctica:** el texto introductorio más usado en facultades de ingeniería eléctrica en América Latina.
- **Valor como guía para el LLM:** registro pedagógico accesible con muchos ejemplos resueltos — aporta texto de nivel introductorio/intermedio.
- **Conocimiento que aporta:** la base conceptual que conoce cualquier egresado de ingeniería eléctrica en la región.
- **Vocabulario técnico:** *ley de Ohm*, *superposición*, *Thévenin*, *Norton*, *fasores*, *factor de potencia*, *amplificador operacional*.
- **Razonamiento que aporta:** simplificación de circuitos complejos, análisis por partes, verificación dimensional.

#### F3 — *Electric Machinery Fundamentals*
- **Cobertura conceptual:** máquinas de CC, transformadores, máquinas de inducción, máquinas síncronas, máquinas especiales.
- **Cobertura práctica:** cálculo de parámetros de máquinas, curvas de torque-velocidad, regulación de voltaje.
- **Valor como guía para el LLM:** texto de referencia en máquinas eléctricas base física de motores, generadores y transformadores.
- **Conocimiento que aporta:** funcionamiento físico de las máquinas eléctricas que son los componentes de todo sistema de potencia.
- **Vocabulario técnico:** *flujo magnético*, *fuerza contraelectromotriz*, *par de arranque*, *deslizamiento*, *regulación de voltaje*, *eficiencia*.
- **Razonamiento que aporta:** análisis de circuitos equivalentes de máquinas, diseño de sistemas de accionamiento.

### Avanzados

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| A1 | Microelectronic Circuits (7ª ed.) | A. S. Sedra, K. C. Smith | 2014 | 4 | 4 | Media | 5 | 4 |
| A2 | Power Electronics: Circuits, Devices, and Applications (4ª ed.) | M. H. Rashid | 2014 | 4 | 4 | Media | 5 | 4 |
| A3 | Signal Processing and Linear Systems | B. P. Lathi | 1998 | 4 | 4 | Media | 5 | 4 |

#### A1 — *Microelectronic Circuits*
- **Cobertura conceptual:** diodos, transistores BJT y MOSFET, amplificadores, retroalimentación, amplificadores operacionales, frecuencia.
- **Cobertura práctica:** diseño y análisis de circuitos electrónicos analógicos; base para entender hardware de sensores y actuadores.
- **Valor como guía para el LLM:** texto avanzado con análisis matemático riguroso y cobertura completa de electrónica analógica.
- **Conocimiento que aporta:** el nivel de electrónica que conecta la teoría de circuitos con dispositivos reales.
- **Vocabulario técnico:** *punto de operación (Q)*, *ganancia*, *banda de paso*, *retroalimentación negativa*, *estabilidad*, *polarización*, *impedancia de entrada*.
- **Razonamiento que aporta:** análisis de pequeña señal, diseño de amplificadores, análisis de estabilidad con criterio de Bode.

#### A2 — *Power Electronics*
- **Cobertura conceptual:** convertidores AC-DC (rectificadores), DC-DC (buck, boost), inversores, convertidores resonantes, controladores.
- **Cobertura práctica:** diseño de fuentes conmutadas, variadores de frecuencia, cargadores; muy relevante en energías renovables.
- **Valor como guía para el LLM:** vocabulario técnico de electrónica de potencia, interfaz entre circuitos y conversión de energía.
- **Conocimiento que aporta:** la electrónica de potencia que convierte y controla la energía en sistemas modernos de generación/transmisión.
- **Vocabulario técnico:** *chopper*, *duty cycle*, *ripple*, *THD*, *PWM*, *IGBT*, *rectificador de onda completa*, *factor de cresta*.
- **Razonamiento que aporta:** análisis de conmutación, diseño de filtros LC, análisis de formas de onda en régimen permanente.

#### A3 — *Signal Processing and Linear Systems*
- **Cobertura conceptual:** señales y sistemas LTI, transformadas (Fourier, Laplace, Z), filtros analógicos y digitales.
- **Cobertura práctica:** diseño de filtros, análisis espectral, procesamiento de señales de sensores eléctricos.
- **Valor como guía para el LLM:** texto matemáticamente riguroso sobre sistemas lineales, base teórica de control y procesamiento de señales.
- **Conocimiento que aporta:** el marco matemático de sistemas lineales que unifica análisis de circuitos, control y DSP.
- **Vocabulario técnico:** *convolución*, *respuesta al impulso*, *función de transferencia*, *polo*, *cero*, *diagramas de Bode*, *BIBO estabilidad*.
- **Razonamiento que aporta:** análisis en dominio frecuencia, síntesis de filtros, análisis de estabilidad.

### Prácticos

| # | Título | Autores | Año | Dificultad | Relevancia | Prioridad | Calidad | Densidad mat. |
|---|--------|---------|-----|:--:|:--:|:--:|:--:|:--:|
| P1 | The Art of Electronics (3ª ed.) | P. Horowitz, W. Hill | 2015 | 3 | 4 | Media | 5 | 2 |
| P2 | Grob's Basic Electronics (12ª ed.) | M. Schultz | 2015 | 1 | 3 | Baja | 4 | 2 |
| P3 | RETIE (Reglamento Técnico de Instalaciones Eléctricas) | Ministerio de Minas y Energía (Colombia) | 2024 (Res. 40117; con ajustes posteriores) | 3 | 5 | Alta | 5 | 2 |

#### P1 — *The Art of Electronics*
- **Cobertura conceptual:** circuitos analógicos y digitales desde perspectiva práctica; diseño real de hardware.
- **Cobertura práctica:** referencia de laboratorio; cómo elegir componentes, depurar circuitos reales, diseñar fuentes y amplificadores.
- **Valor como guía para el LLM:** registro de "artesanía de ingeniería" — prosa técnica con intuición y reglas prácticas que no aparecen en textos académicos.
- **Conocimiento que aporta:** la brecha entre teoría y práctica de laboratorio; conocimiento tácito del ingeniero electrónico.
- **Vocabulario técnico:** *noise floor*, *power supply rejection*, *current mirror*, *op-amp tricks*, *decoupling capacitor*, *ground plane*.
- **Razonamiento que aporta:** heurísticas de diseño práctico, diagnóstico de problemas reales, elección de topologías.

#### P2 — *Grob's Basic Electronics*
- **Cobertura conceptual:** electrónica básica: CC, CA, semiconductores, circuitos digitales — nivel de técnico electricista.
- **Cobertura práctica:** base para trabajos de instalación, mantenimiento y operación eléctrica básica.
- **Valor como guía para el LLM:** texto de nivel introductorio con vocabulario eléctrico básico — guía para el extremo inferior de dificultad.
- **Conocimiento que aporta:** el vocabulario y conceptos que maneja un técnico eléctrico; complementa los textos universitarios.
- **Vocabulario técnico:** *resistencia*, *condensador*, *inductancia*, *diodo*, *transistor*, *circuito serie/paralelo*, *multímetro*.
- **Razonamiento que aporta:** medición y diagnóstico en laboratorio, lectura de esquemas simples.

#### P3 — *RETIE — Reglamento Técnico de Instalaciones Eléctricas (Colombia)*
- **Cobertura conceptual:** normativa técnica colombiana para instalaciones eléctricas: requisitos, clasificación de zonas, materiales, protecciones.
- **Cobertura práctica:** cumplimiento normativo en proyectos eléctricos en Colombia; referencia regulatoria directa para el contexto de Sebastian.
- **Valor como guía para el LLM:** texto regulatorio/normativo específico de Colombia — aporta el dominio de lenguaje de normativa técnica latinoamericana. **Verificar acceso/licencia** (publicado por el Ministerio de Minas y Energía; consultar la versión vigente; uso referencial).
- **Conocimiento que aporta:** el marco regulatorio colombiano de instalaciones eléctricas, esencial para trabajo en el sector energético local.
- **Vocabulario técnico:** *DPS* (dispositivo de protección contra sobretensiones), *ACOMETIDA*, *calibre de conductores*, *THHN*, *tensión nominal*, *nivel de aislamiento*.
- **Razonamiento que aporta:** interpretación de requisitos normativos, aplicación de tablas de la norma a proyectos reales.

## Papers importantes

- Depenbrock, M. — *Direct Self-Control (DSC) of Inverter-Fed Induction Machine* (IEEE Trans. Power Electronics, 1988). [DOI:10.1109/63.17963](https://doi.org/10.1109/63.17963)
- Blaabjerg, F., Chen, Z., Kjaer, S. B. — *Power Electronics as Efficient Interface in Dispersed Power Generation Systems* (IEEE Trans. Power Electronics, 2004).
- Akagi, H. — *New Trends in Active Filters for Power Conditioning* (IEEE Trans. Industry Applications, 1996).
- Arrillaga, J. et al. — *Power System Harmonic Analysis* (libro, Wiley, 1997).
- Rodríguez, J. et al. — *Multilevel Inverters: A Survey of Topologies, Controls, and Applications* (IEEE Trans. IE, 2002).

## Documentación oficial

- [IEC standards portal](https://www.iec.ch/) — normas internacionales IEC (verificar licencia/acceso institucional).
- [IEEE Xplore](https://ieeexplore.ieee.org/) — base de papers y normas IEEE; acceso institucional recomendado.
- [CREG — Comisión de Regulación de Energía y Gas (Colombia)](https://www.creg.gov.co/) — resoluciones técnicas del sector eléctrico colombiano. **Verificar acceso/licencia**.
- [RETIE / RETILAP — MinMinas Colombia](https://www.minenergia.gov.co/) — reglamentos técnicos de instalaciones eléctricas. **Verificar acceso/licencia**.

## Blogs técnicos

- [All About Circuits](https://www.allaboutcircuits.com/) — tutoriales y referencia técnica (copyright del sitio — verificar licencia).
- [Electronics Tutorials (Wayne Storr)](https://www.electronics-tutorials.ws/) — explicaciones claras de componentes y circuitos.
- [Texas Instruments — Application Notes](https://www.ti.com/applications/overview.html) — notas de aplicación técnicas gratuitas.
- [Power Electronics News](https://www.powerelectronicsnews.com/) — noticias y artículos de electrónica de potencia.
- [EPEC Engineered Technologies Blog](https://www.epectec.com/blog/) — ingeniería eléctrica aplicada.

## Repositorios GitHub

- [FabriceSalvaire/PySpice](https://github.com/FabriceSalvaire/PySpice) — simulación de circuitos desde Python (GPLv3).
- [scipy/scipy](https://github.com/scipy/scipy) — señal, filtros, transformadas (BSD-3).
- [scikit-rf/scikit-rf](https://github.com/scikit-rf/scikit-rf) — microondas y RF en Python (BSD-3).
- [python-control/python-control](https://github.com/python-control/python-control) — sistemas de control en Python (BSD-3).

## Benchmarks

- No existe un benchmark estándar para IA en ingeniería eléctrica pura. Proxies útiles:
  - **MMLU — Engineering** subset: preguntas de ingeniería eléctrica y electrónica.
  - Exámenes de licencia profesional de ingeniería (PE Exam — Electrical, NCEES): preguntas de referencia públicas.
  - Exámenes de habilitación profesional COPNIA (Colombia) — verificar disponibilidad pública.

## Datasets públicos de referencia (no incluidos en configs/data.yaml)

| Dataset | Licencia | Notas |
|---------|----------|-------|
| XM — Informes del Mercado Eléctrico Colombiano | Público (verificar términos de uso) | Datos de demanda, generación y precios del mercado colombiano |
| CREG — Resoluciones técnicas | Dominio público (norma regulatoria) | Texto normativo del sector eléctrico colombiano |
| NERC reliability reports | Público | Informes de confiabilidad del sistema eléctrico norteamericano |
| IEEE PES Open Data Sets | Verificar por dataset | Datos de sistemas de potencia de referencia |
| UCI — Electrical grid stability dataset | CC BY 4.0 | Dataset de estabilidad de red |
