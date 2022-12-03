# Introducción a la Teoría de Errores

## Aproximaciones y errores

Siempre que se trabaje con valores aproximados se tendrá que:
$$\text{Valor real = Valor aproximado + Error}$$

### Tipos de errores

#### Errores inherentes

Existen en los valores de los datos, se dan por la naturaleza aproximada de una
aproximación mediante un número finito de dígitos.

##### Errores de truncación

Se aproxima el valor exacto hasta una cantidad determinada de dígitos decimales
exactos.

Son debidos a la omisión de términos en una serie con un número infinito de
términos.

Por ejemplo: Podemos usar la serie de Taylor para calcular el seno de cualquier
ángulo.

$$
sin(x) =
x - \cfrac{x^3}{3!} + \cfrac{x^5} {5!} - \cfrac{x^7} {7!} + ...
$$

##### Errores de redondez (aritmética de punto flotante)

Se aproxima el valor del número mediante una cierta cantidad de cifras
significativas.

Estos errores se introducen en los procesos de computación por el hecho de que
los computadores trabajan con un número finito de dígitos después del punto
decimal y tienen que redondear.

Como nos interesa el redondeo por punto flotante, revisaremos la forma de
representación de un número como punto flotante.

Recordando que cada número lo podemos representar como una fracción llamada
[Mantissa](https://es.wikipedia.org/wiki/Mantisa), la cual está multiplicada por
una potencia del número base, llamada generalmente exponente. Entonces tenemos
números como los siguientes.

$$
\begin {aligned}
0.3864 \times 10^4 &= 3864 \\
0.54365 \times 10^2 &= 54.365 \\
0.182 \times 10^{-3} &= 1.000182 \\
\end{aligned}
$$

#### Errores sistemáticos

 Son debidos a problemas en el funcionamiento de los aparatos de medida o al
 hecho de que al introducir el aparato de medida en el sistema, éste se altera
 y se modifica, por lo tanto, la magnitud que deseamos medir cambia su valor.
 Normalmente actúan en el mismo sentido.

#### Errores accidentales

Son debidos a causas imponderables que alteran aleatoriamente las medidas. Al
producirse aleatoriamente las medidas se distribuyen alrededor del valor real,
por lo que un tratamiento estadístico permite estimar su valor.

## Nociones de estabilidad numérica

**Presición**: Indica qué tan cerca están las aproximaciones (unas de otras).
Además, puede indicar la cantidad de dígitos correctos en una estimación.

**Exactitud**: Diferencia entre el valor aproximado y el valor real.

Una serie se aproximaciones es precisa cuando están <u>cerca de ellas</u>.

Una serie se aproximaciones es precisa cuando están <u>cerca del
valor original</u>.

En nuestras aproximaciones buscamos exactitud y presición.

Cómo cuantificamos la exactitud y la presición?

### Dígitos significativos

**Teorema**: Se dice que $\bar x$ aproxima a $x$ con $k$ dígitos significatvos
si $k$ es el entero más grande positivo para el cual se cumple que:

$$
\cfrac{|x - \bar x|} {x} \leq 5 \cdot 10^{-k}
$$

$$
\varepsilon \bar x \leq 5 \cdot 10 ^ {-k}
$$

### Exactitud de una aproximación

La exactitud de una aproximación es $k-1$, donde $k$ es el número de dígitos
significativos.

Así, $\bar x$ aproxima a $x$ con $k$ dígitos significativos, se puede decir que
$\bar x$ tiene al menos $k-1$ cifras exactas.

### Cifras decimales exactas
**Teorema**: Sea $\bar x$ una aproximación de un cierto número $x$ y sabe que
$\bar x$ aproxima a $x$ con $k$ cifras decimales exactas si:

$$
E\bar x = | x - \bar x | \leq 0.5 \cdot 10^{-k}
$$

## Representación de números en el computador

### Clasificación cualitativa del error

#### Error absoluto

Sea $x$ el valor exacto y $\bar x$ una aproximación del mismo, se
denota al error absoluto como $E \bar x$ y se define como:

$$
E \bar x = |x - \bar x| = \text {Valor real - Aproximación}
$$

Nótese que el error absoluto no nos da información acerca de si una
aproximación es "buena" o "mala". Esto debido a que no toma en cuenta
la dimensión del error con relación a su proporción.

Por ejemplo un error absoluto de 10cm puede considerarse "bueno" si se está
midiendo la longitud de un avión. Sin embargo puede considerarse "malo" si se
está midiendo un escritorio.

#### Error relativo

Pone en perspectiva la dimensió del error que se está realizando.

Sea $x$ el valor exacto y $\bar x$ una aproximación. Se denota
$\varepsilon \bar x$ al error relativo y se define como:

$$
\varepsilon \bar x = \cfrac{|x - \bar x|}{|x|}\\
$$

$$
\varepsilon \bar x = \cfrac{E \bar x}{|x|}
$$

Por lo general es representado de manera porcentual.

Ejemplo: Se sabe que una cancha mide 105m x 68m. Si dos estudiantes obtienen
como dimensiones 103.76m x 66.98m. Cuál sería el error relativo y absoluto?
Qué se midió mejor? ancho o alto?

$$
w: E\bar x = 1.24m \space \varepsilon \bar x  = 0.0118 \\
h: E\bar x = 1.02m \space \varepsilon \bar x  = 0.015
$$

#### Error relativo normalizado

Surge cuando no tenemos el valor real, solo aproximaciones.

Si $\bar x_1$ y $\bar x_2$ son aproximaciones del valor real $x$ y se cree que
$\bar x _ 2$ es mejor que $\bar x_1$.

$$
\varepsilon \bar x_2 =  \cfrac{|\bar x_2 - \bar x_1 |}{\bar x _ 2}
$$

Observe que el error relativo normalizado es el mismo error relativo, pero
utilizando una aproximación en vez del valor real.

## Medidas de error


### Propagación de errores

### Aplicaciones

