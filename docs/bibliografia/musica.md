# Bibliografía — Música

> Dominio `musica` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

**Alcance:** Teoría musical, armonía, historia, acústica y producción/computación musical.

## Libros

### Fundamentales

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Tonal Harmony (8ª ed.) | S. Kostka, D. Payne, B. Almén | 2018 | Armonía tonal estándar universitario |
| Harmony and Voice Leading (5ª ed.) | E. Aldwell, C. Schachter, A. Cadwallader | 2018 | Conducción de voces |
| A History of Western Music (10ª ed.) | J. P. Burkholder, D. J. Grout, C. V. Palisca | 2019 | Historia de la música occidental |

### Avanzados

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| The Jazz Theory Book | M. Levine | 1995 | Armonía y escalas del jazz |
| Teoría de la armonía | A. Schoenberg | 1911 | Clásico de la armonía tonal |
| Sweet Anticipation: Music and the Psychology of Expectation | D. Huron | 2006 | Cognición musical |

### Prácticos

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Fundamentals of Music Processing (2ª ed.) | M. Müller | 2021 | Procesamiento de audio y MIR con Python |
| The Computer Music Tutorial (2ª ed.) | C. Roads | 2023 | Síntesis y computación musical |
| Música en Colombia / ritmos latinos (Wikipedia, fuentes abiertas) | varios | 2025 | Salsa, cumbia, vallenato, bambuco |

## Papers clave

- Huang et al. (2018) — Music Transformer
- Dhariwal et al. (2020) — Jukebox
- Agostinelli et al. (2023) — MusicLM
- Copet et al. (2023) — MusicGen (Simple and Controllable Music Generation)

## Datos, librerías y fuentes de texto

Fuentes que sí usa el corpus: Wikipedia es/en (teoría e historia; `wikipedia_es` es la principal fuente de música en español), además de lo que pase el filtro de dominio en FineWeb-2 `spa_Latn`, FineWeb-Edu y Cosmopedia v2, y los abstracts de arXiv (`cs.SD`, `eess.AS`). Candidatas no ingeridas: IMSLP y Mutopia (partituras de dominio público), MAESTRO (CC BY-NC-SA), Lakh MIDI, Free Music Archive.

## Vocabulario que debe dominar el modelo

*escala*, *acorde*, *tríada*, *cadencia*, *dominante*, *contrapunto*, *compás*, *tempo*, *timbre*, *armónicos*, *MIDI*, *síntesis*, *clave*

> Licencias: los libros guían temas y vocabulario y su texto no se ingiere; el texto del corpus sale solo de las fuentes de [configs/data.yaml](../../configs/data.yaml) (ver índice maestro).
