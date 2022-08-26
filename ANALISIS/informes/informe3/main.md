# MaxSubArray

El algoritmo `maxSubArray` consiste en, dado un aeglo $A$, encontrar un subarreglo
que posea la mayor cantidad de elementos de forma que su suma es máxima. Nótese que
podemos poseer tanto números positivos como negativos.

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
$O(n^2)$

Tenemos que calcular cada subarray partiendo de cada posición del arreglo? 
Quizás no. Podemos partir recorriendo el arreglo. Además podemos descartar todos
los valores negativos Antes de cada valor positivo. Entonces podemos movernos
hasta el primer valor positivo sin complicaciones.


## Ejemplo

Definimos $A = [-3,4,5,-4,2,3]$

```python
import math
def maxCenter(a, c):
    ls = -math.inf
    rs = -math.inf
    s = 0 
    ll = c-1
    lr = c
    rl = c 
    rr = len(a)
    for i in range (c-1, -1, -1):
        #print("Pasando por" ,a[i], end = " ")
        s += a[i]
        if ls < s:
            #print("Incluyo")
            ls = s;
            ll = i
        #else: print("no incluyo")
    s = 0;
    for i in range (c, len(a)):
        #print("Pasando por" ,a[i], end = " ")
        s += a[i]
        if rs < s:
            #print("Incluyo")
            rs = s
            rr = i+1
        #else: 
            #print("no incluyo")

    return ls + rs, ll, rr;

    
        
        
def maxSubArray(a):
    print(a)
    if (len(a) == 1): return a[0], 0, len(a)

    c = len(a) // 2

    ls, ll, lr = maxSubArray(a[c:]);
    print ("ls", ls, a[c:])
    rs, rl, rr = maxSubArray(a[:c]);
    print ("rs", rs, a[:c])
    cs, cl, cr = maxCenter(a, c)
    print ("cs", cs)
    m = max (cs, ls, rs)
    if m == cs:
        return cs, cl, cr;
    elif m == ls:
        return ls, ll, lr;
    elif m == rs:
        return rs, rl, rr;

a = [1, 2, 3, -8, 2, 3, -4, 2, 3, -5, 8, 1, -3, 1, 5, -8, -9, 10, 1, -1, -4, 7]
s, b, c = maxSubArray(a)
print(s,a[b:c])
```
