"""Esta es una de las primeras practicas del curso
intro a la progra con Python, utilizamos version 3.9."""

#Este es la practica 1
nombre = input("Hola Digite su nombre por favor ")
print("su nombre es {}".format(nombre))

#Esta es la practica 2
provincia = input("Digite el nombre de su provincia: ")
print("La provincia de residencia es: {}".format(provincia))

#Esta es la practica 3
def datos_persona(nombre, correo, cedula, carrera, telefono):

    print("Hola {}, su correo electronico es {}, su cedula es {}, actualmente estudias la carrera de {} y su numero "
          "de telefono es {}".format(nombre, correo, cedula, carrera, telefono))
name = input("Hola digite su nombre ")
email = input("Hola digite su correo ")
id = input("Hola digite su cedula ")
career = input("Hola digite su carrera ")
phone = int(input("Hola digite su telefono "))


datos_persona(name, email, id, career, phone)

#Esta es la practica 4, calculo de area de triangulo

base = int(input("Digite la medida de la base: "))
altura = int(input("Digite la medida de la altura: "))
area = ((base*altura)/2)

print("El resultado del area del triangulo es: {}".format(area))

#Esta es la practica 5, convertir monto de colones a dolares y euros

monto_colones = float(input("Digite el monto en colones"))
conversion_dolares = str(monto_colones/604)
conversion_euros = str(monto_colones/717)

print("El monto en dolares es: "+conversion_dolares+" Y la conversion en Euros es: "+conversion_euros)



