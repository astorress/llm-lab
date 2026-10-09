# Bibliografía — Desarrollo Full Stack

> Dominio `full_stack` · peso 1.5 · [índice maestro](../02_libros_y_fuentes.md)

**Alcance:** Aplicaciones web completas: frontend, backend, datos, autenticación y despliegue.

## Libros

### Fundamentales

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Eloquent JavaScript (4ª ed.) | M. Haverbeke | 2024 | Gratis en línea; JavaScript desde cero con rigor |
| Full Stack Open | Universidad de Helsinki | 2025 | Curso gratuito: React, Node, GraphQL, TypeScript, CI/CD |
| Programming TypeScript | B. Cherny | 2019 | Tipos estáticos para frontend y backend |

### Avanzados

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| Learning React (2ª ed.) | A. Banks, E. Porcello | 2020 | Componentes, hooks y estado |
| Node.js Design Patterns (3ª ed.) | M. Casciaro, L. Mammino | 2020 | Asincronía, streams y patrones de backend |
| FastAPI: Modern Python Web Development | B. Lubanovic | 2023 | Backend Python tipado y asíncrono |

### Prácticos

| Título | Autores | Año | Aporte al LLM |
|---|---|---|---|
| CSS: The Definitive Guide (5ª ed.) | E. Meyer, E. Weyl | 2023 | Layout moderno: flexbox, grid |
| Web Application Security (2ª ed.) | A. Hoffman | 2024 | OWASP, XSS, CSRF, autenticación segura |
| MDN Web Docs / docs de React y Next.js | Mozilla / Meta / Vercel | 2025 | Referencia oficial (licencias abiertas en MDN) |

## Papers clave

- Fielding (2000) — Architectural Styles and the Design of Network-based Software Architectures (REST)
- RFC 6749 — OAuth 2.0
- RFC 7519 — JSON Web Token

## Datos, librerías y fuentes de texto

Fuentes que sí usa el corpus: Wikipedia es/en, FineWeb-2 `spa_Latn`, FineWeb-Edu y Cosmopedia v2 filtradas por dominio, abstracts de arXiv (`cs.SE`, `cs.HC`) y código Python de codeparrot-clean. Candidatas no ingeridas: MDN (CC BY-SA 2.5), documentación oficial de frameworks, código JS/TS de GitHub.

## Vocabulario que debe dominar el modelo

*componente*, *estado*, *hidratación*, *SSR*, *SPA*, *endpoint*, *ORM*, *migración*, *JWT*, *CORS*, *WebSocket*, *bundle*

> Licencias: los libros guían temas y vocabulario y su texto no se ingiere; el texto del corpus sale solo de las fuentes de [configs/data.yaml](../../configs/data.yaml) (ver índice maestro).
