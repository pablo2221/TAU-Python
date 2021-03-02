"""
Practicas del Jueves 18 de Febrero curso de introduccion a la programacion con Python
"""

"""ejemplo 1"""

x = int(input("Ingrese un numero: "))

if (x%2 == 0):
    print("{} es un numero par \n".format(x))
else:
    print("{} es un numero inpar".format(x))



#ejemplo 1

x = float(input("Ingrese el numero para x: "))
y = float(input("Ingrese el numero para y: "))

if (x > y):
    print("{} es mayor que  {}".format(x, y))
elif (y > x):
    print("{} es mayor que  {}".format(y, x))
else:
    print("X y Y son numeros son iguales")



#Practica 1
# ejercicio 1

nota = float(input("Por favor ingrese la nota del alumno: "))

if (nota >= 70 and nota <=100):
    print("El alumno aprobo el curso ya que la nota es: {}".format(nota))
elif (nota >= 60 and nota <=69):
    print("El alumno aplazo el curso")
else:
    print("El alumno reprobo el curso")

# ejercicio 2

numero2 = int(input("Ingrese un numero: "))

if (numero2 > 0):
    print("El numero {} es positivo".format(numero2))
elif (numero2 < 0):
    print("El numero {} es negativo".format(numero2))
else:
    print("El numero es nulo")

# ejercicio 3

temperatura = float(input("Ingrese la temperatura en grados centigrados: "))

if (temperatura >= 30):
    print("La temperatura es alta")
else:
    print("La temperatura es moderada")

# ejercicio 4

salario = float(input("Ingrese el salario del colaborador: "))

if (salario >= 600000):
    print("El salario es alto")
elif (salario >= 200000):
    print("El salario es bajo")
else:
    print("El salario es promedio")

# ejercicio 5

precio_unitario = float(input("Ingrese el precio del articulo: "))

if (precio_unitario < 50000):
    print("El precio del articulo era {} pero el nuevo precio con un 6% de descuento es: ".format(precio_unitario)+ str(precio_unitario-(precio_unitario*0.06)))
elif (precio_unitario >= 50000 and precio_unitario <=150000):
    print("El precio del articulo era {} pero el nuevo precio con un 10% de descuento es: ".format(precio_unitario) + str(precio_unitario - (precio_unitario * 0.01)))
elif (precio_unitario > 150000):
    print("El precio del articulo era {} pero el nuevo precio con un 15% de descuento es: ".format(precio_unitario) + str(precio_unitario - (precio_unitario * 0.015)))

#ejercicio 6

letra = str(input("Ingrese una letra del alfabeto: "))

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("La letra es una vocal minuscula")
elif(letra == "A" or letra == "E" or letra == "O" or letra == "I" or letra == "U"):
    print("La letra es una vocal mayuscula")
elif (letra.isupper() == True):
    print("La letra es una consonante mayuscula")
else:
    print("La letra es una consonante minuscula")







