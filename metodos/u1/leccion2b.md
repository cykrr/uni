# Resumen

* Cuantificación del error
* Tipos de errores
  * Error de truncamiento
  * Error de redondeo
El resultado de un problema respecto a la representación
numérica

## Estabilidad numérica

Lo ideal de un algoritmo numérico es que si su representación induce un error, éste se mantuviera estable (acotado).

Un algoritmo inestable, a medida que se realiza el cálculo de va magnificando

$$
x - (x + \varepsilon) \congruent f(x)  - f(x+ \varepsilon)
$$

$$
\cfrac{x - (x + \varepsilon)} x \congruent \cfrac {f(x)  - f(x+ \varepsilon)} {f(x)}
$$

Un problema se puede definir como

$$
f: X \arrow Y
$$

Un algoritmo se puede ver como:

$$
f^~: X \arrow Y
$$

Tenemos además: Un computador cuya representación es punto
flotante. Una implementación de este algoritmo en la forma de un programa.

Una pequeña perturbación en la entrada genera una gran
perturbación en la salida.

### Épsilon de máquina

Da una cota superior al error relativo debido al redondeo
debido a la representación de punto flotante.

Representa el valor más pequeño que puede representar una
variable debido a la cantidad limitada de bits que tenemos.

Equivalente al límite inferior del underflow.

Definición: Un algoritmo $\tilde f$ para un problema $f$ se dice que es estable si para cada $x \in X$ existe $\tilde x$ para el que 

$$
\cfrac {||\tilde x - x|| } {||x||} = O(\Epsilon M)
$$

$$
\cfrac {||f(\tilde x) - \tilde f(x)|| } {||\tilde f(x)||} = O(\Epsilon M)
$$
