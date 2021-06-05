bolitaRoja = 60
bolitaAmarilla = 75

res = "y"

while res == "y" or res == "Y":
    #Parta del precio
    totalCompra = int(input("Ingrese el total (sin descuento)"))
    #Parte de la bolita
    bolita = input("Ingrese la bolita que sacó el cliente (roja, amarilla o blanca)")
    while bolita != "roja" and bolita != "Roja" and bolita != "amarilla" and bolita != "Amarilla" and bolita != "blanca" and bolita != "Blanca":
        print("Ingrese una bolita válida")
        bolita = input("Ingrese la bolita que sacó el cliente (roja, amarilla o blanca)")
    if bolita == "Roja" or bolita == "roja":
        totalDescuento = int(totalCompra * bolitaRoja / 100)
    elif bolita == "Amarilla" or bolita == "amarilla":
        totalDescuento = int(totalCompra * bolitaAmarilla / 100)
    else:
        totalDescuento = totalCompra
    print("El total de su compra es", totalDescuento)
    res = input("Desea ingresar otra compra? y/n")
    
