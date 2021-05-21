""" import pyodbc

conn = pyodbc.connect(
    'DRIVER={Devart ODBC Driver for MySQL}'
    'SERVER=bm6txo0rvfqjhjms2saz-mysql.services.clever-cloud.com;'
    'Database=bm6txo0rvfqjhjms2saz;'
    'UID=uizehxs1nnvfjiax;'
    'PWD=AoV6wing5Q56N0igxFoY'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM productos")

for row in cursor:
    print(row) """

""" class Persona:
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
        print("Hola soy {} y pertenezco al reino {}".format(self.nombre, Persona.reino)) """
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="bm6txo0rvfqjhjms2saz-mysql.services.clever-cloud.com",
            user="uizehxs1nnvfjiax",
            password="AoV6wing5Q56N0igxFoY",
            db="bm6txo0rvfqjhjms2saz"
        )
        self.cursor = self.connection.cursor()
    
    def select_user(self, id):
        sql = "SELECT * FROM users WHERE id_user = {}".format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print("id:", user[0])
            print("name:", user[1])
            print("surname:", user[2])
        except ValueError: 
            print("Error")

    def select_all_users(self):
        sql = "SELECT * FROM users"

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("id:", user[0])
                print("name:", user[1])
                print("surname:", user[2])
                print("\n")
                
        except ValueError:
            print("Error")

    def insert_user(self, name, surname):
        sql = "INSERT INTO users (nombre, apellido) VALUES ('{}', '{}')".format(name, surname)

        try:
            self.cursor.execute(sql)
        except ValueError:
            print("error")
    
    def update_user(self, id, username):
        sql = "UPDATE users SET nombre = '{}' WHERE id_user = {}".format(username, id)
        
        try:
            self.cursor.execute(sql)
        except ValueError:
            print("error")



database = DataBase ()
""" database.insert_user("Pedro", "Pascal") """
database.update_user(1, "alfonso")
""" database.select_user(2) """
database.select_all_users()