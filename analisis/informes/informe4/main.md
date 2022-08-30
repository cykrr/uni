# HeapSort

## Descripción del problema de ordenamiento

Dada una secuencia de $n$ elementos $A[A_0, ...,  A_n]$, buscamos una
permutación de la entrada, llámese $B[B_0, ..., B_n]$ de manera que se cumpla que

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
# @param arr Arreglo
# @param i Posición del elemento a reubicar
def reubicar(arr, i, Verbose = False):

  mayor = i # Guarda el mayor elemento encontrado

  n = len(arr) 
  l = 2*i + 1 # Hijo izq
  r = 2*i + 2 # Hijo der

  # El mayor es el hijo izquierdo
  if arr[l] > arr[i]:
    if Verbose: print("El mayor es el hijo izquierdo")
    mayor = l;

  # El mayor es el hijo derecho
  elif arr[r] > arr[i]: 
    if Verbose: print("El mayor es el hijo derecho")
    mayor = r

  # Si el mayor no es la raiz, la reubicamos y reposicionamos la nueva raiz

  if mayor != i:
    arr[mayor], arr[i] = arr[i], arr[mayor]
    reubicar(arr, mayor)

end = '\033[0m'
bold = '\033[1;4m'

arr = [2,8,5,3,9,1]
reubicar(arr, 0)
print(arr)
```

*Results:*
```
Traceback (most recent call last):
  File "/tmp/mdeval//mainmd_23_56.py", line 31, in <module>
    reubicar(arr, 0)
  File "/tmp/mdeval//mainmd_23_56.py", line 25, in reubicar
    reubicar(arr, mayor)
  File "/tmp/mdeval//mainmd_23_56.py", line 25, in reubicar
    reubicar(arr, mayor)
  File "/tmp/mdeval//mainmd_23_56.py", line 12, in reubicar
    if arr[l] > arr[i]:
IndexError: list index out of range
```
