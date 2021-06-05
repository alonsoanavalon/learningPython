res="S"
ba=0
br=0
bb=0
aa=0
ee=0
while res=="S" or res=="s":
    aa=input("Que bolita saco el cliente? Blanco=bb Roja=br amarilla=ba: ")
    ee=int(input("cuanto era el monto total a pagar (sin descuento):$"))
    pd= int()
    if aa=="bb":
        pd=100
    elif aa=="br":
        pd=60
    elif aa=="ba":
        pd=75

    descuento=int(ee*pd/100)
    print("Monto total con descuento $" ,descuento)
    res=input("Desea ingresar un cliente? (s/n): ") 