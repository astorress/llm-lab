# Corpus semilla — dominio: ingenieria_electrica

## Leyes de Kirchhoff y análisis de circuitos
<!-- subcategoria: circuitos | dificultad: introductorio | idioma: es -->
Las leyes de Kirchhoff son la base del análisis de circuitos. La ley de corrientes (LCK) establece que la suma algebraica de las corrientes que entran a un nodo es cero, consecuencia de la conservación de la carga. La ley de voltajes (LVK) establece que la suma algebraica de las diferencias de potencial en cualquier lazo cerrado es cero, consecuencia de la conservación de la energía. Combinadas con la ley de Ohm (V = I·R), permiten plantear sistemas de ecuaciones lineales que se resuelven con análisis nodal (incógnitas: voltajes de nodo) o análisis de malla (incógnitas: corrientes de lazo). Para circuitos lineales se aplican además los teoremas de superposición, Thévenin y Norton, que simplifican una red compleja a una fuente equivalente con su impedancia.

## Análisis fasorial en régimen sinusoidal permanente
<!-- subcategoria: corriente_alterna | dificultad: intermedio | idioma: es -->
En régimen sinusoidal permanente, una señal v(t) = Vm·cos(ωt + φ) se representa como un fasor complejo V = Vm∠φ, lo que convierte ecuaciones diferenciales en ecuaciones algebraicas complejas. La impedancia generaliza la resistencia: para un resistor Z = R, para un inductor Z = jωL y para un capacitor Z = 1/(jωC). La potencia compleja S = V·I* = P + jQ separa la potencia activa P (vatios, trabajo útil) de la reactiva Q (voltamperios reactivos, intercambio con campos). El factor de potencia cos(φ) mide la eficiencia del uso de la corriente; su corrección con bancos de capacitores reduce pérdidas y mejora la capacidad de la red.

## Máquinas eléctricas: el motor de inducción
<!-- subcategoria: maquinas | dificultad: intermedio | idioma: es -->
El motor de inducción trifásico es el caballo de batalla de la industria. Su estator genera un campo magnético rotativo a la velocidad síncrona ns = 120·f/p, donde f es la frecuencia y p el número de polos. El rotor gira a una velocidad ligeramente menor; el deslizamiento s = (ns − n)/ns es la fracción de diferencia. Las corrientes inducidas en el rotor (de ahí el nombre) crean el par motor. El circuito equivalente por fase, similar al de un transformador con la resistencia del rotor R2/s, permite calcular par, corriente y eficiencia. El par máximo (par de ruptura) ocurre a un deslizamiento que depende de la relación entre la resistencia y la reactancia del rotor.
