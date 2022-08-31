"""
HeapSort

"""


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
        level = 0):
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

def print_heap(arr, head = 0, level = 0):
    """
        Imprime un arreglo en su forma
        de árbol binario.

        Parameters:
        ---
        arr: Arreglo a mostrar

        head: Elemento inicial del arreglo
        a mostrar (utilizado internamente)

        level: Nivel de recursión (utilizado
        internamente)
    """

    print (" " * level * 4,
            f"{arr[head]}",
            end = " ")

    left = 2*head +1
    right = 2*head +2

    if (left < len(arr) or right < len(arr)):
        print ("{")
    else:
        print()


    if left < len(arr):
        print_heap(arr, head = left, level = level +1)
    if right < len(arr):
        print_heap(arr, head = right, level = level + 1)

    if (left < len(arr) or right < len(arr)):
        print (" " * level * 4, "}")
    if not level:
        print ("---")

#a = [2,8,5,3,9,1]
#print("in:\t", a)
#print("out:\t", heap_sort(a))
