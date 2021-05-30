def validarRut ():

    #Iteración y suma
    
    res = True

    while res == True:
        rut = int(input("Ingrese su rut : "))
        digitoVerificadorObtenido = str(input("Ingrese su digito verificador : "))
        digitoVerificadorObtenido = digitoVerificadorObtenido.lower()
        multiplicador = 2
        suma = 0

        #pasando numero por numero
        while rut > 0:
            if multiplicador > 7:
                multiplicador = 2
            else:
                resto = rut % 10
                rut = int(rut / 10)
                suma += int(resto*multiplicador)
                multiplicador += 1
        resto = suma % 11

        #Obteniendo digito verificador

        if resto == 0:
            digitoVerificador = "0"
        elif resto == 1:
            digitoVerificador = "k"
            digitoVerificador = digitoVerificador.lower()
        else:
            digitoVerificador = str(abs(resto -11))


        #Comprobando si digito verificador es válido

        if digitoVerificadorObtenido == digitoVerificador:
            print("Su rut es válido")
        else:
            print("Ha ingresado un rut inválido")

        #Preguntando si desea ingresar otro rut

        res = input("Desea verificar un nuevo rut?: ")
        res = res.lower()

        # Verificando que escriba S o N

        while res != "s" and res != "n":
            print("Solo responda con S o N")
            res = input("Desea verificar un nuevo rut?: ")
            res = res.lower()

        if res == "n":
            res = False
            print("Gracias por preferir nuestro servicio, adiós!")
        else:
            res = True





validarRut()