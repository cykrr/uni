# Análisis del algoritmo Merge Sort

## Problema de ordenamiento

El problema de ordenamiento consiste en, valga la redundancia, ordenar un
arreglo determinado de menor a mayor, o al revés. Naturalmente este puede
ser resuelto computacionalmente por medio de distintos algoritmos de
variable velocidad. Merge Sort es uno de estos algoritmos y será caso de
estudio en el presente informe. Se implementará el algoritmo así como una
salida detallada del proceso de ordenamiento, se comprobará la correctitud
del mismo y se analizarán sus tiempos de ejecución en relación a otros algoritmos

Como todo algoritmo de ordenamiento, MergeSort recibe una entrada $A$ que
se define como una secuencia de $n$ elementos.

$$
A = [a_1, a_2, ..., a_n]
$$

Luego de procesar los datos, se nos retorna un arreglo $A'$ con sus elementos ordenados
secuencialmente.
$$
A' = [a'_1, a_2', ...,a_n'] \\

a_1' \leq a_2' \leq ... \leq a_n'
$$

## Descripción del algoritmo

Merge Sort está basado en el paradigma de diseño "divide y conquistarás". Se
divide repetidamente el arreglo $A$ en subarreglos de longitud $n/2$. Se
ordenan estos subarreglos por medio de recursión (se llama al mismo algoritmo
para que resuelva el subarreglo). Posteriormente estos dos subarreglos son
mezclados para entregar la solución final al problema.

Para implementar el algoritmo entonces es necesario definir dos funciones.
La función `mergeSort(A)` se encargará de recibir el arreglo y de realizar
los llamados recursivos. Mientras que la función `merge(A, left, right)` se
encargará de mezclar dos subarreglos `left, right` en el arreglo principal
$A$.

```python
def merge(a, l, r):
    i = j = k = 0
    while (len(l) > i, j < len(r)):
        if l[i] > r[j]:
            a[k] = r[j];
            j+=1
        elif l[i] < r[j]:
            a[k] = l[i]
            i+=1
        k+=1
    return a

def mergeSort(a):
    n = len(a); # Obtenemos la longitud del arreglo
    h = n//2;   # Obtenemos un punto medio en el arreglo

    # Dividimos el arreglo
    m1 = a[:h]  
    m2 = a[h:]
    
    # Ordenamos los sub-arreglos
    m1 = mergeSort(m1)
    m2 = mergeSort(m2)

    return merge(m1, m2)
```

## Descripción del algoritmo

MergeSort consiste en dividir el arreglo en dos subarreglos de tamaño $n/2$
los cuales son ordenados dividiéndose en dos subarreglos cada uno (de longitud
$n/4$). Así sucesivamente hasta llegar al caso base. El cual se da cuando la
longitud del subarreglo a ordenar es de $1$. Donde el arreglo ordenado es sí
mismo
```python
def merge(a, l, r):
    i = j = k = 0
    while (i < len(l) and j < len(r)):
        if l[i] > r[j]:
            a[k] = r[j];
            j+=1
        else:
            a[k] = l[i]
            i+=1
        k+=1
    while (len(l) > i):
        a[k] = l[i]
        i+=1
        k+=1
    while(len(r) > j):
        a[k] = r[j]
        j+=1
        k+=1
    return a

def mergeSort(a):
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

    return merge(a, m1, m2)

print(mergeSort([random.randint(1,1000) for n in range(1, 35)]))
```
