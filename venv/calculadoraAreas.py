from math import pi, tan
import math
from datetime import datetime, date, time, timedelta
import calendar

calculadoraEncendida = True

# funcion que valida que el dato ingresado por el usuario sea un numero flotante
def inputNumber(mensaje):
    while True:
        try:
            userInput = float(input(mensaje))
        except ValueError:
            print("ERROR Usted no digito un numero, pruebe nuevamente.")
            continue
        else:
            return userInput

# Funcion para obtener la fecha y hora del sistema
def fechaHora():
    fecha_hora = datetime.now()
    print("Fecha y hora: " + str(fecha_hora) + "\n")
    return

# Funcion que calcula el area de un circulo
def areaCirculo():
    radio = float(inputNumber("Ingrese el valor del radio del circulo para calcular su area respectiva: "))
    while radio <= 0:
        radio = float(inputNumber(
            "ERROR El valor del radio no puede ser negativo ni cero. Porfavor ingrese el valor del radio del circulo para calcular su area respectiva: "))

    area = float(math.pi * math.pow(radio, 2))
    print("El area del circulo es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un cuadrado
def areaCuadrado():
    lado = float(inputNumber("Ingrese el valor del lado del cuadrado para calcular su area: "))

    while lado <= 0:
        lado = float(inputNumber("ERROR El valor del lado no puede ser negativo ni cero. Porfavor ingrese el valor del "
                                 "lado del cuadrado: "))

    area = float(math.pow(lado, 2))
    print("El area del cuadrado es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un rectangulo
def areaRectangulo():
    base = float(inputNumber("Ingrese el valor de la base del rectangulo para calcular su area: "))
    altura = float(inputNumber("Ingrese el valor de la altura del rectangulo para calcular su area: "))

    while base <= 0 or altura <= 0:
        print("ERROR El valor de la base o la altura no puede ser negativo o cero")
        base = float(inputNumber("Ingrese el valor de la base del rectangulo para calcular su area: "))
        altura = float(inputNumber("Ingrese el valor de la base del rectangulo para calcular su area: "))

    area = float((base * altura))
    print("El area del rectangulo es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un rombo
def areaRombo():
    diagonalMayor = float(inputNumber("Ingrese el valor de la Diagonal Mayor del Rombo para calcular su area: "))
    diagonalMenor = float(inputNumber("Ingrese el valor de la Diagonal Menor del Rombo para calcular su area: "))

    while diagonalMayor <= 0 or diagonalMenor <= 0:
        print("ERROR El valor de las diagonales no puede ser negativo o cero")
        diagonalMayor = float(inputNumber("Ingrese el valor de la Diagonal Mayor del Rombo para calcular su area: "))
        diagonalMenor = float(inputNumber("Ingrese el valor de la Diagonal Menor del Rombo para calcular su area: "))

    area = float(((diagonalMayor * diagonalMenor) / 2))
    print("El area del Rombo es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un romboide
def areaRomboide():
    base = float(inputNumber("Ingrese el valor de la base del romboide para calcular su area: "))
    altura = float(inputNumber("Ingrese el valor de la altura del romboide para calcular su area: "))

    while base <= 0 or altura <= 0:
        print("ERROR El valor de la base o la altura no puede ser negativo o cero")
        base = float(inputNumber("Ingrese el valor de la base del romboide para calcular su area: "))
        altura = float(inputNumber("Ingrese el valor de la altura del romboide para calcular su area: "))

    area = float((base * altura))
    print("El area del romboide es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un trapecio
def areaTrapecio():
    baseMayor = float(inputNumber("Ingrese el valor de la base mayor del trapecio para calcular su area: "))
    baseMenor = float(inputNumber("Ingrese el valor de la base menor del trapecio para calcular su area: "))
    altura = float(inputNumber("Ingrese el valor de la altura del trapecio para calcular su area: "))

    while baseMayor <= 0 or altura <= 0 or baseMayor <= 0:
        print("ERROR El valor de las bases o la altura no puede ser negativo o cero")
        baseMayor = float(inputNumber("Ingrese el valor de la base mayor del trapecio para calcular su area: "))
        baseMenor = float(inputNumber("Ingrese el valor de la base menor del trapecio para calcular su area: "))
        altura = float(inputNumber("Ingrese el valor de la altura del trapecio para calcular su area: "))

    area = float((altura * ((baseMayor + baseMenor) / 2)))
    print("El area del trapecio es: " + str(area) + " cm2" + "\n")
    return

# Funcion que calcula el area de un poligono regular de X cantidad de lados
def arePoligonoRegular():
    numeroLados = float(inputNumber(" Ingrese el numero de lados del poligono para calcular su area: "))
    longitudLados = float(inputNumber("Ingrese la longitud del lado del poligono para calcular su area: "))

    while numeroLados <= 0 or longitudLados <= 0:
        print("ERROR Los datos para numero de lados o longitud no pueden ser menores o iguales a cero")
        numeroLados = float(inputNumber("Por favor ingrese el numero de lados del poligono para calcular su area: "))
        longitudLados = float(inputNumber("Por favor ingrese la longitud del lado del poligono para calcular su area: "))

    area = float((numeroLados * math.pow(longitudLados, 2)) / (4 * tan(pi / numeroLados)))
    print("El area del Poligono regular de " + str(numeroLados) + " lados es: " + str(area) + " cm2" + "\n")
    return


while calculadoraEncendida: #calculadoraEncendida funciona con un boolean statement para identificar si me salgo o no del sistema
    seleccion = input("En el siguiente Menu, seleccione la opcion que desea calcular para las figuras geométricas: \n \n 1. Area del Circulo \n 2. Area del "
                      "Cuadrado \n 3. Area del Rectangulo \n 4. Area del Rombo \n 5. Area del Romboide \n 6. Area del "
                      "trapecio \n 7. Area del poligono regular \n 8. Salir del sistema \n \n ")
    if seleccion == "1":
        areaCirculo()
    elif seleccion == "2":
        areaCuadrado()
    elif seleccion == "3":
        areaRectangulo()
    elif seleccion == "4":
        areaRombo()
    elif seleccion == "5":
        areaRomboide()
    elif seleccion == "6":
        areaTrapecio()
    elif seleccion == "7":
        arePoligonoRegular()
    elif seleccion == "8":
        calculadoraEncendida = False
        print("Hasta pronto, fue un gusto ayudarle. \n")
        fechaHora()
    else:
        print("La opcion seleccionada no es correcta, intente de nuevo.")
