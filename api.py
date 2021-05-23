from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

users = ["Alonso","Melisa","Pepe","Juanito","Alejandro","Paloma","Gervasio","Xing", "Akram", "Beltuz", "Kinao", "Ahuej"]

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



app.run(debug=True)