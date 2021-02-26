"""#ejemplo 1: pregunta numero a usuario hasta que ingresa el valor cero

num = None
while (num != 0):
    num = int(input("Introduzca un numero: "))

while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break

#calcular la sumatoria de 7 numeros

contador = 0
acumulador = 0

while contador < 7:
    numero = int(input("ingrese el {} numero: ".format(contador+1)))
    acumulador = acumulador + numero
    contador +=1

print("El resultado de la suma es: ", acumulador)

#lee palabra e imprime letra por letra

palabra = "Pablo programa en Python"

for letra in palabra:
    print(letra)

# imprime numerso de 2 en 2 usando inicio 1 y sale en 10

for i in range (1,10,2):
    print(i)

"""
# pide 10 numeros y suma los impares ingresados

acumulador = 0

for i in range (1, 11):
    numero = int(input("Ingrese un numero entero: "))
    if (numero%2 == 1):
        acumulador = acumulador+numero


print("La suma corresponde a: ",acumulador)


