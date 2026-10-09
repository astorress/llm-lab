# Corpus semilla — dominio: apis

## Diseño de APIs REST y semántica HTTP
<!-- subcategoria: rest | dificultad: intermedio | idioma: es -->
REST es un estilo arquitectónico que modela la API como recursos identificados por URLs, manipulados con los métodos HTTP según su semántica: GET (leer, seguro e idempotente), POST (crear), PUT (reemplazar, idempotente), PATCH (actualizar parcial), DELETE (borrar, idempotente). Los códigos de estado comunican el resultado: 2xx éxito, 4xx error del cliente (400 petición inválida, 401 no autenticado, 404 no encontrado), 5xx error del servidor. Buenas prácticas: nombrar recursos con sustantivos en plural, versionar la API, paginar colecciones, y devolver errores con estructura consistente. La idempotencia permite reintentos seguros.

## Autenticación con JWT y OAuth 2.0
<!-- subcategoria: seguridad | dificultad: avanzado | idioma: es -->
OAuth 2.0 es un marco de autorización delegada: permite a una aplicación acceder a recursos en nombre del usuario sin manejar sus credenciales, mediante tokens de acceso emitidos por un servidor de autorización. Los JSON Web Tokens (JWT) son un formato compacto y autocontenido de token: codifican claims (emisor, sujeto, expiración, permisos) firmados criptográficamente, de modo que el servidor puede validarlos sin consultar una base de datos (stateless). El servidor verifica la firma con la clave correspondiente. Riesgos a mitigar: expiración corta, rotación de claves, almacenamiento seguro del token y validación estricta de la firma y los claims.
