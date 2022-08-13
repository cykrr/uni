# Informe 1

[Guía para trabajar en informe 1](https://github.com/rilianx/ADA/blob/main/Guías%20para%20Informes/CriteriosEvaluacion.md

## Problema de ordenamiento

**Entrada**: Secuencia de n números $[a_1, a_2, ..., a_n]$

**Salida**: Permutación ordenada de la secuencia de entrada: $[a_1', a_2', ..., a_n']$

con $a_1' \leq a_2' \leq ... \leq a_n'$

El problema de ordenamiento es uno de los problemas más estudiados en el campo
de las ciencias de la computación. Este es resuelto por medio de distintos
algoritmos, los cuales se comportan de mejor o peor manera dependiendo de la
cantidad de elementos. En el presente informe se analizará el comportamiento del
algoritmo **Insertion Sort**

## Insertion Sort

```python
def sort(a: list, verbose: bool = False):
    aux = 0
    n = len(a)
    if verbose: print("Arreglo", a, ":")
    for i in range(1, n):
        if verbose: print(a)
        for j in range(0, i):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                aux+=1

                if verbose:
                    print(a)
                    print (f"Intercambiamos: ({a[i]},{a[j]}")
    return a
```

## Descripción del algoritmo

El Insertion Sort consiste en recorrer el arreglo de izquierda a derecha. Cada
elemento será comparado con los elementos a su izquierda y reubicado hasta que su
posición sea la correcta.

Se recibe una lista $a$ con una serie de $n$ elementos a ser ordenados. Estos son
ordenados dentro de la misma lista.

- Se itera $i$ desde $1$ hasta $n$
  - Se itera $j$ de $0$ hasta $i$
    - Si el i-ésimo elemento del arreglo es menor que el j-ésimo elemento del
    arreglo, intercambiamos su posición

## Análisis del algoritmo

Añadiremos una variable auxiliar para obtener la
cantidad de veces que el agoritmo debe retroceder
al realizar el ordenamiento. A mayor el valor de
esta variable auxiliar, peor será el caso
correspondiente.

## Ejemplo

Sea $a = [\color{blue}{8}\color{reset}, 3, 7, 5, 9]$

Partimos de izquierda a derecha. Podemos decir que el
primer elemento esta ordenado ya que no tiene ningún
elemento menor a su izquierda, así que la primera
iteración parte del segundo valor.

$a = [\color {blue} 3, \color {red} 8 \color {reset}, 7, 5, 9]$

El $3$ si es menor que el $8$. Para llevarlo a su
posición correspondiente lo desplazamos una casilla
hacia la derecha. 

$a = [\color {blue} 3, 8 \color {reset}, \color {red}
7 \color {reset}, 5, 9]$

El $7$ necesita ser reubicado, al igual que el $8$ lo
desplazamos una posición a la izquierda

$a = [\color {blue} 3, 7, 8 \color {reset},
\color {red} 5 \color {reset}, 9]$

El cinco necesita desplazarse dos posiciones para
llegar a su posición ideal

$a = [\color {blue} 3, 7, \color {red}5 \color {reset}, 8, 9]$

$a = [\color {blue} 3, \color {red}5 \color {blue} , 7, 8, 9]$

$a = [\color {blue} 3, 5 , 7, 8,\color {red} 9\color {reset}]$

Ya en la última posición el arreglo se encuentra completamente ordenado
## Correctitud

### Propiedad invariante del bucle
