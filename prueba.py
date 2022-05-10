import math, random, time

from principal import *

####################################################################
# Abrir lemario y pasar datos a lista

""" lista = []
lemario = open("/Users/Sebastián/OneDrive/Escritorio/Py Game/lemario.txt", "r")
for i in lemario:
    i = i[0:-1]
    lista.append(i)
lemario.close()

####################################################################


####################################################################
# Elegir palabra random
    
palabra = lista[random.randint(0, len(lista))]
print("palabra: ", palabra)

####################################################################


####################################################################
# Dividir la palabra en las tres columnas

listaIzq = []
listaMedio = []
listaDer = []

if len(palabra) % 3 == 0:
    partes = len(palabra) / 3
    i = 0
    while len(listaIzq) < partes:
        listaIzq.append(palabra[i])
        i += 1
    while len(listaMedio) < partes:
        listaMedio.append(palabra[i])
        i += 1
    while len(listaDer) < partes:
        listaDer.append(palabra[i])
        i += 1

else:
    partes = int(len(palabra) / 3)

    i = 0
    while len(listaIzq) < partes:
        listaIzq.append(palabra[i])
        i += 1
    while len(listaMedio) < partes:
        listaMedio.append(palabra[i])
        i += 1
    for i in range (i, len(palabra)):
        listaDer.append(palabra[i])


print("lista izq: ", listaIzq, "|| lista medio: ", listaMedio, "|| lista der: ", listaDer)

####################################################################


####################################################################
# Elegir las posiciones de las letras

posicionesIzq = []
posicionesMedio = []
posicionesDer = []

for i in listaIzq:
    posiciones = [random.randint(8,258), random.randint(40,60)]
    posicionesIzq.append(posiciones)

for i in listaMedio:
    posiciones = [random.randint(274,532), random.randint(40,60)]
    posicionesMedio.append(posiciones)

for i in listaDer:
    posiciones = [random.randint(548,792), random.randint(40,60)]
    posicionesDer.append(posiciones)

print("posicionesIzq: ", posicionesIzq, "|| posicionesMedio:", posicionesMedio, "|| posicionesDer:", posicionesDer)

####################################################################


####################################################################
# Bajar las letras cada x tiempo

def bajar_prueba(posicionesIzq, posicionesMedio, posicionesDer):
    # hace bajar las letras y elimina las que tocan el piso
    for coordenadas in posicionesIzq:
        for i in range(len(coordenadas)):
            if i % 2 == 0:
                pass
            else:
                coordenadas[i] += random.randint(50,75)

    for coordenadas in posicionesMedio:
        for i in range(len(coordenadas)):
            if i % 2 == 0:
                pass
            else:
                coordenadas[i] += random.randint(50,75)

    for coordenadas in posicionesDer:
        for i in range(len(coordenadas)):
            if i % 2 == 0:
                pass
            else:
                coordenadas[i] += random.randint(50,75)

bajar_prueba(posicionesIzq, posicionesMedio, posicionesDer)
print("(BAJADAS) posicionesIzq: ", posicionesIzq, "|| posicionesMedio: ", posicionesMedio, "|| posicionesDer: ", posicionesDer)

####################################################################


####################################################################
# Eliminar las letras que tocan el piso

for coordenadas in posicionesIzq:
    for i in range (len(coordenadas)):
        if not i % 2 == 0:
            if coordenadas[i] > 200:
                coordenadas[i - 1] == -10

####################################################################



####################################################################
# Validar la candidata y devolver puntos

puntos = 0
candidata = "abcdef"
lista = ["abcdef", "chau"]
listaIzq = ["a", "b"]
listaMedio = ["c", "d"]
listaDer = ["e", "f"]


def valida_prueba(lista, candidata, listaIzq, listaMedio, listaDer):
    if candidata in lista:

        revisionIzq = []
        revisionMedio = []
        revisionDer = []

        if len(candidata) % 3 == 0:
            partes = len(candidata) / 3
            i = 0

            while len(revisionIzq) < partes:
                revisionIzq.append(candidata[i])
                i += 1
            while len(revisionMedio) < partes:
                revisionMedio.append(candidata[i])
                i += 1
            while len(revisionDer) < partes:
                revisionDer.append(candidata[i])
                i += 1

        else:
            partes = int(len(candidata) / 3)
            i = 0

            while len(revisionIzq) < partes:
                revisionIzq.append(candidata[i])
                i += 1
            while len(revisionMedio) < partes:
                revisionMedio.append(candidata[i])
                i += 1
            for i in range (i, len(candidata)):
                revisionDer.append(candidata[i])

        if revisionIzq == listaIzq and revisionMedio == listaMedio and revisionDer == listaDer:
            return True
        else:
            return False

if valida_prueba(lista, candidata, listaIzq, listaMedio, listaDer):
    print(Puntos(candidata))
else:
    print(Puntos("")) """
    
####################################################################
        