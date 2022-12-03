# Unidad 1: Introducción

## Orígenes

## Principios

## Lenguajes

### Java

Qué es java?

* Lenguaje de programación orientado a objetos
* Plataforma de ejecución para programas escritos en el
lenguaje Java

Este lenguaje fue desarrollado por un equipo de
investigadores de *SUN Microsystems*.

Java permite:

* Construir *aplicaciones*: Programas computacionales que
apoyan el trabajo o resuelven problemas específicos de
usuarios *(stand-alone)*
* Construir *applets*: Programas de menor envergadura que se
ejecutan al momento de cargar una págna web.

Java se compone de:

* Compilador (Java-compiler)
* Intérprete (Java)
* Biblioteca de clases (Java API)
* Utilitarios de desarrollo (para debug, docs, etc.)

* Lo anterior se encuentra en el SDK de SUN-Microsystems

## Hola mundo

```java
public class Hello 
{
    public static void main (String[] str)
    {
        System.out.println("Hello World");
    }
}
```

## Tipos de datos en Java

Los tipos de datos utilizados se clasifican en dos
categorías:

* **Primitivos**: Sirven para definir variables que guardan
valores numéricos, lógicos y caracteres unitarios,
* **Clases e interfaces**: Sirven para definir variables que
almacenan tipos de datos estructurados y las funciones
asociadas.

### Tipos de datos primitivos

Java soporta los siguientes tipos de datos primitivos:

* Entero
* Punto flotante
* Lógico
* Caracter

#### Familia de datos primitivos (contables)

##### Familia de datos enteros: `byte, short, int, long`

| Tipo  | Almacena        | Rango          |
| --    | --              | --             |
| `byte`| Entero de 8-bit | -128 hasta 127 |
| `short`| Entero de 16-bit | -32.768 hasta 32.767 |
| `int`| Entero de 32-bit | -2.147.483.648 hasta 2.147.483.647 |
| `long`| Entero de 64-bit | caleta |

##### Familia de datos punto flotante

| Tipo  | Almacena        | Rango          |
| --    | --              | --             |
| `float`| Entero de 16-bit | 7 dígitos significativos |
| `double`| entero de 32-bit | 15 dígitos significativos |

#### Tipo de dato String

El `String` es un tipo de dato que permite trabajar con
cadenas de caracteres, por ejemplo:

```java
"Hola mundo",
"Mario Mora",
"12/10/99",
"a",
""
```

String es **una clase, no un tipo primitivo**, sin embargo
se utiliza en forma muy similar a estos últimos.

#### Operadores básicos para tipos primitivos

* Operador de asignación:
  * `=`
* Operadores numéricos
  * Binarios:
    * `+` Suma
    * `-` Resta
    * `*` Multiplicación
    * `/` División
    * `%` Módulo / resto de la división entera
  * Unarios:
    * `++` Auto-incremento
    * `--` Auto-decremento
* Operadores relacionales:
  * `==` Igual a
  * `!=` Distinto de
  * `>` Mayor que
  * `<=` Menor o igual que
  * `>` Mayor que
  * `>=` Mayor o igual que
* Operadores lógicos:
  * `&&` (AND)
  * `||` (OR)
  * `!` (NOT)

### Estructuras de control

#### Decisión

Simple

```java
if (condicion) foo;

if (condicion)
    foo;

if (condicion)
    foo;
else
    bar;

```

Compleja

```java
if (condicion)
{
    foo;
    bar;
} else {
    bar;
    foo;
}
```

#### Iteración

```java
 // Hacer - repetir
while (condicion)
    foo;

 // Hacer - repetir
while (condicion)
{
    foo; bar;
    ...
}

 // Hacer - mientras
 do 
    foo;
while (condicion)

 // Hacer - mientras
 do 
 {
    foo;
    bar;
    ...
 } while (condicion)
```

### Comentarios y documentación

Se pueden incluir comentarios en el código usando los
siguientes marcadores:

```java
// Comentario de linea

/* Comentario de 
 * multiples lineas
 */

/* Es necesario que ponga
 * asteriscos en cada linea?
 * no.
 */

/* Puedes comentar
 así */

/* O asi, tu elige 
lo que más te guste. 
*/

```

#### Documentación

Similar a doxygen, podemos añadir docuentación dentro del
código, la cual será reconocida por el IDE a utilizar.

Es prudente documentar estructuras de datos, métodos y
funciones. De esta manera podemos saber de antemano:

* Qué parámetros utiliza una función
* Qué hace la función
* Cuál es la entrada/salida de la función

--

* Para qué es una clase
* Como usar una interfaz
* Que hace un constructor

```java
/** El método addCallback añade una función
  * estática al vector de callbacks que se
  * ejecutarán dado un evento, por ejemplo
  * una redimensión de ventana. 
  @author krr
  @exception system_error
  @see src/graphics/gl/glad.java

  @param c El callback
  @param e Tipo de evento

  @version 1
*/
public void Window::addCallback(EventEnum e, void *(c))
```

## Declaración de variables

Una variable se declara según el formato:

```java
tipo identificador [ = valor], identificador [ = valor];

int a = 0, b = 1, c = 2;

double foo = 7.05;

car bar = 'c';

byte edad = 20;

```

## Algunos métodos de utilidad

* Convertir de String a número:
  * `Byte.parseByte()`
  * `Short.parseShort()`
  * `Integer.parseInt()`
  * `Float.parseFloat()`
  * `Double.parseDouble()`

Por ejemplo:

```java
x = Integer.pareseInt("24242");
y = Integer.pareseFloat(payload) + 40;
```

## Estructura de una aplicación simple

```java
/** Ejemplo de una app */
public class IdentificadorClase 
{ 
    public static void main (String[] nombreVariable) {
        foo();
        bar();
    }
}

```

Muchas de estas palabras claves pueden no ser reconocidas
facilmente. Con el objetivo de aclararlo describiré
brevemente algunos conceptos

### Clases

Las clases son uno de los pilares fundamentales de la
orientación a objetos. Estas nos ayudan a abstraer
funcionalidades de una manera similar a las funciones.

Las clases están constituidas por un conjunto de
variables y métodos.

#### Qué es un método?

Un método es una función que forma parte de una clase.
La diferencia entre el método y la función es que el
método se encarga de manipular o utilizar la estructura
de la clase.

Por ejemplo, dígamos que queremos crear una clase
para una lista enlazada.

```java
public class LinkedList {
        // Estructura de la clase {

        private Node head;
        private Node current;

        public int longitud;

        // } Métodos de la clase { 

        public void pushBack(void *data);
        public void pushFront(void *data);

        public void next();
        public void prev();
        // }
}

```

Una clase LinkedList tendría métodos para trabajar con dicha lista,
como por ejemplo `next, prev` para moverse por la lista, 
`pushBack, pushFront` para añadir elementos. 

### Public y Private

`public` y `private` son dos palabras claves utilizadas para 
que solo lo justo y necesario sea accesible para poder
utilizar la clase. Por ejemplo queremos que el usuario de la
clase LinkedList pueda acceder a su longitud, pero no a los
punteros a los nodos head y current, porque queremos que 
que se utilicen los métodos para acceder a los datos. De
esta manera protegemos al usuario de la clase a causar
comportamiento indebido al intervenir con la parte interna
de la clase.

