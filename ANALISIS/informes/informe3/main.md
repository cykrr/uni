# MaxSubArray

El algoritmo `maxSubArray` consiste en, dado un arreglo $A$, encontrar un subarreglo
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
sum = 0
currentSum = 0
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
def maxCenter(a, c, l, r):
    print(a[l:r])
    ls = -math.inf
    rs = -math.inf
    s = 0 
    ll = c-1
    lr = c
    rl = c 
    rr = len(a)
    for i in range (c-1, l-1, -1):
        print("Pasando por" ,a[i], end = " ")
        s += a[i]
        if ls < s:
            print("Incluyo")
            ls = s;
            ll = i
        else: print("no incluyo")
    s = 0;
    for i in range (c, r):
        print("Pasando por" ,a[i], end = " ")
        s += a[i]
        if rs < s:
            print("Incluyo")
            rs = s
            rr = i+1
        else: 
            print("no incluyo")

    print("center sum: ", ls + rs)
    return ls + rs, ll, rr;

    
        
        
def maxSubArray(a, l = -1, r = -1):

    if ( r-l == 1):
      print("base", a[l:r])
      return a[r-1], l, r 

    if l == -1 and r == -1:
      l = 0;
      r = len(a);

    print("a:",a[l:r])
    print("L: ", l, "R: ", r)

    c = (l + r) // 2

    print("Recursión izq", end = " ")
    ls, ll, lr = maxSubArray(a, l, c);
    print ("ls", ls, a[ll:lr])
    print("Recursión derecha ", end = "")
    rs, rl, rr = maxSubArray(a, c , r);
    print ("rs", rs, a[rl:rr])
#    print ("rs", rs, rl, rr, a[c:], a[rl:rr])
    print("Recursión centro ", end = " ")
    cs, cl, cr = maxCenter(a, c, l, r)
#    print ("cs", cs)
    m = max (cs, ls, rs)
    if m == cs:
        return cs, cl, cr;
    elif m == ls:
        return ls, ll + l, lr 
    elif m == rs:
        return rs, rl + l, rr + r;

#a = [1, 2, 3, -8, 2, 3, -4, 2, 3, -5, 8, 1, -3, 1, 5, -8, -9, 10, 1, -1, -4, 7]
a = [1, 2, 3, 4]
s, b, c = maxSubArray(a)
print(s,a[b:c])
```

*Results:*
```
a: [1, 2, 3, 4]
L:  0 R:  4
Recursión izq a: [1, 2]
L:  0 R:  2
Recursión izq base [1]
ls 1 [1]
Recursión derecha base [2]
rs 2 [2]
Recursión centro  [1, 2]
Pasando por 1 Incluyo
center sum:  3
ls 3 [1, 2]
Recursión derecha a: [3, 4]
L:  2 R:  4
Recursión izq base [3]
ls 3 [3]
Recursión derecha base [4]
rs 4 [4]
Recursión centro  [3, 4]
Pasando por 3 Incluyo
center sum:  7
rs 7 [3, 4]
Recursión centro  [1, 2, 3, 4]
Pasando por 2 Incluyo
Pasando por 1 Incluyo
center sum:  10
10 [1, 2, 3, 4]
```
