#Ejemplo: 1 funcion que imprime
def bienvenida ():
    nombre = input("Por favor ingrese su nombre: ")
    print("Bienvenido a python "+nombre)
    return

bienvenida()

#Ejemplo: 2 funcion que imprime con parametros
def bienvenida (nombre):
    print("Bienvenido a python "+nombre)
    return

bienvenida("Pablo")

# Ejemplo: 3 calculo de area de triangulo

def areaTriangulo(base, altura):
    area = (base*altura)/2
    print("El area del triangulo es: "+str(area))
    return

areaTriangulo(2, 4)
areaTriangulo(4, 7)

# Ejemplo: 4 calcular hipotenusa de un triangulo

import math

def hipotenusa(c1,c2):
      h=math.sqrt((pow(c1,2)+pow(c2,2)))
      return h

print("La hipotenusa del triangulo es :", hipotenusa(3,4))

