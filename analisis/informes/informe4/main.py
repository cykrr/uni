import pandas
def maxHeap(arr, Verbose = False):
    # Desde el ultimo elemento padre hacia atrás
    # Reubicamos para formar el maxHeap

    for i in range(len(arr) // 2  - 1, -1, -1):
        reubicar(arr, i);

        

def reubicar(arr, i, n = -1, Verbose = False, level = 0):
  """
  asd

  Parameters:
  ---
  arr: Arreglo
  i: Posición del elemento a reubicar
  n: longitud del subarreglo
  Verbose: switch de print detallado
  level: Nivel de recursión
  """

  # Si recibimos la opción predeterminada es 
  # porque queremos todo el arreglo
  if n == -1:  n = len(arr) 

  mayor = i # Iteramos desde la raíz

  l = 2*i + 1 # Hijo izq
  r = 2*i + 2 # Hijo der

  # Si alguno de los hijos sobrepasa el límite del
  # Subarreglo entonces los desactivamos para
  # no guardarlos
  if l >= n: l = -1
  if r >= n: r = -1

  # El mayor es el hijo izquierdo?
  if l != -1 and arr[l] > arr[mayor]:
    mayor = l;

  # El mayor es el hijo derecho?
  if r != -1 and arr[r] > arr[mayor]: 
    mayor = r

  # Si el mayor no es la raiz, la reubicamos y reposicionamos la nueva raiz

  if mayor != i:
    arr[mayor], arr[i] = arr[i], arr[mayor]
    reubicar(arr, mayor, n, Verbose, level = level+1)


def heapSort(arr, Verbose = False):
    n = len(arr)
    maxHeap(arr);
    ## Contador de elementos ordenados
    sortedCount = 0 

    while (sortedCount < n):
        # swap del ultimo elemento con el primero
        arr[0] , arr[-sortedCount] = \
                arr[-sortedCount], arr[0]
        # Reubicar nueva raiz
        reubicar(arr, 0, n - sortedCount - 1, Verbose)
        sortedCount +=1

def printHeap(arr, head = 0, level = 0):
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
heapSort(arr)
print ("out: ")
print(arr)
