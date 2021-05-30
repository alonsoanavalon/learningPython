cantidad_notas = int(input("Ingrese la cantidad de notas que quiere ingresar"))
i = 1
suma = 0

while cantidad_notas >= i:

    

    nota = float(input("Ingrese la nota {}".format(i)))

    while nota > 7 or nota < 1:
        print("Debe ingresar una nota menor a 7 y mayor a 1")
        nota = float(input("Ingrese la nota {}".format(i)))

    suma += nota

    if (i == 1):
        nota_menor = nota
        nota_mayor = nota
    else:
        if nota > nota_mayor:
            nota_mayor = nota
        elif nota < nota_menor:
            nota_menor = nota
    i += 1
print("El promedio de notas es {} ".format(suma / cantidad_notas))
print("La nota menor es {}".format(nota_menor))
print("La nota mayor es {}".format(nota_mayor))
    