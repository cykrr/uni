# Informe 1

[Guía para trabajar en informe 1](https://github.com/rilianx/ADA/blob/main/Gu%C3%ADas%)

## Problema de ordenamiento

**Entrada**: Secuencia de n números $[a_1, a_2, ..., a_n]$

**Salida**: Permutación ordenada de la secuencia de entrada: $[a_1', a_2', ..., a_n']$

El problema de ordenamiento es uno de los problemas más estudiados en el campo
de las ciencias de la computación. Este es resuelto por medio de distintos
algoritmos, los cuales se comportan de mejor o peor manera dependiendo de la
cantidad de elementos. En el presente informe se analizará el comportamiento del
algoritmo **Insertion Sort**

## Insertion Sort

```python
def sort(a: list, verbose: bool = False):
    n = len(a)
    if verbose: print("Arreglo", a, ":")
    for i in range(1, n):
        if verbose: print(a)
        for j in range(0, i):
            if a[i] < a[j]:
                if verbose:
                    print(a)
                    print ("swap: (", a[i], ",", a[j], ")")
                a[i], a[j] = a[j], a[i]
    return a
    
```

## Descripción del algoritmo

El Insertion Sort consiste en recorrer el arreglo de izquierda a derecha. Cada
elemento será comparado con los elementos a su izquierda y movido hasta que su
posición sea la correcta.

Se recibe una lista $a$ con una serie de $n$ elementos a ser ordenados. Estos son
ordenados dentro de la misma lista.

- Se itera $i$ desde $1$ hasta $n$
  - Se itera $j$ de $0$ hasta $i$
    - Si el i-ésimo elemento del arreglo es menor que el j-ésimo elemento del
    arreglo, intercambiamos su posición

