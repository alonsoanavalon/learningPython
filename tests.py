nums = [1,2,45,7,8,54,34,21]

""" while True:
    for n in nums:
        print(n)
        if n == "54" or n == 54:
            break
    break """

""" 
while True:
    try:
        num = float(input("Ingrese su número favorito"))    
        break
    except ValueError:
        print("No ha ingresado un valor válido") """

""" tries = 3
for i in range (tries):
    print(i +1 ) """

"""     #String of characters
alpha_string = "abcdefghijklmnopqrstuvwxyz"

#Convert it to a list using list()
alpha_list = list(alpha_string)
print(alpha_list) """

""" lista = [1,2,3,'a',True,'alonso']
nums = [1,2,3,4,5,6,7]


lista.append('perrito')



for n in nums:
    print(nums.index(n)) """


""" def findInString (string, word):

    print(isinstance(string, str))
    print(isinstance(word, str))

    while True:
        try:
            if isinstance(string, str) and isinstance(word, str):
                print("Todo ok")
                stringToLower = string.lower()
                isWord = stringToLower.find(word)
                if isWord != -1:
                    print("Su palabra se ha encontrado en la posición {}".format(isWord))
                else:
                    print("Su palabra {} no ha sido encontrada".format(word))
                break
            else:
                raise ValueError()
        except ValueError:
            print("Ha ocurrido un error")
            break


frase = "A la melisa le gusta la lasaña"

frase_list = frase.split()
print(frase_list) """

""" nome = "Alonso como estas";
nome = nome.split()
print(nome)

rut = 19238587
print(rut%10)
rut = int(rut/10)
print(rut)
rut = int(rut/10)
print(rut)
rut = int(rut/10)
print(rut)
rut = int(rut/10)
print(rut)
rut = int(rut/10)
print(rut)
 """
""" while rut >  0:
    restoRut = rut % 10
    print(restoRut, "Resto rut")
    rut = rut/10
    print(rut, "RUT") """
 


""" while rutMelisa > 0:
    restoRut = rutMelisa % 10
    print(restoRut)
    rutMelisa = int(rutMelisa /10) """
    

""" print(map(int, str(rutMelisa)))

res = [int(x) for x in str(rutMelisa)]
print(res) """

""" 32765432 / 11 """
""" 19262479 """

""" Primero modo profe """





lista = ["Uno", "dos", "tres", "cuatro"]
lista.insert(1, "kaka")
print(lista)
        



