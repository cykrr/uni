# Cálculo II 

## Calculo I
Se define $f'(a) = \lim_{h \to 0} \cfrac {f(a + h) - f(a)} h$

## Derivadas parciales $\R^n$

Consideremos $f$ una función tal que $f: \R^3 \to \R$.
definimos sus derivadas parciales en un punto 
$(a,b,c)$ como: 

**(Derivada en términos de $x$)**
$$
\frac {df} {dx} = \lim_{(h\to0)} 
{\cfrac {f(a+h, b, c) - f(a,b,c)} {h}} 
$$


**(Derivada en términos de $y$)**
$$
\frac {df} {dy} = \lim_{(h\to0)} 
{\cfrac {f(a, b+h, c) - f(a,b,c)} {h}} 
$$


**(Derivada en términos de $z$)**
$$
\frac {df} {dz} = \lim_{(h\to0)} 
{\cfrac {f(a, b, c+h) - f(a,b,c)} {h}} 
$$

### Observación:
**Estas definiciones se utilizan en problemas del tipo** 

$$f(x,y,z) = \left \{ \begin{array} {ccc} 
    f(x,y,z) & (x,y,z) \neq  (a,b,c) \\
    N & (x,y,z) = (a,b,c)
\end{array} \right.$$

### Notación

1. $\cfrac {df}{dx} = f_x \to$  La derivada de f con respecto a $x$.

2. $\cfrac {df}{dy} = f_y \to$  La derivada de f con respecto a $y$.

3. $\cfrac {df}{dz} = f_z \to$  La derivada de f con respecto a $z$.

4. $(...)$

5. $\cfrac {d^2 f} {dx ^2} = f_{xx} \to$ La segunda derivada de f con respecto a $x$.

6. $\cfrac {d^2 f} {dy ^2} = f_{yy} \to$ La segunda derivada de f con respecto a $y$.

7. $\cfrac {d^2 f} {dz ^2} = f_{zz} \to$ La segunda derivada de f con respecto a $z$.

8. $(...)$

### Derivadas mixtas

9.  $\cfrac  {d^2 f} {dx dy} = f_{yx}$ Derivar f con respecto a $y$ y luego con respecto a $x$.

    * $dxdy$ = $\leftarrow$ derecha a izquierda
    * $f_{yx}$ = $\rightarrow$   de izquierda a derecha

#### Generalización:
$$
\cfrac {d^m f}  {dx^p_i dy_j ^q}
$$

Con $p+q = m$ 

$x_i$, $x_j$ son variables

1. Dada la función $f: \R^3 \to \R$ definifa como: 
$$
f(x,y,z) = x^3 + y^3 + z^3 - 3xyz -4
$$

Determine:

$a)$ Las derivadas parciales 
$\cfrac {df} {dx}$, 
$\cfrac {df} {dy}$, 
$\cfrac {df} {dz}$ evaluadas en el punto $(1, -1, 2)$.

$b)$ Las derivadas de orden superior 
$\cfrac {d^2 f} {dxdy}$,
$\cfrac {d^2 f} {dydx}$,
$\cfrac {d^2 f} {dzdy}$,

$c)$ Si se llegara a cumplir que $\cfrac {d^2 f} {dxdy} = \cfrac {d^2 f} {dydx}$

<br>
<br>
<br>

$a1)$ $f_x = 3x^2 - 3yz$ 

$f_x(1,-1,2) = 3 \cdot 1^2 - 3 \cdot (-1) \cdot 2 = 9$   

$a2)$ $f_y = 3y^2 - 3xz$  

<br>
<br>

$b2)$ $f_{yx} = \cfrac {df} {dy} f_x$

$f_x = 3x^2 - 3yz$

$f_{yx} = - 3z$



