# Ejemplo 4: Escriba un program que permita llenar una lista de 9 alumnos de un curso de programacion, el programa
# debe permitir agregar un alumno pero antes verifique si ese alumno existe, si no existe se agrega

alumnos = ["Pablo", "Andres", "Ana", "Carlos", "Pedro", "Luis", "Maria", "Andrea", "Juna"]
nuevo_alumno = input("Ingrese el nombre de un nuevo alumno: \n")

resultado = nuevo_alumno in alumnos #Busqueda del alumno en la lista
if resultado:
    print("No se puede agregar un alumno que ya se encuentra en la lista")
else:
    print("El alumno sera agregado a la lista")
    alumnos.append(nuevo_alumno)

print("La nueva lisga de alumnos es: \n")
print("============================================= \n")
print(alumnos)