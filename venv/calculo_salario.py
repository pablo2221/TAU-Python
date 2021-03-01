salarios_mayores = 0
salarios_menores = 0
on_off = 0
sumaConversionDolares = 0
while on_off != -1:
    salario = float(input("Ingrese el salario en colones: "))
    conversion_dolares = (salario / 800)
    print("El salario en Colones era de: " + str(salario) + " pero luego de convertirlo a dolares es de: $" + str(conversion_dolares))
    sumaConversionDolares = sumaConversionDolares + conversion_dolares
    if conversion_dolares >= 800:
        salarios_mayores += 1
    else:
        salarios_menores += 1

    print("La cantidad de salarios mayores a $800 es: "+str(salarios_mayores))
    print("La cantidad de la suma de los salarios es $: " + str(sumaConversionDolares))

    on_off = int(input("Digite -1 si desea salir del sistema: "))
