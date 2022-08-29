# Sobrecarga y colecciones

## Sobrecargas

### Sobrecargas de métodos

Una clase puede tener más de un método con el mismo nombre.
Los métodos se diferencian por **cantidad, tipo y orden de parámetros**.
Todo esto constituye la firma del método _(Method signature)_.

```java
public setColor(String color){}
public setColor(Vec3 color){}
public 
```

### Sobrecarga de constructores

Una clase puede tener más de un constructor. Estos se diferencian
por **cantidad,  tipo y orden** de parámetros.

```java

public Observacion(){}
public Observacion(int a){}
public Observacion(int a, String b){}
```

Esto permite instanciar objetos considerando distintos tipos de datos
disponibles

## Arreglos de objetos

Se declaran e instancian como los arreglos de tipos primitivos

```java
// Clase [] variable = new Clase[entero];

CuentaAhorro[] ctas = new CuentaAhorro[20];
Tiempo reloj[] = new Tiempo[n];
```

Un arreglo de objetos puede almacenar en cada posición una referencia
a un objeto de la clase con la que fue definido, así como la dirección
null.

La instanciación de un arreglo no instancia los objetos que pued
referenciar. Los objetos a referenciar desde un arreglo deben
instanciarse individualmente,

Se debe instanciar cada objeto y luego asociarlo al arreglo.

## Colecciones

### Java Collection Framework

**Collection**: La raíz de la jerarquía de colecciones. Una colección
representa un grupo de objetos conocidos como sus elementos.

**Set**: Una colección que no puede contener elementos duplicados. Es la abstracción
matemática de un conjunto.

**Lista**: Una colección ordenada (a veces llamada secuencia). Las listas pueden
contener elementos duplicados. El usuario de una lista generalmente tiene un control
preciso sobre donde en la lista cada elemento se inserta y puede acceder a los
elementos por su índice (posición);

**Mapa**. Un objeto que mapea claves a valores. Un mapa no puede contener claves
duplicadas; a cada clave se le puede asignar a lo más un valor.

#### ArrayList

```java
public class ArrayList<T>
```

Es la implementación de una lista (permite elementos repetidos) mediante
arreglos. Tiene la particularidad de de ser des-sincronizado (los cambios
realizados por múltiples hilos no son reflejados)

#### Vector

Es sinctornizado (los cambios realizados por múltiples hilos son reflejados).
La única diferencia con el `ArrayList` es su sincronización. Por lo que es conveniente
utiliza `ArrayList` siempre que se trabaje en un sólo hilo.

#### Stack

Se extiende de la clase `Vector` agregando las funciones para ser operada como Stack.
Permite guardar objetos almacenándolos en forma de pila tipo **LIFO (Last in First
out);

#### HashSet

Implementa la interfaz Set mediante una has table (una instancia de hashmap)

Permite el elemento null

No entrega garantía en cuanto al orden de iteración al interior del set. Ni garantiza
que el orden permanecerá constante en el tiempo.

#### HashTable

Implementa una hash table, la cual almacena pares **clave-valor**. Cualquier objeto
no null puede ser utilizado como clave o valor

Los objetos utilizados como claves deben implementar el método `hashCode` y el método
`equals`.

Reemplaza a los diccionarios ya que cumplen la misma función y de manera más eficiente.

Las hashtable son comúnmente usadas para almacenar datos de usuarios y contraseńas
debido a su rápido acceso y codificación (hashcode);
