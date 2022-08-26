# Análisis del algoritmo Merge Sort

## Problema de ordenamiento

El problema de ordenamiento consiste en, valga la redundancia, ordenar un
arreglo determinado de menor a mayor, o al revés. Naturalmente este puede
ser resuelto computacionalmente por medio de distintos algoritmos de
variable velocidad. Merge Sort es uno de estos algoritmos y será caso de
estudio en el presente informe. Se implementará el algoritmo así como una
salida detallada del proceso de ordenamiento, se comprobará la correctitud
del mismo y se analizarán sus tiempos de ejecución en relación a otros
algoritmos.

Como todo algoritmo de ordenamiento, MergeSort recibe una entrada $A$ que
se define como una secuencia de $n$ elementos.

$$
A = [a_1, a_2, ..., a_n]
$$

Luego de procesar los datos, se retorna un arreglo $A'$ con sus elementos
ordenados secuencialmente.
$$
A' = [a'_1, a_2', ...,a_n'] \\

a_1' \leq a_2' \leq ... \leq a_n'
$$

## Descripción del algoritmo

Merge Sort está basado en el paradigma de diseño *"divide y conquistarás".* Se
divide repetidamente el arreglo $A$ en subarreglos de longitud $n/2$. Se
ordenan estos subarreglos por medio de recursión (se llama al mismo algoritmo
para que resuelva el subarreglo). Posteriormente estos dos subarreglos son
mezclados para entregar la solución final al problema.

Para implementar el algoritmo entonces es necesario definir dos funciones.
La función `mergeSort(A)` se encargará de recibir el arreglo y de realizar
los llamados recursivos. Mientras que la función `merge(A, left, right)` se
encargará de mezclar dos subarreglos `left, right` en el arreglo principal
$A$.

Con el fin de facilitar el análisis del algoritmo se añadirá un contador
`compareCount` que cuenta el número de comparaciones que realiza la función
`merge`. Así como el contador `mergeCount` que  contará el número de llamadas
recursivas a la función `mergeSort()`;

```python
compareCount = 0;
mergeCount = 0;

def merge(a, l, r):
    global compareCount;
    i = j = k = 0
    while (i < len(l) and j < len(r)):
        if l[i] > r[j]:
            a[k] = r[j];
            j+=1
        else:
            a[k] = l[i]
            i+=1
        compareCount += 1
        k+=1
    while (len(l) > i):
        a[k] = l[i]
        compareCount += 1
        i+=1
        k+=1

    while(len(r) > j):
        compareCount += 1
        i+=1
        a[k] = r[j]
        j+=1
        k+=1
    return a

def mergeSort(a):
    global mergeCount;
    n = len(a); # Obtenemos la longitud del arreglo
    if n == 1: return a;
    h = n//2;   # Obtenemos un punto medio en el arreglo


    # Dividimos el arreglo
    m1 = a[:h]  
    m2 = a[h:]

    print(a, m1, m2)
    
    # Ordenamos los sub-arreglos
    m1 = mergeSort(m1)
    m2 = mergeSort(m2)

    mergeCount += 2; # Contamos las llamadas recursivas

    return merge(a, m1, m2)

print(mergeSort([random.randint(1,1000) for n in range(1, 1000)]))
print(mergeCount, compareCount);
```

MergeSort consiste en dividir el arreglo en dos subarreglos de tamaño $n/2$
los cuales son ordenados dividiéndose en dos subarreglos cada uno (de longitud
$n/4, n/8, ..., 1$). Así sucesivamente hasta llegar al caso base. El cual se da
cuando la longitud del subarreglo a ordenar es de $1$ (que está ordenado).
La función `merge` recibe los subarreglos y los ordena. Para esto
recorre cada subarreglo por separado y compara sus elementos, añadiendo el menor.

## Correctitud: `merge()`

El índice $k$ nos indica la posición actual por la
que nos desplazamos en el arreglo de salida $A$,
que está formado por los elementos $A[k .. n]$ siendo $n$ la suma entre $n_1$
y $n_2$, que son la longitud del subarreglo ordenado izquierdo $L$ y  el derecho
$R$ respectivamente.

Planteamos como invariante de ciclo que el subarreglo $A[0..k]$ siempre estará ordenado.

**Inicialización**: En una primera instancia el arreglo $A$ se encuentra vacío,
así que está completamente ordenado. $k = 0$ por lo que el subarreglo $A[0..k]$
tiene 0 elementos.

**Mantención**: En la posición $k$ del arreglo $A$ se almacenará el menor de los
elementos de los arreglos $L$ y $R$. Sabemos que estamos trabajando con el menor
elemento ya que el arreglo $L$ y $R$ fueron previamente ordenados por la función
`mergeSort()`.

