# Uso de arreglos con tipos primitivos

Los arreglos son colecciones ordenadas de datos del mismo tipo.

## Identificación y tamaño de un arreglo

Cada arreglo se conoce por un **identificador** y cada dato
se almacena en una posición **indexada**.

Un arreglo de **largo N** tiene posiciones indexadas mediante
**enteros** desde $0$ hasta $n-1$.

## Pasos para crear un arreglo en Java

1. **Definir** una variable que identifique el arreglo, indicando
la naturaleza de los tipos de datos que se almacenarán:
`tipo[] variable` o de otra forma `tipo variable[]`

2. **Instanciar** el arreglo indicando el largo que tendrá, y
**asignarlo** a la variable
`variable = new tipo[entero]`

## Creación de un arreglo

```java
int[] edades; /* Define que la variable edades
* referenciará un arreglo de enteros */

edades =  /* Asigna el arreglo instanciado */
    new int[8]; /* Instancia un arreglo de enteros */
```

## Recorrer un arreglo

Se puede utilizar la propiedad **length** del arreglo para controlar
procesos iterativos sobre el mismo:

```java
...
int i;
long[] numeros;
numeros = new long[20]
...
i = 0;
while (i < numeros.length)
{
    System.out.println(numeros[i]);
    ++i;
}
...
```

## Error típico al manejar arreglos

Tratar de accesar una posición inexistente del arreglo, por ejemplo
la posición 10 de un arrelgo de largo 10.

Cuando lo anterior ocurre, se genera en tiempo de ejecución una excepción
denominada `ArrayIndexOutOfBoundsException`

## Consideraciones respecto al largo de un arreglo

Una vez instanciado un arreglo no puede modificarse su largo

**length** es una propiedad o atributo del atributo
