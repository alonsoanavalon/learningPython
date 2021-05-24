
limitNumber = int(input("Cuantos numeros desea obtener?"))
contador = 3

primerNumero = 0
segundoNumero = 1
suma = primerNumero + segundoNumero


print(primerNumero)
print(segundoNumero)
print(suma)

while limitNumber > contador:

    primerNumero = segundoNumero
    segundoNumero = suma
    suma = primerNumero + segundoNumero
    print(suma)

    contador = contador+1 