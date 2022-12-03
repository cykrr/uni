from random import randint
from math import sqrt
print("Bienvenid@s a GimnasIWI!");

# Inicializamos variables a utilizar
Meta = 0 
CaloriasQuemadas = 0
Ejercicio = -1 # -1 pues no es una opcion válida
NumeroEjercicio = 0

Meta=int(input("Ingrese meta en calorías: "))

while Ejercicio != 4 or CaloriasQuemadas >= Meta:
    print("ingrese ejercicio")

    print(" (1) Sentadillas sumo")
    print(" (2) Plancha abdominal")
    print(" (3) Press frances")
    print(" (4) Me cansé")

    Ejercicio=int(input())
    if Ejercicio == 1:
        Aleatorio = randint(3,7)
        Repeticiones = int(input(("Cuantas repeticiones?")))
        CaloriasRepeticiones = Aleatorio * Repeticiones
        print("Calorias quemadadas con sentadillas sumo: ",
                CaloriasRepeticiones )
        CaloriasQuemadas = CaloriasQuemadas + CaloriasRepeticiones

    if Ejercicio == 2:
        Segundos=int(input("Cuantos segundos?:"))
        CaloriasPlancha = 0

        
        for Segundo in range(1, Segundos +1):
#            print("Segundo: ", Segundo);
            Factorial = 1
            for i in range(1, Segundo+1):
                Factorial = Factorial * i
#            print("Factorial: ", Factorial)

            CaloriasPlancha+=round((4**Segundo)/Factorial)
        print("Calorias quemadas con plancha: ", CaloriasPlancha)
        CaloriasQuemadas = CaloriasQuemadas + CaloriasPlancha

    if Ejercicio == 3:
        print("PRESS FRANCES")
        repeticiones = int(input("Cuantas repeticiones?: "))
        kilos = int(input("Cuantos kilos?: "))

        n = 0
        suma = 0
        
        if repeticiones < kilos:
            n = repeticiones
            suma = kilos

        elif kilos < repeticiones:
            n = kilos
            suma = repeticiones
        else:
            n = kilos
            suma = kilos

        sumando = 0 
        TerminoAnterior = 0
        for i in range(1, n + 1):
            sumando = 1 + sqrt(TerminoAnterior)
            TerminoAnterior = sumando
            suma = suma + sumando

        suma = round(suma)
        print("Calorias quemadas por el press frances: ", suma)
        CaloriasQuemadas=CaloriasQuemadas + suma
    
    if Ejercicio == 4:
        print("********")
        print("Quemaste ", CaloriasQuemadas, "calorias")
        exit(0)


    if Ejercicio <= 0 or Ejercicio > 4:
        print("Ingrese una opcion valida")

    if CaloriasQuemadas != 0:
        print("Calorias quemadas hasta el momento: ", CaloriasQuemadas)
    if CaloriasQuemadas >= Meta:
        break
 

    NumeroEjercicio = NumeroEjercicio + 1
if CaloriasQuemadas >= Meta:
    print("Quemaste ", CaloriasQuemadas, " de un total de ", Meta, "Calorias")


