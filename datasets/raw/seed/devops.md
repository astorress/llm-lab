# Corpus semilla — dominio: devops

## Integración y entrega continua (CI/CD)
<!-- subcategoria: cicd | dificultad: intermedio | idioma: es -->
La integración continua (CI) automatiza la construcción y prueba del código cada vez que se integra un cambio, detectando errores temprano. La entrega/despliegue continuo (CD) extiende el pipeline hasta poner los cambios en producción de forma automática y frecuente. Un pipeline típico: checkout, build, pruebas unitarias e integración, análisis estático, construcción de imagen, despliegue a staging y a producción. Estrategias de despliegue como blue-green y canary reducen el riesgo liberando gradualmente. Las métricas DORA (frecuencia de despliegue, lead time, tasa de fallo de cambios, tiempo de recuperación) miden la madurez del flujo de entrega.

## Contenedores con Docker y orquestación
<!-- subcategoria: contenedores | dificultad: intermedio | idioma: es -->
Docker empaqueta una aplicación con todas sus dependencias en una imagen inmutable que se ejecuta igual en cualquier entorno, resolviendo el clásico 'en mi máquina funciona'. Una imagen se construye por capas desde un Dockerfile; los contenedores son instancias en ejecución de una imagen, aislados pero compartiendo el kernel del host (más ligeros que máquinas virtuales). A escala, un orquestador como Kubernetes gestiona el despliegue declarativo, el escalado, el balanceo de carga y la recuperación de contenedores fallidos, reconciliando continuamente el estado real con el deseado.
