#1. Ingresar “n” números a una lista “num” y posteriormente mostrar:
#a. La suma
#b. El promedio

def promedioSuma():

    suma = int()
    num = list()
    promedio = float()
    n = int(input("Ingrese la cantidad de números sobre los que desea operar"))

    while len(num) < n:
        number = int(input("Ingrese un número"))
        num.append(number)
        suma += number
    promedio = suma / len(num)
    print("El promedio es {}".format(promedio))
    print("La suma total de los numeros es {}".format(suma))
     


#2. Dada una lista con números pares e impares, modificarla de tal manera que los números impares se 
#transformen al número par que lo precede.

listilla = [3,3,3,3,2,6,8,7,7]

def listaPar (lista):
    for index, element in enumerate(lista):
        if element % 2 != 0:
            lista[index] = element + 1
    return lista

listaPar(listilla)
print(listilla)
                


#3. Traspasar los elementos de una lista “a” a una lista “b”.

lista1 = [1,2,10,4,5]
lista2 = [6,7,8,9]

def traspasarElementos(primeraLista, segundaLista):
    primeraLista.extend(segundaLista)
    primeraLista.sort()
    return primeraLista

traspasarElementos(lista2, lista1)
print(lista2)


#4. Mostrar los elementos de una lista “x” de forma inversa.
listaReversa = [1,2,3,4,5]

def listaInversa(lista):
    lista.sort(reverse=True)
    return lista

listaInversa(listaReversa)
print(listaReversa)

#5. Traspasar los elementos de una lista “a” a una lista “b” de forma inversa.

lista_a = [1,2,3]
lista_b = [10,20,30]

def traspasarListaInversa(listaA, listaB):
    listaB.sort(reverse=True)
    listaA.extend(listaB)
    return listaA

traspasarListaInversa(lista_a, lista_b)
print(lista_a)


#6. Llenar una lista con “n” números enteros y posteriormente:
#a. Mostrar la cantidad de números pares
#b. Mostrar la cantidad de números impares

def mostrarParImpar():
    lista = list()
    listaPares = list()
    listaImpares = list()
    n = int(input("Ingrese la cantidad de números que desea ingresar"))
    i = 1
    while len(lista) < n:

        num = int(input("Ingrese el número #{}".format(i)))
        lista.append(num)
        i += 1
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
        else:
            listaImpares.append(i)
    print("Los números que haz ingresado son {}".format(lista))
    print("La cantidad de numeros impares es {}".format(len(listaImpares)))
    print("La cantidad de numeros pares es {}".format(len(listaPares)))

mostrarParImpar()



#7. Mostrar el día de la semana en base a un número ingresado por el usuario.

def mostrarDia():
    num = int(input("Ingrese un número entre 1 y 7"))
    while num < 1 or num > 7:
        num = int(input("Ingrese un número entre 1 y 7"))
    diaElegido = str()
    diasSemana = {
        1:"Lunes",
        2:"Martes",
        3:"Miércoles",
        4:"Jueves",
        5:"Viernes",
        6:"Sábado",
        7:"Domingo"
    }
    for i in diasSemana:
        if num == i:
            diaElegido = diasSemana[i]
    return diaElegido

print(mostrarDia())



#8. Dada una lista “x” traspasar a una lista “a” los pares y a una lista “b” los impares.

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


#9. Crear una lista con números primos

#10. El monto escrito: usando listas cree un programa que permita ingresar una cantidad numérica y 
#escribir en palabras

#a. Inicialmente trabajar con números entre 1 y 999
#b. Luego extender el rango desde 1 a 999999
#Ejemplo: Si el usuario ingresa 673, debe escribir “seiscientos setenta y tres”