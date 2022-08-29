# MaxSubArray()

## Descripción del problema

El problema del **subarreglo máximo** consiste en, dado un arreglo $A$ de una
cantidad de elementos relativa $n$.

$$
A: [A_1, A_2, ..., A_n]
$$

Buscamos un subarreglo $B$ de al menos un elemento, de forma que la suma de sus
elementos sea la mayor entre todos los posibles subarreglos de $A$.  cumpliendo
para cada valor $A_n \in \mathbb R$.

Nuestra primera solución sería calcular todos los subarreglos posibles y
repetir para los segundos números. Sin embargo esto no sería óptimo ya
que tendría complejidad $O(n^3)$ .

```python
for i in range (n-1):
    for j in range(i, n-1):
        for k in range (i, j):
            ...
```

Podemos ahorrar tiempo guardando la suma del subarreglo anterior y le sumamos el
número extra. Esto reduce la cantidad de cálculos y la cota asintótica a
$O(n^2)$.

```python
sum = 0
currentSum = 0
for i in range (n-1):
    for j in range(i, n-1):
        currentSum += num[j];
```

Es necesario calcular cada subarray pasando por cada posible subarreglo?
No es mandatorio. Podemos recorrer el arreglo y descartar todos los valores
negativos antes de cada valor positivo. Entonces podemos movernos hasta el
primer valor positivo sin complicaciones. Esto se conoce como el algoritmo de
Kadane y tiene una complejidad  $O(n)$.

## Descripción del algoritmo

Existen distintas formas de resolver este problema, distintos algoritmos con
distintos tiempos de ejecución. En el presente informe trabajaremos con la
solución recursiva y posteriormente la compararemos con el algoritmo de Kadane.

Dado un arreglo $A$ de largo $n$, buscamos un punto medio $c$. El cual se
utiliza con el objetivo de fraccionar el arreglo $A$ en dos subarreglos $L$ y
$R$.

$$
L = [A_1, A_2, \space \dots \space, A_{c-1}]
$$

$$
R = [A_c, A_{c+1}, \space \dots \space, A_n]
$$

En este punto si buscamos la solución tenemos tres posibles casos

El subarreglo máximo:

* Es un subarreglo de $L$
* Es un subarreglo de $R$
* Está entre los dos subarreglos

El arreglo central $C$ es revisado de manera lineal. Mientras que los arreglos
$L$ y $R$ son revisados de manera recursiva, estos se dividen hasta llegar al
caso base.

### Caso base

El caso base se da cuando la longitud del arreglo es de un elemento, donde la
suma máxmia es su único elemento.

#### Revisión  del  arreglo central $C$

Recorremos el subarreglo $A$ desde el centro hasta los extremos, sin importar
el orden.

Para ambos casos, al pasar por un elemento revisamos si la suma sería mayor
con ese número, de ser así, lo incluímos en el subarreglo máximo.

Al finalizar retornamos la suma entre el sector izquierdo y el sector derecho,
junto con los índices que indican los límites del subarreglo máximo.

### Conclusión del algoritmo

Para finalizar, retornamos la mayor entre la suma central, la suma izquierda y
la suma derecha.

## Implementación

```c```

### Ejemplo de ejecución

```python
[1, -2, 3] {
  Recursión izquierda [1] {
    [1]: Caso base
  } Resultado:  1 [1]

  Recursión derecha [-2, 3] {
      Recursión izquierda [-2] {
        [-2]: Caso base
      } Resultado:  -2 [-2]

      Recursión derecha [3] {
        [3]: Caso base
      } Resultado:  [3]

      Recursión centro [-2, 3] {
        Recorrido izquierda: 
          Pasando por -2
            Incluyo
        Recorrido derecha: 
          Pasando por 3
            Incluyo
      } Resultado 1 [-2, 3]

  } Resultado:  [3]

  Recursión centro [1, -2, 3] {
    Recorrido izquierda: 
      Pasando por 1
        Incluyo
    Recorrido derecha: 
      Pasando por -2
        Incluyo
      Pasando por 3
        Incluyo
  } Resultado 2 [1, -2, 3]

} Resultado 3 [3]
```

## Ejemplo detallado del algoritmo

Para el caso de $A: [1, -2, 3]$ dividimos en el punto central, obteniendo los
subarreglos

$$L: [1]$$

$$R: [-2, 3]$$

Trabajando con $L:$

* Caso base, retornamos el valor y su posición, $(Suma, l, r) = (1, 0, 1)$
* Obtenemos $L = [1]$

Trabajando con $R:$

* Dividimos en
  * $R_L: [-2]$
    * Caso base
  * $R_R: [3]$
    * Caso Base
* Entre $R_L$ y $R_R$ nos quedamos con el mayor $R_R = [3]$
* Obtenemos $R = [3]$

Trabajando con $C$

* Iteramos del centro a la izquierda
  * Pasamos por el 1 y lo incluimos pues es el primer valor que encontramos
* Iteramos del centro a la derecha
  * Pasamos por el -2 y lo incluimos pues es el primer valor que nos
  encontramos
  * Pasamos por el 3 y lo incluimos pues aumenta el valor de nuestra suma total
* Obtenemos $C: [1, -2, 3]$

Comparamos los resultados:

Entre $L, R, C$ nos quedamos con el mayor.

$$
( sum(L) = 1 ) < (sum(C) = 2) < (sum(R) = 3)
$$

Obteniendo así como resultado el subarreglo $R = [3]$

