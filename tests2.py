lista = [1,2,3,4,5]
def mostrarParImpar(lista):
    listaPares = list()
    listaImpares = list()
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
    print("Los números que haz ingresado son {}".format(lista))
    print("Los números impares son {}".format(listaImpares))
    print("Los números pares son {}".format(listaPares))

mostrarParImpar(lista)
