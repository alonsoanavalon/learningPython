import random

bolitaRoja = .60
bolitaAmarilla = .75
bolitaBlanca = 1
res = "y"

while res == "y":
    while True:
        try:
            costo = int(input("Ingrese costo de la compra"))
            break
        except ValueError:
            print("Error en el tipo de dato, ingreselo nuevamente")
    rand = random.randint(0, 2)
    if rand == 1:
        print("Ha salido la bolita roja! tiene un '40%' de descuento")
        total = costo*bolitaRoja
        print("El valor total de su compra es ${:.0f}".format(total))
    elif rand == 2:
        print("Ha salido la bolita roja! tiene un '25%' de descuento")
        total = costo*bolitaAmarilla
        print("El valor total de su compra es ${:.0f}".format(total))
    else:
        print("Ha salido la bolita blanca! Lamentablemente no tiene descuento!")
        total = costo
        print("El valor total de su compra es ${:.0f}".format(total))
    res = input("Desea ingresar otra compra? y/n ")
    res = res.lower()






