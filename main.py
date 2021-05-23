from datetime import datetime

""" Hola mundo """
print('Hello world')

""" Funcion con parametros determinados """
def suma (a,b):
    return a+b

result = suma(2,50)
print(result)

""" Funcion con parámetros indeterminados """

def saludar_personas(*personas):
    for persona in personas:
        print("Hola {} como estás?".format(persona))

saludar_personas("Pepe", "Nose", "Malcolm")

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
    contador = 0
    reino = "animal"
    
    def __init__(self, nombre, apellido, nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        Persona.contador+=1
        
    def devolver_edad(self):
        return datetime.today().year - self.nacimiento
    def comer(self, comida):
        print("Hola soy {} y quiero comer {}".format(self.nombre, comida))
    def isReino(self):
        print("Hola soy {} y pertenezco al reino {}".format(self.nombre, Persona.reino))

alonso = Persona('alonso', 'anavalon', 1995)
print(alonso.nombre)
print(alonso.apellido)
print(alonso.devolver_edad())
















alonso.comer('pizza')
melisa = Persona("Melisa", "Fuentealba", 1996)
print("La cantidad de personas creadas es {}".format(Persona.contador))
print("La persona {}")

alonso.isReino()