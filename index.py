from datetime import datetime

class Animal:

    contador = 0;
    esInerte = False;

    def __init__(self, name, year, fav_food):
        self.name = name
        self.year = int(year)
        self.fav_food = fav_food
        Animal.contador += 1

    def saludar (self, name):
        print("Hola {} soy {}".format(name.lower(), self.name))

    def edad (self):
        return datetime.today().year - self.year
    

snoopy = Animal('Snoopy', '2020', 'Croquetas')

snoopy.saludar('Alonso')
pelusa = Animal("Pelisa", "2019", "Pollo")

edadSnoopy = snoopy.edad()
print(edadSnoopy)

print(Animal.contador)
print(Animal.esInerte)

