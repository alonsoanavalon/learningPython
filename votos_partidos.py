strPartidos = "partido1$partido2$partido3$partido1$partido4"


def votos_partido(votos, partido):
    listaPartidos = list(votos)
    partidosFiltrados = list()
    partido = partido.lower()

    contadorPartido = 0
    n = listaPartidos.count("$")+1
    i = 1

    
    while i < n:
        nuevoPartido = ""
        for letra in listaPartidos:
            if letra != "$":
                nuevoPartido += letra
            else:
                partidosFiltrados.append(nuevoPartido)
                nuevoPartido = ""
                i += 1
        partidosFiltrados.append(nuevoPartido)

    for p in partidosFiltrados:
        if p == partido:
            contadorPartido +=1

    print("El partido que quieres analizar es", partido)
    print("La lista de partidos es la siguiente {}".format(partidosFiltrados))
    print("El partido '{}' se ha repetido {} veces".format(partido, contadorPartido))

votos_partido(strPartidos, "partido1")