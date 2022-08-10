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

```
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
    *   `=`
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
