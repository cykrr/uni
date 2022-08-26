# MaxSubArray

Buscamos el subarreglo contiguo conteniendo al menos un número que posea la mayor
suma entre sus elementos.

Poseemos tanto números positivos como negativos.

Nuestra primera solución sería calcular todos los subarreglos posibles y
repetir para los segundos números. Sin embargo esto no sería óptimo ya
que tendría complejidad $O(n^2)$.
```python
for i in range (n-1):
    for j in range(i, n-1):
        for k in range (i, j):
            ...
```

Podemos ahorrar tiempo calculando un sub-array

Podemos guardar la suma del subarreglo anterior y le sumamos el número extra.
Esto reduce la cantidad de cálculos.

```python
for i in range (n-1):
    for j in range(i, n-1):
        currentSum += num[j];
```
^ $O(n^2)$

Tenemos que calcular cada subarray partiendo de cada posición del arreglo?

Quizás no. 

Podemos partir recorriendo el arreglo.

Podemos descartar todos los valores negativos Antes de cada valor
positivo. Entonces podemos movernos hasta el primer valor positivo
sin complicaciones.


