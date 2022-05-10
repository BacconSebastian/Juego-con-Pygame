from principal import *
from configuracion import *
from extras import *
from pygame import *

import random
import math

import time


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    
    ####################################################################################################
    # Elige una palabra

    palabra = lista[random.randint(0, len(lista))]
    print("palabra: ", palabra)

    ####################################################################################################

    ####################################################################################################
    # La carga dividida en las tres listas

    caracteres = int(len(palabra) / 3)

    indice = 0

    for i in range(caracteres):
        listaIzq.append(palabra[indice])
        posiciones = [random.randint(10,250), 50]
        posicionesIzq.append(posiciones)
        indice += 1
    for i in range(caracteres):
        listaMedio.append(palabra[indice])
        posiciones = [random.randint(270,510), 50]
        posicionesMedio.append(posiciones)
        indice += 1
    for i in range(caracteres):
        listaDer.append(palabra[indice])
        posiciones = [random.randint(540,790), 50]
        posicionesDer.append(posiciones)
        indice += 1

    ####################################################################################################    


def bajar(posicionesIzq, posicionesMedio, posicionesDer, lista, listaIzq, listaMedio, listaDer):

    ####################################################################################################
    # Hace bajar las letras y elimina las que estan muy abajo

    largo = len(posicionesIzq)
    for i in range(largo -1, -1, -1):
        posicion = posicionesIzq[i]
        if posicion[1] <= 460:
            posicion[1] += 40
        else:
            lista.pop(i)
            posicionesIzq.pop(i)
            listaIzq.pop(i)


    largo = len(posicionesMedio)
    for i in range(largo -1, -1, -1):
        posicion = posicionesMedio[i]
        if posicion[1] <= 460:
            posicion[1] += 40
        else:
            lista.pop(i)
            posicionesMedio.pop(i)
            listaMedio.pop(i)

    largo = len(posicionesDer)
    for i in range(largo - 1, -1, -1):
        posicion = posicionesDer[i]
        if posicion[1] <= 460:
            posicion[1] += 40
        else:
            lista.pop(i)
            posicionesDer.pop(i)
            listaDer.pop(i)

    ####################################################################################################

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):

    ####################################################################################################
    ## Llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y cargar nuevas letras a la pantalla

    bajar(posicionesIzq, posicionesMedio, posicionesDer, lista, listaIzq, listaMedio, listaDer)
    cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)    

    ####################################################################################################


def Puntos(candidata):

    ####################################################################################################
    # Devuelve el puntaje que le corresponde a candidata

    puntos = 0
    vocales = ["a", "e", "i", "o", "u"]
    dificiles = ["j", "k", "q", "w", "x", "y", "z"]

    if candidata != "":
        for i in candidata:
            if i in vocales:
                puntos += 1
            elif i in dificiles:
                puntos += 5
            else:
                puntos +=2
    
    return puntos

    ####################################################################################################


def procesar(lista, candidata, listaIzq, listaMedio, listaDer):

    ####################################################################################################
    # Chequea que candidata sea correcta en cuyo caso devuelve el puntaje y -5 si es incorrecta (Agregado) 

    if esValida(lista, candidata, listaIzq, listaMedio, listaDer):
        pygame.mixer.music.load("menu/correcto.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.2)
        puntos = Puntos(candidata)
        return puntos
    else:
        pygame.mixer.music.load("menu/incorrecto.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.2)
        return -5

    ####################################################################################################


def esValida(lista, candidata, listaIzq, listaMedio, listaDer):

    ####################################################################################################
    # Devuelve True si candidata cumple con los requisitos

    if candidata in lista:

        partes = int(len(candidata) / 3)
        revisionIzq = []
        revisionMedio = []
        revisionDer = []
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

        for i in revisionIzq:
            if i in listaIzq or i in listaMedio or i in listaDer:
                return True

    ####################################################################################################


