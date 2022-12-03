# Problema: Búsqueda lineal

**Entrada:** Una lista L de n números y un valor a buscar v

**Salida:** Un índice i, tal que el i-ésimo elemento de la lista corresponda al valor buscado v.

Escriba un algoritmo que busque secuencialmente dentro de la lista.

```python
def search(l, n):
    for i in range len(l):
        if l[i] == n:
            return True
    return False
```

b. Pruebe que el algoritmo es correcto usando una **propiedad invariante de bucle y** asegúrese que cumpla con las dos condiciones.

En cualquier posición del arreglo podemos afirmar que todo elemento a la izquierda de la posición actual tendrá un valor distinto al buscado.

c. La cantidad de elementos a ser revisados es $n$ ya que el valor buscado puede estar en cualquier posición del arreglo.

$$
\cfrac{\sum_{i=1}^n i}{n} 
$$

d. En el peor caso tendríamos que recorrer la totalidad del arreglo para encontrar el valor dado 


e. El peor caso $O(n)$ y el caso promedio es $O(\frac n 2)$

2. $O(n^3)$

3. 

```python
def low(l):
    for i in range len(l):

def insSort(l):
    
```
