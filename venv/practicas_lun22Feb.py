
"""PRACTICAS CON EL CICLO WHILE"""

# ejercicio 1  escriba un programa para calcular el  producto de 4 numeros enteros

contador = 0
acumulador = 1

while contador < 4:
    numero = int(input("ingrese el {} numero: ".format(contador+1)))
    acumulador = acumulador * numero
    contador +=1

print("El resultado de la multiplicaion es: ", acumulador)

# ejercicio 2  calcula el promedio de 10 numeros

contador = 0
acumulador = 0

while contador < 10:
    numero = int(input("ingrese el {} numero: ".format(contador+1)))
    acumulador = acumulador + numero
    contador +=1

print("El promedio de los numeros es: ", (acumulador/10))

# ejercicio 3  pide 12 numeros y suma pares e impares

contador2 = 0
acumuladorPar = 0
acumuladorInpar = 0

while contador2 < 3:
    numero = int(input("Ingrese un numero entero: "))
    if (numero%2 == 1):
        acumuladorInpar = acumuladorInpar+numero
    else:
        acumuladorPar = acumuladorPar + numero

    contador2 +=1


print("La suma de impares corresponde a: "+str(acumuladorInpar)+", La suma de los pares corresponde a: "+str(acumuladorPar))

# ejercicio 4  pide 15 numeros y suma positivos y negativos

contador3 = 0
acumuladorPos = 0
acumuladorNeg = 0

while contador3 < 5:
    numero = int(input("Ingrese un numero entero: "))
    if (numero >= 0):
        acumuladorPos = acumuladorPos+numero
    else:
        acumuladorNeg = acumuladorNeg + numero

    contador3 +=1


print("La suma de Positivos corresponde a: "+str(acumuladorPos)+", La suma de los negativos corresponde a: "+str(acumuladorNeg))

"""PRACTICAS CON EL CICLO FOR"""

#Practica 1: Escriba un programa que solicite 20 números y calcule la suma de los positivos y la suma de los negativos

acumuladorPos = 0
acumuladorNeg = 0

for i in range (1, 2):
    numero = int(input("Ingrese un numero entero: "))
    if (numero >= 0):
        acumuladorPos = acumuladorPos+numero
    else:
        acumuladorNeg = acumuladorNeg+numero


print("La suma de Positivos corresponde a: "+str(acumuladorPos)+", La suma de los negativos corresponde a: "+str(acumuladorNeg))

#Practica 2: Solicite el precio unitario de 30 artículos , calcule y muestre : IV (impuesto de venta ) de cada articulo Precio total

for i in range (1, 3):
    precioArticulo = int(input("Ingrese el precio del articulo: "))
    print("El impuesto de venta del articulo es: "+str(precioArticulo*0.13)+", Y el precio con el impuesto es: "+str(precioArticulo+(precioArticulo*0.13)))

#Practica 3: Calcule el factorial de n, el usuario ingresa n

numeroFactorial = int(input("Ingrese un numero:"))
contador = 1
z = 1
while z <= y:
    acumulador = acumulador * z
    z = z + 1
print("El factorial de "+str(numeroFactorial)+" es: "+str(acumulador))



