cadena = "[#]*hola$[!]*chao$"
i = 6
longitudCadena = len(cadena)
emoji = ""

while i < longitudCadena:
    caracter = cadena[i:i+1]
    if caracter == "*":
        print(emoji)
        i += 1
        significado = ""
        caracter = cadena[i:i+1]
        while caracter != "$":
            significado += cadena[i:i+1]
            i+=1
            caracter = cadena[i:i+1]
        print("significado", significado)
        emoji = ""
    else:
        emoji += caracter
    i += 1



        


