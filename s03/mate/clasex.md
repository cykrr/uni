# Continuidad
## Ejemplo: 
Determine el conjunto de todos los puntos $(a,b)$ en donde la siguiente función es continua 

$$
f(x,y)= \left \{  \begin{array}{ccc}
y-x^2 & si & y > x^2 \\
\\ 0 & si & y = x^2 \\
\\ x - y & si & y < x^2 
    \end{array}
\right.
$$

Sobre la parábola debemos asegurar continuidad ya que $y - x^2$ es continua bajo la parábola podemos asegurar continuidad ya que $x-y$ es continua.

Por Lo tanto debemos analizar continuidad en los puntos que forman la parábola.


### Recuerdo:
$$
f(x) = \left \{ \begin{array}{cc}
    x+2 & x \geq 2 \\
    \\ \cfrac{x^2-4}{x-2} & x < 2 \\
    \end{array} \right.
$$


De qué forma representamos un límite a la parábola?

La parábola es de la forma $y = x^2$, por lo tanto podemos representar los puntos de la parábola como $(a, a^2)$.

luego el límite sería:

$$
{\lim_{(x,y)\to(a,a^2)}{y - x^2}}_{y>x^2} =
$$

$y > x^2$ nos permite aproximarnos por un lado de la parábola. 

<img src="./pic1.png" alt="Gráfico" style="height: 300px; width:300px; display: block; margin-left: auto; margin-right: auto;"/>

Determine el conjunto de todos los puntos $(x,y)$ en donde la siguiente función es continua.

$$
f(x,y) = \left \{ \begin{array}{cc} 
    2x^2 + xy - y^2 & y >x \\
    \\ x - \cfrac{y}{2} & y \leq x \\
    \end{array}
    \right.
$$
<br>
<br>

$$
{\lim_{(x,y)\to (a,a)} 2x^2 + xy - y^2}_{ 
y > x }
$$

$$
2a^2 + a^2 - a^2 = 2a^2
$$

$$
{\lim_{(x,y)\to (a,a)} x - \cfrac y 2}_{ 
y \leq x }
$$

$$
a - \cfrac a 2 = \cfrac a 2
$$

Igualamos los límites

$$
\cfrac a 2 = 2a^2
$$



Por lo tanto la función no es continua.
