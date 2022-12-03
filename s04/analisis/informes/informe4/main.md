# HeapSort

## Índice

- [Descripción del problema de ordenamiento](#descripción-del-problema-de-ordenamiento)
- [Descripción del algoritmo](#descripción-del-algoritmo)
- [Implementación del algoritmo HeapSort](#implementación-del-algoritmo-heapsort)

## Descripción del problema de ordenamiento

Dada como entrada una secuencia de $n$ elementos $A[A_0, ...,  A_n]$, buscamos
como salida una permutación de la entrada, llámese $B[B_0, ..., B_n]$ de manera
que se cumpla que:

$$
B_0 \leq B_1 \leq ... \leq B_n
$$

Donde cada elemento $A_n$ tiene una correspondencia a un único elemento $B_n$.

## Descripción del algoritmo

El algoritmo **HeapSort**, como bien podría uno intuir con su nombre, soluciona
el problema de ordenamiento reposicionando los elementos del arreglo con la
estructura de un montículo binario (Heap). Donde cada nodo padre en la posición
$p$ tiene sus hijos en las posiciones $L: 2p + 1$ y $R: 2p + 2$. Siendo $L$ el
hijo izquierda y $R$ el hijo derecha.

### Sub-rutina reposicionar

La sub-rutina reposicionar es clave ya que se utiliza para la creación y
posterior mantenimiento del montículo de máximos. Su funcionamiento consiste en
reubicar un elemento en el montículo a su posición correspondiente en el
montículo de máximos

#### Ejemplo reposicionar

Dado un arreglo $K: [1,3,2,4,5]$ el reposicionamiento del primer elemento
consiste en:

Intercambiar posición con el hijo mayor. En este caso $3$. Lo cual da lugar al
arreglo $K[3,1,2,4,5]$.

Sin embargo el elemento $1$ todavía no está en su posición correspondiente. Pues
todavía tiene un hijo mayor que él ($5$). Así que volvemos a realizar el proceso
correspondiente, intercambiando el $5$ con el $1$. Dando como resultado el
arreglo $K'[3,5,2,4,1]$.

### Creación del montículo de máximos

El primer paso del algoritmo consiste en crear un montículo de máximos dentro
del arreglo $A$.

Para lograr esto el algoritmo se posiciona en el último nodo padre. Esta
posición es elegida estratégicamente para reducir el tiempo de ejecución del
algoritmo. Esto es debido a que el reposicionamiento del padre implica que los
hijos también serán reposicionados en casos de ser mayores que su padre,
ahorrándonos un par de iteraciones.

La posición de este elemento es fácilmente calculable por medio de la ecuación

$$
\textit{LastParent} = round(n/2) - 1
$$

Una vez calculado este valor recorremos el arreglo desde la posición
$LastParent$ hasta $0$ y reposicionamos el elemento correspondiente.

#### Ejemplo maxHeap

Dado un arreglo $K[3,1,2,4,5]$ aplicamos el algoritmo señalado.

1. Calculamos el valor de $LastParent$.

   Sabiendo que el largo del arreglo es $n = 5$. Podemos deducir que la posición
   del último padre $n//2 -1 = 1$.

2. Reubicación de los elementos

   Reubicamos el elemento $K_\text{LastParent} = 1$. (No se describirá el
   proceso nuevamente. Ante cualquier duda refiérase a la sección
   [Ejemplo de la sub-rutina reposicionar](#ejemplo-reposicionar)). Lo que
   genera el arreglo $K[3,5,2,4,1]$

   Repetimos el proceso para el elemento $LastParent -1 = 0$. Pasando por los
   arreglos $K[5,3,2,4,1]$ y finalmente $K'[5,4,2,3,1]$. Siendo $K'$ el
   montículo máximo resultante.

### Mantenimiento del montículo

Una vez generado el montículo de máximos es revelado el último elemento del
arreglo de salida $B_{n-1}$. El cual se encuentra en la posicióń $A_0$.

## Implementación del algoritmo HeapSort

```python
def max_heap(
        arr: list[int],
        ):
    """
    Reposiciona los elementos de  arr de forma
    que la permutación de elementos formen un
    montículo de máximos.

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

## Tiempo de ejecución del algoritmo

### Tiempo de ejecución maxHeap

### Tiempo de ejecución reubicar

### Tiempo de ejecución HeapSort

## Correctitud del algoritmo

### Correctitud reubicar

### Correctitud maxHeap

### Correctitud HeapSort

## Experimentos

### Comparación con MergeSort

### Comparación con QuickSort

## Conclusiones