## Correctitud del algoritmo

### Función `maxCenter`

La función `maxCenter` es un algoritmo iterativo con complejidad
$O(n)$. Para determinar si esta función es correcta es conveniente utilizar la
propiedad invariante del bucle.

Recordar que este algoritmo trabaja desde el centro del arreglo a sus extremos.
Es decir, se recorre a la izquierda con un ciclo y a la derecha con otro.

Para cada bucle necesitamos dos datos. Definimos la **suma** $S$ como la suma
de todos los elementos visitados y la **suma maxima** $SM$ como la suma que posee
sólo los elementos que maximizan la suma.

**Propiedad invariante**: En todo momento la suma máxima será menor o igual a la
suma de todos los elementos. Es decir $S \leq SM$.

Utilizamos un contador $i$ para recorrer el arreglo .Tanto del centro a la
izquierda como del centro a la derecha

* $L: [A_{l,}...,A_{c-1}]$
(de derecha a izquierda).

* $R: [A_c, ...,  A_r]$ (de izquierda a derecha);

**Inicialización**: La suma total es 0 y máxima ya que no ha sido visitado ningún
elemento del arreglo $A$. $S = SM$.

**Mantención**: En cada iteración tenemos dos posibles casos

* El elemento actual aumenta el valor de la suma
  * Le asignamos el valor $S = SM$
  * Actualizamos el límite para que incluya
    el nuevo valor
* El elemento actual **no** aumenta el valor de la suma.
  * Mantenemos $SM$ intacto
  * Se cumple que ${S} < {SM}$

Para finalizar la iteración aumentamos en $1$ el valor de $i$.

**Finalización**:  Al finalizar se ha recorrido la totalidad del brazo

* $i == l$ en el brazo izquierdo
* $i == r - 1$ en el brazo derecho

Por lo que $SM$ posee la suma total máxima de todos los elementos recorridos.
Finalmente retornamos el valor de la suma máxima, así como los límites de los
brazos izquierdo y derecho.

### Tiempo de ejecución del algoritmo maxSubArray

El algoritmo maxSubArray realiza dos llamadas recursivas con un problema cuyo
tamaño es la mitad del problema inicial. Además de la llamada a la función
`maxCenter`. Cuya complejidad es de $O(n)$. De esto obtenemos que la función de
recurrencia del algoritmo `maxSubArray` es la siguiente:

$$
T(n) \leq 2\cdot T \left ( n/2 \right ) + O(n)
$$

Este algoritmo tiene la particularidad de cumplir con el teorema maestro.

El cual nos dice que para toda función de recursión de la forma

$$
T(n) \leq a \cdot T  \left ( n/b \right) + O(n^c)
$$

La complejidad estará dada por:

* $O(n^c \cdot \log n)$ En el caso de que $a = b^c$
* $O(n^c)$ En el caso de que $a < b^c$
* $O(n^{\log_b a})$ En el caso de que $a > b^c$

En el caso del algoritmo del sub arreglo máximo recursivo. Los valores de
$a, b, c$ serían:

$$
a = 2 \\
b = 2 \\
c = 1
$$

$$a = b^c = 2$$

De lo anterior se obtiene que:
$$T(n) = O(n^c \cdot \log n) = O(n \log n)$$

### Prueba por inducción

Asumimos que $T(n) \leq O(n \log n)$.

$$
T(n) \leq 2 \cdot T(n/2) + c_1n \\
$$
  
$$
T(n) \leq c_2 n \log (n) \\
T(n/2) \leq c_2 (n/2) \cdot \log (n/2) \\
T(n/2) \leq c_2 (n/2)  \cdot (\log n - \log_2(2)) \\
T(n/2) \leq c_2 (n/2)  \cdot (\log n - 1) \\
$$

$$
T(n) \leq 2 \cdot T(n/2) + c_1n \\
T(n) \leq 2 \cdot  (c_2 (n/2)  \cdot (\log n - 1))+ c_1n \\
T(n) \leq (c_2 n  \cdot (\log (n) - 1))+ c_1n \\
T(n) \leq n((c_2  \cdot (\log (n) - 1))+ c_1) \\
c_2n\log (n) \leq n((c_2  \cdot (\log (n) - 1))+ c_1) \\
c_2\log (n) \leq (c_2  \cdot (\log (n) - 1))+ c_1 \\
c_2\log (n) - c_2  \cdot \log (n) + c_2 \leq c_1 \\
0 \leq c_1 - c_2 \\
c_2 \leq c_1 \\
$$

## Experimentos

### Comparación con el algoritmo de Kadane

El algoritmo de Kadane consiste en recorrer linealmente el
arreglo como si fuera una cortina. Se actualizan a medida que uno
se desplaza por el arreglo los limites izquierdo y derecho.


```c```

Del gráfico podemos observar que efectivamente el algoritmo de Kadane
es mucho más rápido que el algoritmo recursivo para el problema del
sub-arreglo máximo.

### Nivel de recursión máximo

Para cada llamada recursiva compararemos el nivel de la llamada actual
con el nivel máximo alcanzado. De esta manera obtendremos el nivel
máximo de recursividad dependiendo del tamaño del arreglo $n$.

Se espera que el nivel de recursiones converga a un valor específico

Podemos interpretar que no existe un valor al que converja el número de recursiones. Al parecer, este depende de $n$ de forma que $lvl(n) = c \cdot n \log n$. Sin embargo demostrar esto requiere más experimentos.
