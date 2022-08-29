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
