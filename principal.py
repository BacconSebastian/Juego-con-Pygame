#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


############################################################################################################

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada, COLOR_DIFICULTAD):
        self.imagen_normal = fuente.render(titulo, 1, (0,0,0,))
        self.imagen_destacada = fuente.render(titulo, 1, (0,0,0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 500
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('menu/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

class Menu:
    "Representa un menu con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('menu/dejavu.ttf', 40)
        color = pygame.color
        x = 400
        y = 290
        paridad = 1

        self.cursor = Cursor(x - 60, y, 60)

        COLOR_DIFICULTAD = (0,0,0)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion, COLOR_DIFICULTAD))
            y += 60
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funciÃƒÆ’Ã‚Â³n asociada a la opciÃƒÆ’Ã‚Â³n.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor estÃƒÆ’Ã‚Â© entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opciÃƒÆ’Ã‚Â³n del menÃƒÆ’Ã‚Âº."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

variable_dificultad = 1

def menu_dificultades():
    dificultades()

def dificultad_facil():
    main(variable_dificultad)

def dificultad_media():
    variable_dificultad = 1.5
    main(variable_dificultad)

def dificultad_dificil():
    variable_dificultad = 2
    main(variable_dificultad)

def salir_del_programa():
    import sys
    sys.exit(0)

opciones = [("Jugar", menu_dificultades),
    ("Salir", salir_del_programa)]

############################################################################################################


############################################################################################################

def main(variable_dificultad):

    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    #Preparar la ventana
    pygame.display.set_caption("Armar palabras...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    # Apagamos la musica del menu
    pygame.mixer.music.stop()

    puntos = 0
    candidata = ""
    listaIzq = []
    listaMedio = []
    listaDer = []
    posicionesIzq = []
    posicionesMedio = []
    posicionesDer = []
    lista = []

    archivo= open("C:/Users/Sebastián/OneDrive/Escritorio/Nuevo Pygame/lemario.txt","r")
    for linea in archivo.readlines():
        lista.append(linea[0:-1])

    cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
    dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, puntos,segundos)

    while segundos > fps/1000:
    # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if segundos > 30:
        	fps = variable_dificultad
        else:
            fps = variable_dificultad * 1.5
        
        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata)-1]
                if e.key == K_RETURN:
                    puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer)
                    candidata = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        #Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        #Dibujar de nuevo todo
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer, puntos, segundos)

        pygame.display.flip()

        actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq, posicionesMedio, posicionesDer)

    if segundos < fps/1000:
        menu_principal([("Salir", salir_del_programa)])

    while 1:
        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

############################################################################################################    

def menu_principal(opciones):

    salir = False

    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fondo = pygame.image.load("menu/fondo.png").convert()
    menu = Menu(opciones)

    pygame.init()
    pygame.mixer.music.load("menu/musica.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.2)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

def dificultades():

    salir = False

    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fondo = pygame.image.load("menu/fondo.png").convert()
    menu = Menu([("Facil", dificultad_facil),
    ("Normal", dificultad_media),
    ("Dificil", dificultad_dificil),
    ("Salir", salir_del_programa)])

    pygame.init()
    pygame.mixer.music.load("menu/musica.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.2)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)



##Programa Principal ejecuta Main
if __name__ == "__main__":
    menu_principal(opciones)