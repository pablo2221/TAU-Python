#Practica 1: Sea msj= "Hola Mundo", imprima en pantalla la variable msj.

mensaje = "Hola mundo"
print(mensaje)

#Usando la variable anterior obtenga
"""
mensaje[3]
mensaje[7]
mensaje[8]
mensaje[2:6]
mensaje[3]
mensaje[:9]
"""
mensaje = "hola mundo"
print(mensaje[3])
print(mensaje[7])
print(mensaje[8])
print(mensaje[2:6])
print(mensaje[3:])
print(mensaje[:9])

#Practica 2:

#1: concatene usando python los textos "Hola mundo", "pura vida", "jaja"

c1="Hola mundo "
c2="pura vida "
c3 = "jaja"

mensaje_concatenado = c1+c2+c3
print(mensaje_concatenado)

#2: Muestre 4 veces el string "Pura Vida CR"

msj = "Pura Vida CR "
print(msj * 4)

#3: Verifique si la palabra "pura" esta en el texto "Pura vida Costa Rica"

'Pura' in 'Pura vida costa rica'

#PRACTICA 3

"""
1:
Sea Txt=“ Viva la Sele , somos ticos“
Muestre el tamaño de Txt
Convierta a mayúscula el texto de la variable
Convierta a minúscula el texto de la variable
"""

Txt = "Viva la Sele, somos ticos"
print(len(Txt))
print (Txt.upper())
print (Txt.lower())

"""
2) Solicite al usuario digitar una oración, luego:
Muestre en pantalla la oración digitada
Convierta a mayúscula la primera letra 
Muestre todas las su cadenas contenidas en la oración
"""

oracion = input("Por favor digite una oracion de su gusto ")
print("La oracion digitada es: "+oracion)
print("Asi se convierte la primer letra a Mayuscula: "+oracion.capitalize())

#PRACTICA 4

"""
1.Solicite al usuario ingresar un numero entero, luego convierta a string y muéstrelo.
2. Pida ingresar cualquier numero entero, luego convierta a flotante y muéstrelo.
3. Convierta un numero decimal cualquiera a cadena y muestrelo
"""

numero_entero = int(input("Por favor ingresar un numero entero para convertirlo a string y mostrarlo: "))
print(str(numero_entero))

numero_entero2 = int(input("Por favor ingresar un numero entero para convertirlo a float y mostrarlo: "))
print(float(numero_entero2))

numero_entero3 = float(input("Por favor ingresar un numero decimal para convertirlo a string y mostrarlo: "))
print(str(numero_entero3))

#PRACTICA 5

#1: Asigne a 3 variables diferentes los valores 7,9 y 11 respectivamente.
v1, v2, v3 = 7, 9, 11
print(v1, v2, v3)

#2: Asigne a pi y e , sus valores decimales respectivos(use 2 decimales). Muestre el contenido de ellas.
pi = 3.14
e = 2.71

#3: Intercambie el contenido de las variables del punto 2

pi, e = e, pi
print(pi ,e)

#4: Solicite al usuario ingresar 3 textos, forme una oracion con ellos y muestre el resultado

oracion1 = input("Ingrese una oracion: ")
oracion2 = input("Ingrese una segunda oracion: ")
oracion3 = input("Ingrese una tecera oracion: ")

print("La nueva oracion es: "+oracion3+" "+oracion2+" "+oracion1)

#PRACTICA 6

"""
Escribir un programa, que solicite al usuario una oración, luego debe:
   a. Solicitar la búsqueda de un substring indicando posición inicial y posición final (el usuario lo indica)
   b. Obtener un substring desde la posición x, luego convertirlo a mayusculas
"""

oracion = input("Digite una oracion")
posicion_inicial = int(input("Ingrese la posicion inicial a empezar el substring de la oracion: "))
posicion_final = int(input("Ingrese la posicion final a terminar el substring de la oracion: "))

posicionX = int(input("Ingrese la posicion X a empezar el substring de la oracion: "))
print(oracion[posicionX:].upper())