**Finalización**: El ciclo finaliza cuando $k= n_1 + n_2$. A estas alturas
el subarreglo ordenado $A[0..k]$ constituye la totalidad del arreglo $A$. Por
lo que la totalidad de $A$ está ordenado.

## Correctitud del algoritmo mergeSort

Probar la correctitud de la función merge es un gran paso para saber si el
algoritmo mergeSort es correcto. Definimos $P(n)$ como la hipótesis de que
la función mergeSort ordena una secuencia de $n$ elementos de menor a mayor.

### Caso base

Establecemos como caso base $P(1)$ como ordenar una secuencia de un elemento.
Naturalmente, este arreglo está ordenado. Por lo que se cumple $P$ para $P(1)$.

### Paso inductivo

Definimos $m$ como un tamaño de un subarreglo menor a $n$. Como por ejemplo
$n/2$. Deducimos que $P(m)$ es correcto ya que sabemos que la función
`merge` es correcta, lo que quiere decir que podemos asumir que los subarreglos
han sido ordenados de manera correcta (Sabiendo que se construye desde el
caso base). Debido a que $P(m)$ es correcto podemos concluir que $P(n)$ lo es.
Ya que $m<n$.

## Tiempo de ejecución del algoritmo

Definimos $T(n)$ como aquella función que nos retorna el tiempo de ejecución
de la función `mergeSort()`. Como sabemos, la función `mergeSort` realiza dos
llamadas recursivas y una llamada a la función `merge`.

### Tiempo de ejecución de la función Merge

La función Merge busca el menor elemento entre los dos arreglos iterándolos
hasta que uno de los dos se acabe por medio de un ciclo while el cual toma
$O(n_1 || n_2)$ = $O(n)$. Para finalizar otro ciclo while recorre los $n$
elementos restantes. De esto obtenemos que el tiempo de ejecución de la
función merge es $O(n)$

### Tiempo de ejecución de la función mergeSort

Ahora que se conoce el tiempo de ejecución de Merge sabemos que el
tiempo de ejecución de mergeSort $T(n)$ está condicionado por dos llamadas
recursivas $T(n/2)$ así como de la función merge de tiempo $O(n)$. Quedando
de la siguiente manera (descartamos aquellas instrucciones de tiempo constante $c$)

$$
T(n) = T(n/2) + T(n/2) + O(n)
$$

$$
T(n) = 2T(n/2) + O(n)
$$

Podemos obtener el tiempo de ejecución de la función `mergeSort` analizando su
árbol de recursividad

![tree.png](tree.png)

Observemos que la suma de cada nivel es de $cn$. Como la función `mergeSort`
divide cada subarreglo en dos partes de longitud $n/2$ hasta llegar al caso
base, podemos decir que la altura de este árbol es de $log(n)$. Por lo que
el tiempo de ejecución total sería base por altura $cn \cdot log(n)$. De
esto concluimos que el tiempo de ejecución de la función `mergeSort` es de
$O(n\log(n))$.

## Experimentos

### Variación en el número de comparaciones con el mejor y peor caso teóricos

#### Peor caso teórico

El peor caso se dará cuando mergeSort tenga que realizar la mayor cantidad de
comparaciones. Esto se da cuando los subarreglos $L$ y $R$ tienen elementos
alternados entre sí. Consideremos por ejemplo los arreglos $L = [1,3,5]$ y
$R = [2,4,6]$. En este caso cada elemento deberá ser comparado al menos una
vez con cada elemento

#### Mejor caso teórico

El mejor caso se da cuando el mayor elemento de uno de los subarreglos es menor
que el primer elemento del otro subarreglo. Esto reduce el número de comparaciones
de cada paso en el Merge a $n/2$.

Si bien tanto el mejor como el peor caso presentan variaciones en el tiempo de ejecución
En la función merge, estas variaciones no son suficientes para cambiar el tiempo
de ejecución del algoritmo. Es decir, tanto como para el mejor como para el peor
caso el tiempo de ejecución de la subrutina merge seguirá siendo $O(n)$.

```python
from random import randint
from matplotlib import pyplot as plt
from math import log2
samples = 50;

worst = best = [n * log2(n) for n in range(samples)];

m = [randint(1, samples) for n in range(samples)]

x = [n for n in range(samples)];


plt.plot(x, worst);
plt.plot(x, m);
plt.plot(x, best);
plt.legend(["Peor caso teórico", "Merge Sort", "Mejor caso teórico"]);
```

### Comparación con InsertionSort

```python
x = [n for n in range (samples)];
ym = []
yi = []
for i in range(samples):
    
```


### Análisis de los resultados obtenidos
