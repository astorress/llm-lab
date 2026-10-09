# Corpus semilla — dominio: estadistica

## Estimación por máxima verosimilitud
<!-- subcategoria: inferencia | dificultad: avanzado | idioma: es -->
La estimación por máxima verosimilitud (MLE) elige los parámetros θ que maximizan la probabilidad de los datos observados bajo el modelo: θ_MLE = argmax L(θ; datos), donde L es la función de verosimilitud. En la práctica se maximiza el logaritmo (log-verosimilitud), que convierte productos en sumas y es numéricamente estable. Para muchos modelos, minimizar la entropía cruzada equivale a MLE: entrenar un clasificador con cross-entropy es estimar por máxima verosimilitud una distribución categórica. Bajo condiciones de regularidad, el MLE es consistente y asintóticamente eficiente, alcanzando la cota de Cramér-Rao.

## Teorema de Bayes e inferencia bayesiana
<!-- subcategoria: bayesiana | dificultad: intermedio | idioma: es -->
El teorema de Bayes actualiza creencias ante evidencia: P(θ|datos) ∝ P(datos|θ)·P(θ), es decir, el posterior es proporcional a la verosimilitud por el prior. La inferencia bayesiana trata los parámetros como variables aleatorias con distribución, en contraste con el enfoque frecuentista que los considera fijos pero desconocidos. El prior codifica conocimiento previo; con priors conjugados el posterior tiene forma cerrada. Cuando no, se recurre a métodos de Monte Carlo (MCMC) o inferencia variacional. El posterior permite cuantificar incertidumbre con intervalos de credibilidad.
