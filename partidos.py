
strPartidos = "partido1$partido2$partido3$partido1$partido4"

listaPartidos = list(strPartidos)
partidosFiltrados = list()
n = listaPartidos.count("$")+1
print(n)
print(listaPartidos)
i = 1;

while i < n:
    partido = ""
    for letra in listaPartidos:
        if letra != "$":
            partido += letra
        else:
            partidosFiltrados.append(partido)
            partido = ""
            i += 1
    partidosFiltrados.append(partido)


print("Array de partidos")
print(partidosFiltrados)
contadorPartido = 0
for partido in partidosFiltrados:
    if partido == "partido1":
        contadorPartido +=1
print(contadorPartido)


    
    