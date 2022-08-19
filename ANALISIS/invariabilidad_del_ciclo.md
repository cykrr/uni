# Invariabilidad del ciclo y correctitud del algoritmo

```python
def insertionSort(A):
    for j in range (1, len(A)):
        key = A[j]
        # Insertamos A[j] en la secuencia ordenada A[1 .. j-1]
        i = j - 1
        while i > 0 and a[i] > key:
            A[i+1] = A[i]
            i -= 1
        a[i+1] = key
```

La figura muestra como este algoritmo funciona para A = {5, 2, 4, 6, 1, 3}. El
índice $j$ indica la "carta actual" que está siendo insertada en la mano. Al
principio de cada iteración del ciclo **for**, que es indexado por $j$. el
subarreglo está formado por elementos $A[1..j-1]$ corresponde a la pila de
cartas ordenadas, y el subarreglo $A[j+1..n]$ corresponde a la pila de cartas
todavía en la mesa. De hecho, los elementos $A[1..j-1]$ son los elementos
originalmente en posiciones desde $1$ a $j-1$, pero ahora ordenados. Definimos
estas propiedades de $A[1..j-1]$ formalmente como una **invariante de ciclo**

Al inicio de cada iteracion del ciclo **for**, el subarreglo $A[1..j-1]$ consiste
de los elementos originalmente en $A[1..j-1]$ ahora ordenados.

Usamos invariables de ciclo para ayudarnos a entender por que un algoritmo es
correcto. Debemos mostrar tres cosas de una invariante de ciclo.

**Inicialización**: Es verdadera antes de iniciar la primera iteración del
ciclo

**Mantenimiento**: Es verdadera antes de una iteración del ciclo. Permanece
verdadera antes de la siguiente iteración.

**Terminación**: Muestra cuando termina el ciclo, la invariante de ciclo nos
da una propiedad útil que nos ayuda a demostrar que el algoritmo es correcto.

Cuando las dos primeras propiedades se cumplen, la invariante de ciclo es
cierta antes de cada iteración del ciclo. (por supuesto, somos libres de usar
otros hechos establecidos aparte de la invariante de ciclo para probar que esta
misma se mantiene antes de cada iteración.) Note la similaridad a la
inducción matemática, donde para probar que una propiedad se mantiene, debes
probar un caso base y un paso inductivo. Aquí, mostrando que la invariante
se mantiene antes de la primera iteración corresponde al caso base, y mostrando
que la invariante se mantiene entre iteración e iteración corresponde al paso
inductivo.

La tercera propiedad es quizás la más importante, ya que usamos la invariante
de ciclo para probar correctitud. Típicamente, usamos la invariante de ciclo
junto con la condición que causó que el ciclo se terminara. La propiedad de
terminación difiere de como usualmente usamos la inducción matemática, en la
cual aplicamos el paso inductivo infinitamente; aqí paramos la "inducción" cuando
el ciclo termina. Veamos como estas propiedades se mantienen en el InsertionSort

