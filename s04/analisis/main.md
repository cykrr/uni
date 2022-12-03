# Introducción

## Temas 

* Problema computacional
    * Problema del ordenamiento
* Algoritmo InsertionSort
* Propiedades del algoritmo
* Actividad

### Qué es un algoritmo?

Instrucciones para el computador con el objetivo de resolver problemas.
Reciben una entrada y entregan una salida.

### Problema computacional

Puede ser resuelto con algoritmos.

Por ejemplo: Dado un entero positivo $n$, encuentre un factor primo de $n$.

Al igual que un algoritmo, se define por una entrada o un **conjunto de
instancias** y una salida.

### Clasificación de problemas

_(Según el tipo de solución)_

* Problemas de decisión
    * problema de si y no
* Problemas de búsqueda
    * Busqueda de una solución del sudoku
* Problema de optimización
    * Encontrar el camino más corto

### Tipos de problema

_(Según dificultad)_

#### Problemas P

Problemas fáciles de resolver.

P: Se puede resolver en un tiempo polinomial

Casi todos los algoritmos vistos hasta ahora son en tiempo polinomial

#### Problemas NP Hard

Requiere tiempos exponenciales de resolución

Ejemplo: Turing halting problem

### Problema NP

Problemas **verificables** en tiempo polinomial. Si tengo una solución puedo 
verificarla en un tiempo polinomial.

### Problemas NP Complete

Problemas más dificiles del conjunto NP

## Problema de ordenamiento

### InsertionSort

### Correctitud

Teorema 1: El algoritmo InsertionSort genera un arreglo:
$[a_1', a_2', ..., a_n']$, con los mismos elementos del arreglo de entrada
ordenados de menor a mayor, es decir $a_1' \geq  a_2', \geq ..., a_n'$

Propiedad que distingue a un algoritmo de un procedimiento efectivo.

Un algoritmo es correcto si:

1. Resuelve el problema para el cual fue diseñado.
2. Para cada entrada, produce la salida deseade.
3. Termina en un tiempo de ejecución finito

#### Propiedad del bucle invariante

Propiedad lógica que permite estudiar un programa
o un algoritmo.

las invariantes de los bucles son predicados logicos, que sirven para probar los
algoritmos que los utilizan, en particular en la correción de estos algoritmos.


### Tiempo de ejecución InsertionSort

En el peor caso $O(n^2)$. Se analiza el código,
se ve cuantas instrucciones realiza en el peor caso, el cual se da cuando el
arreglo está ordenado de mayor a menor.

