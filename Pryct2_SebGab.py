#Sebastian Delgado y Gabriel Arias
#Proyecto #2 de inroduccion a la programacion

#Importar todas las librerias necesarias
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import random 
import pygame 
import time 

#Definir la pantalla del juego 
def ven0():
    r = Tk()
    # Main menu
    r.title('Puckman')
    r.geometry('1200x675')
    # Main menu canvas
    mainmenu_canvas = Canvas(r, width=1200, height=675)
    mainmenu_canvas.pack(fill='both', expand=True)
    # Main menu background
    mainmenu_bg = PhotoImage(file='mainmenu_bg.png')
    label_mainmenu = Label(r, image=mainmenu_bg)
    label_mainmenu.place(x=0, y=0, relwidth=1, relheight=1)
    # Colors
    white = '#FFFFFF'
    # Music
    pygame.mixer.init()

    # Tamaño del tablero
    filas = 40
    columnas = 36

    # Crear el tablero inicial
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Establecer los valores iniciales en el tablero
    # 0: representa una pared
    # 1: alimento (punto)
    # 2: cápsula (permite que PacMan se coma los fantasmas por un tiempo determinado)
    # 3: alimento comida

    # Aquí puedes definir la disposición inicial de las paredes y alimentos
    # Por ejemplo:
    # Paredes exteriores
    for i in range(filas):
        for j in range(columnas):
            if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                tablero[i][j] = 0  # Pared exterior

    # Puedes agregar más elementos al tablero según lo necesites
    tablero[5][5] = 1  # Alimento
    tablero[10][10] = 2  # Cápsula
    tablero[15][15] = 3  # Alimento especial

    # Imprimir el tablero inicial
    for fila in tablero:
        print(' '.join(map(str, fila)))
        
    

    # Crear instancias de PacMan y Fantasma
    pacman = PacMan(estado=True, posicion_x=2, posicion_y=2, velocidad=1)
    fantasma_rojo = Fantasma(estado=True, posicion_x=20, posicion_y=20, color='rojo')    

    #Funciones 
    def name_pantalla():
        #Colores 
        n_grey = '#242424'
        # Top level
        name_pantalla_TP = tk.Toplevel()
        name_pantalla_TP.geometry('600x650')
        name_pantalla_TP.config(bg='#242424')
        name_pantalla_TP.title('ROBOTS-lvl1')

        # Recuperar nombre
        get_name = tk.StringVar()
        entry_name = tk.Entry(name_pantalla_TP, width=50, borderwidth=10, textvariable=get_name)
        entry_name.place(x=150, y=275)

        def introducir_name():
            global Name
            Name = get_name.get()
            if isinstance(Name, str):
                level_1()
                print(Name)
            else:
                print('Nombre no valido')

        intro_num = tk.Button(name_pantalla_TP, text='Introduzca el nombre', font='Courier', command=introducir_name, height=3, width=20)
        intro_num.place(x=200, y=325)

        # Cerrar la pantalla
        close_ventana_name = tk.Button(name_pantalla_TP, text='X', fg='red', command=name_pantalla_TP.destroy)
        close_ventana_name.place(x=1180, y=0)

    #Definir clases de enemigos
    class Fantasma(Personaje):
        def __init__(self, estado, posicion_x, posicion_y, color):
            # Velocidad dependiendo del color
            if color == 'rojo':
                    velocidad = 'rápido'
            else:
                velocidad = 'normal'
                
            super().__init__(estado, posicion_x, posicion_y, velocidad)


    class Personaje:
            def __init__(self, estado, posicion_x, posicion_y, velocidad):
                self.estado = estado
                self.posicion_x = posicion_x
                self.posicion_y = posicion_y
                self.velocidad = velocidad

            def mover_izquierda(self):
                if self.posicion_y > 0:
                    self.posicion_y -= 1

            def mover_derecha(self):
                if self.posicion_y < columnas - 1:
                    self.posicion_y += 1

            def mover_arriba(self):
                if self.posicion_x > 0:
                    self.posicion_x -= 1

            def mover_abajo(self):
                if self.posicion_x < filas - 1:
                    self.posicion_x += 1

            def comer_alimento(self):
                # Lógica para comer alimento
                pass

            def comer_capsula(self):
                # Lógica para comer cápsula
                pass

    class PacMan(Personaje):
            def __init__(self, estado, posicion_x, posicion_y, velocidad):
                super().__init__(estado, posicion_x, posicion_y, velocidad)

            def comer_alimento(self):
                # Lógica específica para PacMan al comer alimento
                pass

            def comer_capsula(self):
                # Lógica específica para PacMan al comer cápsula
                pass

    def level_1():
        print('abriendo level 1')
        
        # Crear instancias de PacMan y Fantasma
        pacman = PacMan(estado=True, posicion_x=2, posicion_y=2, velocidad=1)
        fantasma_rojo = Fantasma(estado=True, posicion_x=20, posicion_y=20, color='rojo')  
    
    def high_scores():
        print(2)
    
    def settings():
        print(3)

    def help_center():
        print(4)
    
    def about_us():
        print(5)

    #Botones
    play_button = Button(r, text='PLAY', font='Courier 14', command=name_pantalla)
    play_button.config(width=14, height=3)
    score_button = Button(r, text='High scores', font='Courier', command=high_scores)
    config_button = Button(r, text='Settings', font='Courier', command=settings)
    info_button = Button(r, text='About us', font='Courier', command=about_us)
    help_button = Button(r, text='Help', command=help_center)
    play_window = mainmenu_canvas.create_window(600, 460, anchor="center", window=play_button)
    score_window = mainmenu_canvas.create_window(600, 510, anchor="n", window=score_button)
    config_window = mainmenu_canvas.create_window(600, 550, anchor="n", window=config_button)
    info_window = mainmenu_canvas.create_window(600, 590, anchor="n", window=info_button)
    help_window = mainmenu_canvas.create_window(1150, 600, anchor="n", window=help_button)

    r.mainloop()
ven0()