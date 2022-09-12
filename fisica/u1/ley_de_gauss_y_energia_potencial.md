# Ley de Gauss, la energía potencial y cinética de una carga, y el potencial eléctrico

## Motivación

- Ver que propone la Ley de Gauss y como aplicarla. Posteriormente, definir la
  energía potencial eléctrica, su relación con la energía cinética de una carga,
  y la posterior definición de potencial eléctrico. A partir de aquí, relacionar
  esta cantidad con el campo eléctrico.

## Carga cerrada por una superficie no esférica

Consideremos a la carga anterior, **encerrada ahora además por una superficie
irregular.**

Sobre esta nueva superficie, **se escoge una sección de Área**, que estará por
encima de nuestra primera esfera imaginaria.

Sin embargo, el campo eléctrico que cuenta, pasa por las partes donde el área es
completamente perpendicular al campo

Los únicos lugares donde ocurre aquello, es donde la superficie nueva se
proyecte completamente sobre la esfera. Como el campo atraviesa simplemente otra
esfera de mayor área, **decimos que en ambos casos el flujo es el mismo.**

## Ley de Gauss

Para **cualquier** distribución de carga o cuerpo cargado **y encerrado
completamente** por una superficie:

$$
\phi_E = \oint {
    \vec E
    \cdot
    d\vecA
} =

\cfrac {
    Q_\text{enc}
} {
    \varepsilon_0
}
$$

Se dice que el flujo que atraviesa esta superficie es igual a la carga
encerrada, dividida entre la permeabilidad eléctrica en el vacío.

Existen dos casos de interés: **si el campo es uniforme, o si este no depende de
las coordenadas del diferencial**. En ambos casos, el campo eléctrico puede
sacarse de la integral, y la integral de superficie se convierte en el área
total que se estudia (por lo tanto, volvemos al producto punto habitual).

Por otro lado, asumiremos siempre que la carga eléctrica dentro de la superficie
se distribuye **homogéneamente**.

## Aplicación

Lo siguiente es una especie de algoritmo para emplear la Ley de Gauss. Aunque no
lo parezca, **esta Ley es equivalente a la Ley de Coulomb**, pero su formulación
esta motivada por la **geometría del objeto cargado que se estudia y sus
simetrías**.

La Ley de Gauss se emplea usualmente para calcular el campo eléctrico de un
objeto cargado. De este objeto se estudia el campo eléctrico tanto en su
interior como en el exterior de este. Para hacerlo:

1. Se define una “Superficie Gaussiana”. Esta superficie se dibuja dentro o
   fuera del objeto cargado, dependiendo donde queramos estudiar el campo. Su
   forma tiene relación con la del cuerpo estudiado.

2. Estudiamos si el campo es uniforme o no sobre la superficie que va a
   atravesar. Esto puede facilitar los cálculos. Luego, procedemos a calcular el
   flujo eléctrico que atraviesa esta “Superficie Gaussiana”.

3. Una vez calculamos el flujo, ahora debemos calcular la carga encerrada en el
   cuerpo cargado. La carga encerrada a su vez, se relaciona con la densidad de
   carga en el cuerpo. Si nos interesa el campo dentro del cuerpo estudiado, la
   carga encerrada será siempre una porción de la carga total, que debemos
   calcular. Si nos interesa el campo fuera del cuerpo estudiado, la carga
   encerrada en este caso será siempre la carga total contenida en el cuerpo.
   Luego, se procede a despejar el campo eléctrico a partir del flujo.

### Ejemplo: campo eléctrico de una esfera sólida

Se distribuye uniformemente una carga $Q$ en el interior de una esfera solida.
Calcule el campo eléctrico tanto fuera como dentro de la esfera –ósea, en todo
el espacio-.

#### La energía potencial y cinética de una carga eléctrica

Estudiemos la situación de la imagen, donde la carga $q$, ejerce una fuerza
sobre $q0$, desplazándola desde un punto $A$ hasta otro $B$. La fuerza total que
siente $q0$ es:

Supongamos que esta fuerza provoca un desplazamiento en $q0$. Podríamos decir
que el trabajo necesario para desplazar esta carga, bajo la acción de esta
fuerza hecha por $q$, es:

◦ Supongamos que ahora, el desplazamiento provocado en la carga $q0$ es
infinitesimalmente pequeño. Por lo tanto, el trabajo sobre ella también lo es, y
la formula anterior cambia a:

◦ Por lo tanto, el trabajo total que siente una carga eléctrica $q0$, bajo un
campo eléctrico emitido por $q$, es:

◦ La siguiente cantidad se define como la energía potencial eléctrica de una
carga. Es la responsable de mantener a una carga eléctrica en una posición fija:

◦ Podemos notar entonces que el trabajo necesario para mover una carga $q0$,
desde un punto $A$ hasta otro $B$, no es más que el negativo del cambio en la
energía potencial entre ambos puntos:

◦ Por otro lado, podemos tomar la segunda Ley de Newton como tal, y procedemos
de la misma forma:

◦ Y ahora integramos para obtener el trabajo:

◦ Notamos que en este caso, el trabajo es igual al cambio en la energía cinética
de la carga $q0$, entre los puntos $A$ y $B$. Podemos igualar este resultado de
trabajo con el anterior, para llegar a un resultado interesante:

◦ Concluimos que la energía mecánica -o total-, igual a la suma de la energía
potencial mas cinética, tanto al inicio como al final del desplazamiento, es la
misma. Por lo tanto, para una carga eléctrica, la energía se conserva.

El potencial eléctrico ◦ Si dividimos el trabajo total en la magnitud de la
carga de prueba, se obtiene:

◦ Se define la siguiente cantidad $V$, como el potencial eléctrico, y la
ecuación anterior se transforma en:

◦ Podemos comparar la última ecuación, con la ecuación de trabajo en términos
del campo eléctrico:

◦ Podemos igualar para obtener lo siguiente:

◦ Y se dice que la diferencia de potencial eléctrico depende del campo
eléctrico. Esto asumiendo que el vector $E$ se conoce. Si lo que se conoce es la
diferencia de potencial y la función que la describe, entonces podemos conocer
al vector $E$, reescribiendo la ecuación anterior como:

◦ Como los limites de ambas integrales son iguales, entonces sus argumentos
deben ser iguales también:

◦ Y el campo eléctrico a partir del potencial, se define como el negativo de su
gradiente:
