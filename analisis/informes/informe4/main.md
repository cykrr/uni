# HeapSort

## Índice
<!--toc:start-->
- [Descripción del problema de ordenamiento](#descripción-del-problema-de-ordenamiento)
- [Descripción del algoritmo](#descripción-del-algoritmo)
- [Implementación del algoritmo HeapSort](#implementación-del-algoritmo-heapsort)
<!--toc:end-->

## Descripción del problema de ordenamiento

Dada una secuencia de $n$ elementos $A[A_0, ...,  A_n]$, buscamos una
permutación de la entrada, llámese $B[B_0, ..., B_n]$ de manera que se
cumpla que:

$$
B_0 \leq B_1 \leq ... \leq B_n
$$

Donde a cada elemento $A_n$ tiene una correspondencia a un único elemento $B_n$.

## Descripción del algoritmo

El algoritmo **HeapSort**, como bien dice el nombre soluciona el problema de
ordenamiento reposicionando los elementos del arreglo con la estructura de un
montículo binario. Donde cada nodo padre $p$ tiene sus hijos en las posiciones
$L: 2p + 1$ y $R: 2p + 2$. Siendo $L$ el hijo izquierda y $R$ el hijo derecha.

## Implementación del algoritmo HeapSort

```python
def max_heap(
        arr: list[int],
        ):
    """
    Permuta arr de forma que la permutación de
    elementos formen un montículo de máximos.

    Parameters:
    ---
    arr: Arreglo a permutar
    """

    # Desde el ultimo elemento padre hacia atrás
    # Reubicamos para formar el maxHeap

    for i in range(len(arr) // 2  - 1, -1, -1):
        reubicar(arr, i)

def reubicar(
        arr: list[int],
        i: int,
        longitud: int = -1,
        verbose: bool = False,
        level: int = 0
        ):
    """
    Reubica un elemento "i" en el montículo
    ubicado en el subarreglo "arr" de longitud
    "n".

    Parameters:
    ---
    arr: Arreglo
    i: Posición del elemento a reubicar
    n: longitud del subarreglo
    verbose: switch de print detallado

    level: (interno) Nivel de recursión

    """

    # Si recibimos la opción predeterminada es
    # porque queremos todo el arreglo
    if longitud == -1:
        longitud = len(arr)

    mayor = i # Iteramos desde la raíz

    left = 2*i + 1 # Hijo izq
    right = 2*i + 2 # Hijo der

    # Si alguno de los hijos sobrepasa el límite
    # del subarreglo entonces los desactivamos
    # para no guardarlos

    if left >= longitud:
        left = -1
    if right >= longitud:
        right = -1

    # El mayor es el hijo izquierdo?
    if left != -1 and arr[left] > arr[mayor]:
        mayor = left

    # El mayor es el hijo derecho?
    if right != -1 and arr[right] > arr[mayor]:
        mayor = right

    # Si el mayor no es la raiz, la reubicamos y
    # reposicionamos la nueva raiz
    if mayor != i:
        arr[mayor], arr[i] = arr[i], arr[mayor]
        reubicar(arr, mayor, longitud,
            verbose, level = level+1)

def heap_sort(arr, verbose = False):
    """
    Ordena un arreglo arr por medio del algoritmo
    heap sort.
    """
    longitud = len(arr)
    max_heap(arr)
    ## Contador de elementos ordenados
    sorted_count = 0

    while sorted_count < longitud:
        # swap del ultimo elemento con el primero
        arr[0] , arr[-sorted_count] = \
                arr[-sorted_count], arr[0]
        # Reubicar nueva raiz en el subarreglo
        reubicar(arr, 0, longitud - sorted_count - 1,
                verbose)
        sorted_count +=1
    return arr
```
