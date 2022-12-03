# Principios OOP

"_La mitad de la pelea es saber cual es el problema a resolver._"

## De problemas a soluciones

Análisis: entender el problema y sus requerimientos.

Diseño: determinar un modelo que nos permita resolver el problema.

Implementación: determinar la forma de representar el modelo que
describe el problema (y la solución).

## Los requerminentos

Los requerimientos tienden a ser incompletos, a estar equivocados, a ser
engañosos y no contar la historia completa, por lo tanto, es común que
los requisitos cambien.

## Metodologías y modelos

La ingeniería de software provee metodologías de desarrollo, modelos
para soportar el desarrollo y lenguages para la implementación. Esto se
verá más adelante en el curso de _Modelamiento de Sistemas_.

## OOP

El paradigma de la orientación a objetos es sucesor de la [descomposición
funcional](http://cv.uoc.edu/UOC/a/moduls/90/90_331/web/main/m2/Ejemplo2_3_2a.html#:~:text=La%20descomposici%C3%B3n%20funcional%20nos%20se%C3%B1ala,conocimientos%20para%20obtener%20un%20producto.).

Se sabe que OOP se centra en el concepto de Objeto, donde

$$
\text {Objeto = Datos + Métodos}_{\text{(Definición tradicional)}}
$$

Los objetos son responsables de sí mismos, "saben" de que tipo son, conocen
su propio estado, es decir, sus datos y contienen el código que les permite
actuar.

## OOP vs. Descomposición funcional

El modelo de programación funcional mantiene centralizadas las
responsabilidades, por ejemplo:

_"Una cena en la cual un garzón pide a cada comensal lo que se servirá, y
luego les trae los platos solicitados."_

El modelo **OOP** provee delegación de responsabilidades:

_"Una cena en la cual los comensales se les indica la distribución del
buffet. Ellos se sirven a su propio gusto."_

## Identificación de Objetos

En problemas pequeños una técnica sencilla se basa en la identificación de
sustantivos y verbos, de forma que los sustantivos pueden ser objetos y los
verbos pueden ser métodos.

## Objetos

Una buena forma de concebir un objeto es pensar en él como una **entidad con
responsabilidades.**  Las responsabilidades determinan el **comportamiento**
del objeto.

Debe existir una forma de comunicar a un objeto qué debe hacer. Esta
comunicación se logra por medio del **conjunto de métodos** que un objeto
orfrece para que **otros puedan invocar**.

El conjunto de estos métodos se denomina como la **interfaz pública del objeto**.

## Visión de Objetos

Martin Fowler identifica tres perspectivas para describir los objetos:

* **Nivel conceptual**: Un objeto es un conjunto de responsabilidades.
* **Nivel especificación**: Un objeto es un conjunto de métodos
(comportamientos) que pueden ser invocados por otros objetos o por sí mismos.
* **Nivel implementación**: Un objeto es código y datos, junto con las
interacciones computacionales entre ellos.

## Ejemplo de perspectivas OOP

Imagine un sistema de docencia que mantiene datos de alumnos y registra sus
inscripciones en cursos.

Se realizará el analisis partiendo en lo conceptual, pasando por la
especificación y terminando con la implementación.

### Nivel conceptual

Responsabilidades:

Alumno: Mantener datos de un alumno (rol y nombre). Debe validar el rol del
alumno.

Curso:

* Mantener datos de un curso (nombre).
* Mantener la lista de alumnos que se inscriben en el curso, verificando que
estos no se repitan al momento de agregarlos.
* Retornar alumnos, buscándolos por rol del alumno.

### Nivel especificación

```python

class Alumno:
    def set_rol(numero, verificador);
    def set_nombre(nombre);
    def get_rol();
    def get_Nombre();

class Curso:
    def set_nombre(nombre);
    def add_alumno(alumno);
    def get_alumno();
```

### Nivel implementación

```python
class Alumno:
    rol = ""; nombre = "";

    def set_rol(self, numero, verificador):
        if __suma_digitos(numero) == verificador:
            self.rol = rol + "-" + verificador;

    def  set_nombre(self, nombre):
        self.nombre = nombre;

    def get_rol(): 
        return rol;

    def get_nombre():
        return nombre;

    ## "__" simula el espacio privado en Python

    def __suma_digitos(num):
        ...
```

## Precauciones

_"Todos los sistemas cambian durante su ciclo de vida. Esto debe ser tomado en
cuenta a la hora de desarrollar sistemas que duren más que la primera
versión."_

## POO y encapsulación

Tradicionalmente se asocia al **"ocultamiento de datos"** (estado) de un
objeto. Sin embargo, además hace referencia al ocultamiento de:

* Implementaciones de métodos
* Tipo y clases derivadas
* Detalles de diseño
* Reglas de instanciación

### Encapsulación como ocultamiento de datos

Tome por ejemplo la siguiente clase:

```python
class Vector:
    # Self = This
    # Constructor
    def __init__(self, x, y):
        self.__coord_a = x;
        self.__coord_b = y;

    def get_x(self):
        return self.__coord_a;

    def get_y(self):
        return self.__coord_b;
```

El "contexto" de la clase Vector no tiene visibilidad de cómo almacena sus
datos. Por consecuencia, puede modificarse el conjunto de variables de la
clase Vector sin que esto afecte su contexto.

### Encapsulación en la implementación de métodos

```python

class Angle:
    def __init__(self, angle):
        self.angle = angle;
    def set_angle(self, a):
        self.angle = a
    def get_sin(self):
        ... 
        pass # Nada
```

El "contexto" de la clase Angle no tiene visibilidad del algoritmo de cálculo
de seno del ángulo. Por consecuencia, puede modificarse la implementación del
método sin afectar al contexto.

### Encapsulación del tipo

Suponga una clase **Figura** con los métodos de dibujar rellenar y ocultar.
Suponga además tres clases hijas de **Figura**, respectivamente **Rombo,
Cuadrado y círculo, Cuadrado y círculo**.

El "contexto" de las figuras no tiene visibilidad de cuál de ellas está
exactamente utilizando. Por consecuencia, el contexto puede implementar una
lógica común para utilizar cualquiera de las figuras (o cualquier subclase).

Suponga una clase **Banco** con métodos  para recibir y atender clientes.
Este banco posee una **Cola** con métodos para agregar y quitar clientes,
junto con un **Cajero** que atiende los clientes en la Cola.

El "contexto" de la clase **Banco** no tiene visibilidad de las clases
que soportan sus operaciones. Por consecuencia, puede modificarse la
arquitectura del Banco sin afectar su contexto.

### Encapsulación de las reglas de instanciación

```python
#@ Singleton
class DaVinci:
    instance = None;
    def __init__(self):
        pass
    def get_DaVinci():
        if instance == None:
            instance = DaVinci();
        return instance
```

## Encapsulación y diseño

Muchos patrones de diseño (soluciones a problemas comunes de diseño)
utilizan la encapsulación de tipos para crear capasa de separación entre objetos.

La separación se crea asignando referencias a clases abstractas o interfaces.

Esto permite modificar algno de los "lados" de la capa sin afectar a otra.

### Principio abierto-cerrado (OCP)

_"Las entidades de software (clases, módulos, funciones, etc) deberían estar
**abiertos para extensión y cerrados para modificaciones**"_.

En otras palabras, el software debe ser diseñado para soportar la adición de
nuevas funcionalidades sin que esto signifique en modificacione de aquellas
ya existentes.

"Regla" de diseño: estableces visibilidad "privada" a variables de instancia.

Los conceptos de **abstracción y polimorfismo** del principio "abierto-cerrado"
están asociados a la especificación de **jerarquías de herencia**.

No siempre es posible seguir completamente este principio.

### Síntomas de un mal diseño

Al modificar un módulo de software, los cambios se propagan a otros módulos.

Por lo tanto se deben diseñar módulos que nunca cambiarán. Si los requerimientos
cambian, se debe extender el comportamiento de tales módulos, agregando nuevo
código, no modificando aquél existente.

La base de este principio está en los conceptos de abstracción y polimorfismo.

## Principio de sustitución de Liskov (LSP)

_"Las funciones que utilizan punteros o referencias a clases de base, deben ser
capaces de utilizar subclases de éstas, sin necesidad de conocerlas"_.

Cualquier propiedad que sea cierta para una súperclase, debe serlo también para
sus subclases.

Un cliente de una clase debe funcionar correctamente con cualquier subclase de
esta última

## Principio de inversión de dependencia (DIP)

Establece como implementar los objetivos enunciados por el OCP y el LSP.

_"Los módulos de alto nivel no deberían depender de los módulos de bajo nivel.
Ambos deberían depender de las abstracciones. Las abstracciones no deberían
depender de detalles. Los detalles deberían depender de abstracciones."_

El principio propone la estrategia de depender de abstracciones (interfaces,
funciones abstractas y/o clases abstractas), en vez de depender de funciones y
clases concretas.

## Agentes de software

Los objetos ofrecen una interfaz pública por medio de la cual otros objetos
invocan sus comportamientos. Son inherentemente **reactivos**: su comportamiento
es gatillado por la acción externa de otro objeto.

Los agentes de software son unidades de software con **objetivos y responsabilidades**.

Exhiben un **comportamiento proactivo**: un agente actúa por cuenta propia sobre
el ambiente y otros agentes para alcanzar sus objetivos.
