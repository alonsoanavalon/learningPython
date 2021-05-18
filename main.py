""" Hola mundo """
print('Hello world')

""" Funcion con parametros determinados """
def suma (a,b):
    return a+b

result = suma(2,43)
print(result)

""" Funcion con parámetros indeterminados """

def saludar_personas(*personas):
    for persona in personas:
        print("Hola {} como estás?".format(persona))

saludar_personas("Javiera", "Rodrigo", "Antonio")

""" Ciclo for básico"""

for i in range (6):
    print("Hola como tay?", i)

""" Ciclo for con inicio y fin"""
for i in range (1,8):
    print("Hola inicio y fin", i)

""" Ciclo for que cuenta de tanto en tanto """

for i in range (1,10,2): 
    print(i)
#Cuenta de 1 a 9 en pares

""" Ciclo for trabajando con tupla """

nums = [10,5,3,7,11 ,20,30,40,50]

for n in nums:
    print(n)

""" Ciclo for trabajando con tupla y condicional """

for n in nums:
    if n % 2 == 0:
        print("{} es par".format(n))
    else:
        print("{} es impar".format(n))

""" Creando clase """

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

alonso = Persona('alonso', 'anavalon')
print(alonso.nombre)
print(alonso.apellido)