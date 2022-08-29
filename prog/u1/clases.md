# Estructura de una clase

Una clase en Java se compone de:

- Variables de instancia
- Constructor
- Métodos

A los anteriores se les conoce también como
**miembros de la clase**.

## Estructura de una clase simple

```java
public class IdentificadorClase {
    declaración variables de instancia;

    declaración constructor {
        cuerpo constructor;
    }

    declaración metodo primero() {
        cuerpo método;
    }

    declaración método segundo() {

    }
```

## Variables de instancia

- Son los **atributos de la  clase**.
- Se declaran fuera de cualquier constructor
o método.
- Dependen de la naturaleza del problema que se
esté resolviendo.

### Ejemplos

En la clase **persona**:

- R.U.T.
- Nombre
- Fecha de nacimiento

En la clase **auto**:

- Patente
- Marca
- Modelo
- Año de fabricación

En la clase **casa**:

- Dirección
- Número de pisos
- Número de piezas

En la clase **artículo**:

- Código de inventario
- Nombre
- Unidad de medida
- Stock físico

### Declaración

```java
public class CajaAhorro {
    private int saldo;
    // Modificador de visibilidad - Tipo de dato
    public int transacciones;
    ...
}
```

Se declaran fuera de cualquier constructor o
método.

### Modificadores de visibilidad

El **"modificador de visibilidad"** determina
**quién** puede tener acceso a la variable de la
instancia:

#### Mayor visibilidad `public`

"Todo el mundo" (cualquier otra clase) puede
acceder.

#### Menor visibilidad `private`

Sólo constructores y métodos de la misma clase
pueden acceder.

- Acceso restringido
- Las variables sólo reciben valores que los
constructores y métodos permitan.
- Si los métodos están correctos y hacen las
validaciones adecuadas, el objeto no cae en
inconsistencias.

---

#### Cualquier subclase `protected`

#### Cualquier clase del mismo package `"omisión"`

### Public vs private

Acceso a una variable `public` desde una aplicación
u otra clase:

```java
varRefObj.varInstancia
```

Variables `private`  no pueden ser accedidas desde
otras clases o aplicaciones.

## Constructores

Contienen las instrucciones que se ejecutan al
momento de **crear** una instancia de clase.

Tienen **el mismo nombre que la clase**.

Normalmente se utilizan para **inicializar**
las variables de instancia.

Pueden recibir valores por parámetro

Todas las clases **deben tener** un constructor, el
que se utilizará en la instanciación de objetos de
la clase.

Si se **omite** la implementación del constructor
de una clase, Java proporciona automáticamente un
constructor **sin párametros y sin instrucciones**.

### Ejemplo

```java
public class Caja {
    private int saldo;
    private int transacciones;

    public CajaAhorro(int saldo) {
        this.saldo = saldo;
        this.transacciones = 0;
    }
}
```
