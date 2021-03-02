"""# Ejemplo 4: Escriba un program que permita llenar una lista de 9 alumnos de un curso de programacion, el programa
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

# Practica: Escriba un programa que almacena una lista las notas finales de 15 alumnos de un curso de matematicas. El
# programa debe: calcular el promedio de las notas del curso, obtener la nota mayor, obtener la nota menor,
# El rango de notas, eliminar una nota del curso
"""
def promedio_notas(lista):
    print("El promedio de notas de los alumnos del curso es: "+str(sum(lista)/len(lista))+"\n")

def nota_mayor(lista):
    print("La nota mas alta del curso es: "+str(max(lista))+"\n")

def nota_menor(lista):
    print("La nota mas baja del curso es: "+str(min(lista))+"\n")

def rango_nota(lista):
    print("El rango de notas del curso es de: "+str(max(lista)-min(lista))+"\n")

def eliminar_nota(lista):
    dato=float(input("De la lista de notas, ingrese la nota a eliminar \n"))
    lista.remove(dato)
    print("Ahora la lista se muestra de la siguiente forma: "+str(lista)+"\n")

def seleccion_menu(opcion, lista):
    if(opcion==1):
        promedio_notas(lista)
    elif(opcion==2):
        nota_mayor(lista)
    elif(opcion==3):
        nota_menor(lista)
    elif(opcion==4):
        rango_nota(lista)
    elif(opcion==5):
        eliminar_nota(lista)
    else:
        print("Opcion invalida")


seleccion_menu(1,[45,34,67,89,87,67,67,67])