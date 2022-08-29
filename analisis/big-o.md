# Complejidad computacional

Si los computadores fueran infinitamente rápidos, necesitariamos
analizar nuestros algoritmos? La respuesta es sí. De igual manera
debemos demostrar que nuestros algoritmos terminan y que entregan una
respuesta correcta.

Si los computadores fueran infinitamente rápidos, cualquier método
para resolver un problema bastaría. Probablemente querrás que tu
implementación esté bien diseñada y documentada, pero la mayoría de
las veces usarías el método que sea el más fácil de implementar.

## Problemas difíciles

Si bien buscamos algoritmos eficientes y rápidos, hay algunos 
problemas para los cuales no conocemos una solución eficiente. Estos
problemas son conocidos como **NP-Complete**

Por qué son interesantes los problemas NP Completos? Primero, no se
ha encontrado **ningún** algoritmo eficiente para un problema NPC.
Sin embargo, nadie ha probado que un algoritmo eficiente no existe.
En otras palabras, nadie sabe si existen algoritmos eficientes para
los problemas NPC.
Segundo, el conjunto de problemas NPC tiene la destacable propiedad
de que si se encuentra una solución eficiente, entonces todos los
problemas NPC tienen una solución eficiente.

Es prudente estudiar los problemas NPC ya que algunos de estos
aparecen en aplicaciones reales. Si se te pide crear un algoritmo
eficiente para un problema NPC, es probable que gastes una gran
cantidad de tiempo en una búsqueda que no dará frutos. Si puedes
demostrar que el problema es NPC, puedes gastar tu tiempo 
desarrollando un algoritmo que da una buena, pero no la mejor 
solución.

## Eficiencia

El tiempo y el uso de recursos difiere dramáticamente entre algoritmos. Estas diferencias pueden ser más significativas que diferencias de hardware y software.

Por ejemplo, el **InsertionSort** toma un tiempo de $c_1n^2$ para
ordenar $n$ elementos. donde $c_1$ es una constante que no depende de $n$. Esto quiere decir que el tiempo que toma es proporcional a
$n^2$. El segundo, **MergeSort** toma apenas $c_2\cdot \log_2(n)$ y
$c_2$ es otra constante que no depende de $n$.

El factor constante de InsertionSort es típicamente menor al del MergeSort. Así $c_1 < c_2$.

Veremos que estas constantes tienen un impacto muy reducido comparado a la dependencia de el tamaño de la entrada $n$.

Si bien el InsertionSort funciona usualmente más rápido para arreglos
pequeños, cuando la entrada se vuelve lo suficientemente grande, la ventaja del MergeSort de $\log_2 n \space \text vs. \space n$ 
compensará la diferencia de las constantes.
