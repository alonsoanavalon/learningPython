from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

users = [{"nombre":"pepe", "numero":"9"}, {"nombre":"jose", "numero":"10"}]

@app.route('/app/users/add', methods=["POST"])
def add_user():
    if request.method == "POST":
        user_name = request.form["nombre"]
        user_num = request.form["numero"]
        users.append({
            "nombre":user_name,
            "numero":user_num
        })
        print(users)
        return jsonify(users)


#request.args.params("name", "prametropordefecto")

@app.route('/app/users/<id>', methods=["GET"])

def test_function(id):
    contador = 1
    id = int(id)
    for user in users:
        print("contador es", contador)
        print("id es", id)
        if contador == id:
            msg = ("El usuario {} es {}".format(id, user ))
            return msg
        else:
            contador +=1
    else:
        return("No se ha encontrado el usuario")
    #print(request.args.get('nombre')) <- conseguir argumento /app/users?nombre=alonso
    


app.run(debug=True)







@app.route('/app/test/<id>', methods=['GET', "POST"])



def users_action(id):


    print(request)

    
    message = False
    posicion = 1

    if request.method == "POST":

        new_user = request.form['nombre']
        users.append(new_user)
        print("Usuario agregado")
        print(users)
        return (jsonify(new_user))
    else:
        return jsonify(users)
    for user in users:
        id = int(id)
        if posicion == id:
            message = "El usuario numero {} es {}".format(id, user)
            posicion += 1
            return jsonify(users[id])
    if message == False:
        return "Su id no se ha encontrado"
    return message  