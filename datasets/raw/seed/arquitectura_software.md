# Corpus semilla — dominio: arquitectura_software

## Principios SOLID y arquitectura limpia
<!-- subcategoria: principios | dificultad: intermedio | idioma: es -->
Los principios SOLID guían el diseño orientado a objetos mantenible: responsabilidad única (una clase una razón para cambiar), abierto/cerrado (abierto a extensión, cerrado a modificación), sustitución de Liskov (los subtipos deben ser sustituibles por sus tipos base), segregación de interfaces (interfaces específicas mejor que una general) e inversión de dependencias (depender de abstracciones, no de concreciones). La arquitectura limpia aplica la inversión de dependencias a nivel de sistema: la lógica de negocio en el centro no depende de detalles como la base de datos o el framework web, que quedan en capas externas; las dependencias apuntan siempre hacia adentro.

## Microservicios frente al monolito
<!-- subcategoria: estilos | dificultad: avanzado | idioma: es -->
Una arquitectura de microservicios descompone una aplicación en servicios pequeños e independientes, cada uno con su responsabilidad de negocio, base de datos y ciclo de despliegue. Frente al monolito, ofrece escalado independiente, despliegues autónomos y aislamiento de fallos, a costa de complejidad operativa: comunicación en red, consistencia distribuida, observabilidad y orquestación. La frontera de cada servicio se define idealmente alrededor de un bounded context del dominio (DDD). Patrones clave: API Gateway, circuit breaker para tolerancia a fallos, y sagas para transacciones distribuidas. No es la opción por defecto: el monolito modular suele ser preferible al inicio.
