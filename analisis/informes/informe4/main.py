def maxHeap(
        arr:list[int],
        Verbose: bool = False):

    """
    Permuta arr de forma que la permutación de
    elementos formen un montículo de máximos.

    Parameters:
    ---
    arr: Arreglo a permutar
    Verbose: switch para print detallado
    """

    # Desde el ultimo elemento padre hacia atrás
    # Reubicamos para formar el maxHeap

    for i in range(len(arr) // 2  - 1, -1, -1):
        reubicar(arr, i);

        

def reubicar(
        arr: list[int], 
        i: int,
        n: int = -1,
        Verbose: bool = False,
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
  Verbose: switch de print detallado

  level: (interno) Nivel de recursión

  """

  # Si recibimos la opción predeterminada es 
  # porque queremos todo el arreglo
  if n == -1:  n = len(arr) 

  mayor = i # Iteramos desde la raíz

  l = 2*i + 1 # Hijo izq
  r = 2*i + 2 # Hijo der

  # Si alguno de los hijos sobrepasa el límite
  # del subarreglo entonces los desactivamos 
  # para no guardarlos

  if l >= n: l = -1
  if r >= n: r = -1

  # El mayor es el hijo izquierdo?
  if l != -1 and arr[l] > arr[mayor]:
    mayor = l;

  # El mayor es el hijo derecho?
  if r != -1 and arr[r] > arr[mayor]: 
    mayor = r

  # Si el mayor no es la raiz, la reubicamos y
  # reposicionamos la nueva raiz
  if mayor != i:
    arr[mayor], arr[i] = arr[i], arr[mayor]
    reubicar(arr, mayor, n,
            Verbose, level = level+1)


def heapSort(arr, Verbose = False):
    n = len(arr)
    maxHeap(arr);
    ## Contador de elementos ordenados
    sortedCount = 0 

    while (sortedCount < n):
        # swap del ultimo elemento con el primero
        arr[0] , arr[-sortedCount] = \
                arr[-sortedCount], arr[0]
        # Reubicar nueva raiz en el subarreglo
        reubicar(arr, 0, n - sortedCount - 1,
                Verbose)
        sortedCount +=1
    return arr;

def printHeap(arr, head = 0, level = 0):
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

    l = 2*head +1
    r = 2*head +2

    if (l < len(arr) or r < len(arr)):
        print ("{")
    else: print()


    if l < len(arr):
        printHeap(arr, head = l, level = level +1)
    if r < len(arr):
        printHeap(arr, head = r, level = level + 1);
    if (l < len(arr) or r < len(arr)):
        print (" " * level * 4, "}")
    if not level: print ("---")

arr = [2,8,5,3,9,1]
print("in:\t", arr)
print("out:\t", heapSort(arr))
