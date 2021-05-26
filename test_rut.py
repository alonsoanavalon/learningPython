num = int(input("Su rut  "))
digitoVerificadorObtenido = str(input("Ingrese su digito verificador  "))
suma = 0
multiplicador = 2

while num > 0:
    if multiplicador > 7:
        multiplicador = 2
    else:
        resto = num%10
        print(resto)
        num = int(num/10)
        suma += int(resto * multiplicador)  
        print("{} * {}". format(resto, multiplicador))
        multiplicador += 1
resto = suma % 11
print(resto)

     #Obteniendo digito verificador

if resto == 0:
    digitoVerificador = "0"
elif resto == 1:
    digitoVerificador = "k"
    digitoVerificador = digitoVerificador.lower()
else:
    digitoVerificador = str(abs(resto -11))

print(digitoVerificador)

if digitoVerificadorObtenido == digitoVerificador:
    print("Su rut es válido")
else:
    print("Ha ingresado un rut inválido")