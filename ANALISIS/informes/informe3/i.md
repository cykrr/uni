# MaxSubArray()

## Descripción del problema

El problema del **subarreglo máximo** consiste en, dado un arreglo $A$ de una cantidad de elementos relativa $n$.

$$
A: [A_1, A_2, ..., A_n]
$$

Buscamos un subarreglo $B$ de al menos un elemento, de forma que la suma de sus elementos sea la mayor entre todos
los posibles subarreglos de $A$.  cumpliendo para cada valor $A_n \in \mathbb R$ .

Nuestra primera solución sería calcular todos los subarreglos posibles y
repetir para los segundos números. Sin embargo esto no sería óptimo ya
que tendría complejidad $O(n^3)$ .

```python
for i in range (n-1):
    for j in range(i, n-1):
        for k in range (i, j):
            ...
```

Podemos ahorrar tiempo guardando la suma del subarreglo anterior y le sumamos el número extra.
Esto reduce la cantidad de cálculos y la cota asintótica a $O(n^2)$.

```python
sum = 0
currentSum = 0
for i in range (n-1):
    for j in range(i, n-1):
        currentSum += num[j];
```

Es necesario calcular cada subarray pasando por cada posible subarreglo? 
No es mandatorio. Podemos recorrer el arreglo y descartar todos los valores negativos
antes de cada valor positivo. Entonces podemos movernos hasta el primer valor positivo
sin complicaciones. Esto se conoce como el algoritmo de Kadane y tiene una complejidad 
$O(n)$.

## Descripción del algoritmo

Existen distintas formas de resolver este problema, distintos algoritmos con distintos tiempos de ejecución. En el presente informe trabajaremos con la solución recursiva y posteriormente la compararemos con el algoritmo de Kadane.

Dado un arreglo $A$ de largo $n$, buscamos un punto medio $c$. El cual se utiliza con el objetivo de fraccionar
el arreglo $A$ en dos subarreglos $L$ y $R$.

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

El arreglo central $C$ es revisado de manera lineal. Mientras que los arreglos $L$ y $R$ son revisados de manera recursiva,
estos se dividen hasta llegar al caso base.

#### Caso base:

El caso base se da cuando la longitud del arreglo es de un elemento, donde la suma máxmia es su único elemento.

#### Revisión  del  arreglo central $C$

Recorremos el subarreglo $A$ desde el centro hasta los extremos, sin importar el orden.

Para ambos casos, al pasar por un elemento revisamos si la suma sería mayor con ese número, de ser así, lo incluímos en el
subarreglo máximo.


Al finalizar retornamos la suma entre el sector izquierdo y el sector derecho, junto con los índices que indican
los límites del subarreglo máximo.

### Conclusión del algoritmo
Para finalizar, retornamos la mayor entre la suma central, la suma izquierda y la suma derecha.

## Implementación

```python
import math
def maxCenter(a, c, l, r, level = 0, Verbose = False):
#    if Verbose: print(a[l:r])
    ls = -math.inf
    rs = -math.inf
    s = 0 
    ll = c-1
    lr = c
    rl = c 
    rr = len(a)
    if Verbose: print (" " * level * 2 + "Recorrido izquierda: ");
    for i in range (c-1, l-1, -1):
        if Verbose: print(" " * (level + 1)* 2 + "Pasando por " + str(a[i]))
        s += a[i]
        if ls < s:
            if Verbose: print(" " * (level + 2) * 2 + "Incluyo")
            ls = s;
            ll = i
        else: 
            if Verbose: print(" " * (level + 2) * 2 + "No Incluyo")
    s = 0;
    if Verbose: print (" " * level * 2 + "Recorrido derecha: ");
    for i in range (c, r):
        if Verbose: print(" " * (level + 1)* 2 + "Pasando por " + str(a[i]))
        s += a[i]
        if rs < s:
            if Verbose: print(" " * (level + 2) * 2 + "Incluyo")
            rs = s
            rr = i+1
        else: 
            if Verbose: print(" " * (level + 2) * 2 + "No Incluyo")

    return ls + rs, ll, rr;

    
        
        
def maxSubArray(a, l = -1, r = -1, level = 0, Verbose = False):
    if l == -1 and r == -1:
      l = 0;
      r = len(a);

    if ( r-l == 1):
      if Verbose: print(a[l:r], "{")
      if Verbose: print(" " * 2 * level + str(a[l:r]) + ": Caso base")
      return a[r-1], l, r 

    if Verbose: print(a[l:r], "{")
#    if Verbose: print("L: ", l, "R: ", r)

    c = (l + r) // 2

    level +=1

    if Verbose: print(" " * level * 2 + "Recursión izquierda ", end = "")
    ls, ll, lr = maxSubArray(a, l, c, level = level + 1, Verbose = Verbose);
    if Verbose: print (" " * level * 2 + "} Resultado: ", ls, a[ll:lr])
    if Verbose: print()
    if Verbose: print(" " * level * 2 + "Recursión derecha ", end = "")
    rs, rl, rr = maxSubArray(a, c , r, level = level + 1, Verbose = Verbose);
    if Verbose: print (" " * level * 2 + "} Resultado: ", a[rl:rr])
    if Verbose: print()
#    if Verbose: print ("rs", rs, rl, rr, a[c:], a[rl:rr])
    if Verbose: print(" " * level * 2 + "Recursión centro " + str(a[l:r]) + " {")
    cs, cl, cr = maxCenter(a, c, l, r, level = level + 1, Verbose = Verbose)
    if Verbose: print(" " * level * 2 + "} Resultado " + str(cs) + " " + str(a[l:r]))
    if Verbose: print()
    level -= 1
    m = max (cs, ls, rs)
    if m == cs:
        return cs, cl, cr;
    elif m == ls:
        return ls, ll, lr
    elif m == rs:
        return rs, rl, rr;

#a = [1, 2, 3, -8, 2, 3, -2, 2, 3, -5, 8, 1, -3, 1, 5, -8, -9, 10, 1, -1, -2, 7]
#a = [-2, -5, -6, 1, 2, 3]
#a =  [1, 2, 5, -1,  6, 3]
#a = [1, -2, 3]
a = [1, -2]
#a = [1,2,3, -2, -5, -6]
#a = [1, 2, 3, 2, 5,6,7,8,9,10]
s, b, c = maxSubArray(a, Verbose = True)
print("} Resultado", s,a[b:c])
```

*Results:*
```python
[1, -2] {
  Recursión izquierda [1] {
    [1]: Caso base
  } Resultado:  1 [1]

  Recursión derecha [-2] {
    [-2]: Caso base
  } Resultado:  [-2]

  Recursión centro [1, -2] {
    Recorrido izquierda: 
      Pasando por 1
        Incluyo
    Recorrido derecha: 
      Pasando por -2
        Incluyo
  } Resultado -1 [1, -2]

} Resultado 1 [1]
```

## Ejemplo de ejecución


## Ejemplo detallado del algoritmo

Para el caso de $A: [1, -2, 3]$ dividimos en el punto central, obteniendo los subarreglos 
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
    * Pasamos por el -2 y lo incluimos pues es el primer valor que nos encontramos
    * Pasamos por el 3 y lo incluimos pues aumenta el valor de nuestra suma total
  * Obtenemos $C: [1, -2, 3]$

Comparamos los resultados:

Entre $L, R, C$ nos quedamos con el mayor.

$$
( sum(L) = 1 ) < (sum(C) = 2) < (sum(R) = 3)
$$

Obteniendo así como resultado el subarreglo $R = [3]$ 