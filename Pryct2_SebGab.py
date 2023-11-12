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
import keyboard

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
    mainmenu_bg = PhotoImage(file='ProyectoPacman/mainmenu_bg.png')
    label_mainmenu = Label(r, image=mainmenu_bg)
    label_mainmenu.place(x=0, y=0, relwidth=1, relheight=1)
    # Colors
    white = '#FFFFFF'
    # Music
    pygame.mixer.init()

    class Ventanas:
        def namePantalla(self):
            # Top level
            name_pantalla_TP = tk.Toplevel()
            name_pantalla_TP.geometry('600x650')
            name_pantalla_TP.config(bg='#242424')
            name_pantalla_TP.title('PACKUMAN-NP')

            get_name = StringVar()
            entry_name = tk.Entry(name_pantalla_TP, width= 50, borderwidth=10,  textvariable = get_name).place(x=140, y=400)

            def introducir_name():
                global Name
                Name = get_name.get()
                if isinstance(Name, str):
                    #level_1
                    self.name = Name
                    print(Name)
                    ventana_instance = Ventanas()
                    ventana_instance.level_1()
                else:
                    print('Nombre no valido')

            intro_num = tk.Button(name_pantalla_TP, text='Introduzca el nombre', font='Courier', command=introducir_name, height=3, width=20)
            intro_num.place(x=200, y=325)

            # Cerrar la pantalla
            close_ventana_name = tk.Button(name_pantalla_TP, text='X', fg='red', command=name_pantalla_TP.destroy)
            close_ventana_name.place(x=1180, y=0)

        def settings(self):
            print(2)

        def aboutUs(self):
            print(3)

        def helpCenter(self):
            print(4)
        
        def highScores(self):
            print(7)

        

        def level_1(self):
            global score
            #Variables
            lives = 3
            enemies = 5
            high_score = 999999999
            comida = 618
            score = 0
            #Top level
            level1 = tk.Toplevel()
            level1.geometry('360x450')
            level1.config(bg=white)
            level1.title('PUCKMAN-lvl1')
            #Canvas de lvl1
            level1_canvas = Canvas(level1, width=360, height=400, bg= 'black')
            level1_canvas.pack()
            #Condicion para que se abra el segundo nivel 
<<<<<<< HEAD
            if comida == 10:
                ventana_instance = Ventanas(self.score, self.name)
=======
            if comida == 0:
                ventana_instance = Ventanas()
>>>>>>> e5648ac4b153554aea299bcfafad4a4cb8763fca
                ventana_instance.level_2(enemies)
            #Frame
            info_frame = tk.Frame(level1, bg=white)
            info_frame.pack() 
            #Texto 
            score_text = tk.Label(info_frame, text='Score: ' + str(score), bg=white)
            score_text.grid(row=0, column=0, padx=10)
            lives_text = tk.Label(info_frame, text='Lives: ' + str(lives), bg=white)
            lives_text.grid(row=0, column=1, padx=10) 
            enemies_text = tk.Label(info_frame, text='Enemies: ' + str(enemies), bg=white)
            enemies_text.grid(row=0, column=2, padx=10)
            scores_text = tk.Label(info_frame, text='High Score: ' + str(high_score), bg=white)
            scores_text.grid(row=0, column=3, padx=10)
            #Matriz 
            tablero =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [2, 3, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 0, 3, 2], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 3, 4, 4, 0, 4, 0, 4, 4, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 4, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 4, 4, 0, 0, 0, 0, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 0], 
                        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            #Mapa 
            def dibujar_cuadros_desde_matriz(matriz):
                for fila in range(len(matriz)):
                    for columna in range(len(matriz[0])):
                        if matriz[fila][columna] == 0:
                            # Coordenadas del cuadro en el canvas
                            x1 = columna * 10
                            y1 = fila * 10
                            x2 = x1 + 10
                            y2 = y1 + 10
                            level1_canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
<<<<<<< HEAD
=======

>>>>>>> e5648ac4b153554aea299bcfafad4a4cb8763fca
            dibujar_cuadros_desde_matriz(tablero)
            def on_key_press(event):
                key = event.keysym
                if key == "Up":
                    pacman.mover_arriba()
                elif key == "Down":
                    pacman.mover_abajo()
                elif key == "Left":
                    pacman.mover_izquierda()
                elif key == "Right":
                    pacman.mover_derecha()

                # Update positions on the canvas
                update_positions()

            def update_positions():
                # Clear the canvas
                level1_canvas.delete("all")

                # Redraw the matrix
                dibujar_cuadros_desde_matriz(tablero)

                # Draw PacMan at the new position
                x1 = pacman.get_posY() * 10
                y1 = pacman.get_posX() * 10
                x2 = x1 + 10
                y2 = y1 + 10
                level1_canvas.create_oval(x1, y1, x2, y2, fill="yellow")

                # Draw ghosts at their positions
                for ghost in enemigos:
                    x1 = ghost.get_posY() * 10
                    y1 = ghost.get_posX() * 10
                    x2 = x1 + 10
                    y2 = y1 + 10
                    level1_canvas.create_rectangle(x1, y1, x2, y2, fill="red")
            r.bind("<Key>", on_key_press)
            # Clase base para los personajes
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
                    if self.posicion_y < 36 - 1:
                        self.posicion_y += 1

                def mover_arriba(self):
                    if self.posicion_x > 0:
                        self.posicion_x -= 1

                def mover_abajo(self):
                    if self.posicion_x < 40 - 1:
                        self.posicion_x += 1

                def comer_alimento(self):
                    # Lógica para comer alimento
                    pass

                def comer_capsula(self):
                    # Lógica para comer cápsula
                    pass

            # Clase para PacMan
            class PacMan(Personaje):
                def __init__(self, estado, posicion_x, posicion_y, velocidad):
                    super().__init__(estado, posicion_x, posicion_y, velocidad)
                    self.estado = 'ser comido'

                def comer_alimento(self):
                    # Lógica específica para PacMan al comer alimento
                    pass

                def comer_capsula(self):
                    # Lógica específica para PacMan al comer cápsula
                    pass
                
                def get_posX(self):
                    return self.posicion_x
                def get_posY(self):
                    return self.posicion_y

                def get_estado(self):
                    return self.estado 
                def change_estado(self, n):
                    if n == 1:
                        self.estado = 'comer'
                    else:
                        self.estado = 'ser comido'

            # Clase para Fantasma
            class Fantasma(Personaje):
                def __init__(self, estado, posicion_x, posicion_y, color):
                    # Velocidad dependiendo del color
                    if color == 'rojo':
                        velocidad = 'rápido'
                    else:
                        velocidad = 'normal'
                    
                    super().__init__(estado, posicion_x, posicion_y, velocidad)
                    self.color = color
                def get_posX(self):
                    return self.posicion_x
                def get_posY(self):
                    return self.posicion_y
                def get_coords(self):
                    return self.posicion_x, self.posicion_y

            # Crear una instancia de PacMan y configurar su posición inicial
            pacman = PacMan(estado=True, posicion_x=5, posicion_y=5, velocidad=1)
            # Lista de enemigos (cada enemigo es una instancia de Fantasma)
            enemigos = [Fantasma(estado=True, posicion_x=10, posicion_y=15, color='rojo'),
                        Fantasma(estado=True, posicion_x=20, posicion_y=25, color='celeste'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=5, color='rosado'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=10, color='naranja'),]
            # Función para imprimir el tablero con separación horizontal
            def imprimir_matriz():
                for n in range(len(tablero)):
                    row = ""
                    for x in range(len(tablero[0])):
                        if n == pacman.posicion_y and x == pacman.posicion_x:
                            row += "6"
                        else:
                            for enemigo in enemigos:
                                if n == enemigo.posicion_y and x == enemigo.posicion_x:
                                    row += "7"
                                    break
                            else:
                                if tablero[n][x] == 0:
                                    row += "0 "
                                else:
                                    row += "4 "
                    print(row)
                print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

            #Colisiones
            def colision_D():
                global score
                pacmanCoords = pacman.get_posX() + 1, pacman.get_posY()
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            def colision_I():
                global score
                pacmanCoords = pacman.get_posX() - 1, pacman.get_posY()
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            def colision_AB():
                global score
                pacmanCoords = pacman.get_posX(), pacman.get_posY() + 1
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1
            def colision_A():
                global score
                pacmanCoords = pacman.get_posX(), pacman.get_posY() - 1
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            #Comer 
            def comer_D():
                global score
                pacmanX = pacman.get_posX() + 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX - 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX - 1][pacmanY] = 0 
            def comer_I():
                global score
                pacmanX = pacman.get_posX() - 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX + 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX + 1][pacmanY] = 0 
            def comer_AB():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() + 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY - 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY - 1] = 0 
            def comer_A():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() - 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY + 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY + 1] = 0 

            def puede_mover(x, y):
                return 0 <= x < 36 and 0 <= y < 40 and tablero[y][x] != 0 and not any(enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos)

            # Función para mover al jugador
            def mover_jugador(dx, dy):
                nuevo_x = pacman.posicion_x + dx
                nuevo_y = pacman.posicion_y + dy
                print('prueba')
                if puede_mover(nuevo_x, nuevo_y):
                    pacman.posicion_x = nuevo_x
                    pacman.posicion_y = nuevo_y
                    imprimir_matriz()
                    print('no toca pared')
                else:
                    print('toca pared')

            # Asignar las funciones de movimiento a las teclas
            def mover_derecha():
                colision_D()
                comer_D()
                mover_jugador(+1, 0)

            def mover_izquierda():
                colision_I()
                comer_I()
                mover_jugador(-1, 0)

            def mover_abajo():
                colision_AB()
                comer_AB()
                mover_jugador(0, +1)

            def mover_arriba():
                colision_A()
                comer_A()
                mover_jugador(0, -1)

            teclas = ['a', 's', 'd', 'w']

            for tecla in teclas:
                if tecla == 'd':
                    keyboard.add_hotkey(tecla, mover_derecha)
                elif tecla == 's':
                    keyboard.add_hotkey(tecla, mover_abajo)
                elif tecla == 'w':
                    keyboard.add_hotkey(tecla, mover_arriba)
                elif tecla == 'a':
                    keyboard.add_hotkey(tecla, mover_izquierda)

            # Función para mover a los enemigos
            def mover_enemigos():
                for enemigo in enemigos:
                    movimiento_x = random.choice([-1, 0, 1])
                    movimiento_y = random.choice([-1, 0, 1])

                    nuevo_x = enemigo.posicion_x + movimiento_x
                    nuevo_y = enemigo.posicion_y + movimiento_y

                    if (0 <= nuevo_x < 36 and 0 <= nuevo_y < 40 and tablero[nuevo_y][nuevo_x] != 0):
                        enemigo.posicion_x = nuevo_x
                        enemigo.posicion_y = nuevo_y
            
            mover_enemigos()
            imprimir_matriz()
            def dibujar_personajes():
                # Borrar todos los elementos en el canvas
                level1_canvas.delete("all")

<<<<<<< HEAD
                # Dibujar las paredes y otros elementos desde la matriz
                dibujar_cuadros_desde_matriz(tablero)

                # Dibujar PacMan
                pacman_coords = (pacman.posicion_x * 10, pacman.posicion_y * 10)
                level1_canvas.create_oval(pacman_coords[1], pacman_coords[0], pacman_coords[1] + 10, pacman_coords[0] + 10, fill="yellow")

                # Dibujar fantasmas
                for enemigo in enemigos:
                    enemigo_coords = (enemigo.posicion_x * 10, enemigo.posicion_y * 10)
                    level1_canvas.create_rectangle(enemigo_coords[1], enemigo_coords[0], enemigo_coords[1] + 10, enemigo_coords[0] + 10, fill="red")

                # Actualizar el canvas
                level1.update()

            def mover_personajes(event):
                # Mover PacMan
                if event.keysym == 'Up':
                    pacman.mover_arriba()
                elif event.keysym == 'Down':
                    pacman.mover_abajo()
                elif event.keysym == 'Left':
                    pacman.mover_izquierda()
                elif event.keysym == 'Right':
                    pacman.mover_derecha()
                mover_personajes(event)
                colision_D()
                colision_I()
                colision_AB()
                dibujar_personajes()
            level1.bind('<Key>', mover_personajes)

            # Enfocar el canvas para que pueda recibir eventos del teclado
            level1_canvas.focus_set()

            # Dibujar los personajes inicialmente
            dibujar_personajes()
=======
>>>>>>> e5648ac4b153554aea299bcfafad4a4cb8763fca
        def level_2(self, enemies):
            global score
            #Variables
            lives = 3
            enemies = 5
            high_score = 999999999
            comida = 618
            #Top level
            level2 = tk.Toplevel()
            level2.geometry('360x450')
            level2.config(bg=white)
            level2.title('PUCKMAN-lvl2')
            #Canvas de lvl1
            level2_canvas = Canvas(level2, width=360, height=400, bg= 'black')
            level2_canvas.pack()
            #Condicion para que se abra el segundo nivel 
            if comida == 0:
                ventana_instance = Ventanas(self.score, self.name)
                ventana_instance.level_2(enemies)
            #Frame
            info_frame = tk.Frame(level2, bg=white)
            info_frame.pack() 
            #Texto 
            score_text = tk.Label(info_frame, text='Score: ' + str(self.score), bg=white)
            score_text.grid(row=0, column=0, padx=10)
            lives_text = tk.Label(info_frame, text='Lives: ' + str(lives), bg=white)
            lives_text.grid(row=0, column=1, padx=10) 
            enemies_text = tk.Label(info_frame, text='Enemies: ' + str(enemies), bg=white)
            enemies_text.grid(row=0, column=2, padx=10)
            scores_text = tk.Label(info_frame, text='High Score: ' + str(high_score), bg=white)
            scores_text.grid(row=0, column=3, padx=10)
            #Matriz 
<<<<<<< HEAD
            tablero =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
=======
            tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
>>>>>>> e5648ac4b153554aea299bcfafad4a4cb8763fca
                        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [2, 3, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 0, 3, 2], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 3, 4, 4, 0, 4, 0, 4, 4, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 4, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 4, 4, 0, 0, 0, 0, 0, 4, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 4, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [4, 4, 4, 4, 4, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4], 
                        [0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 0], 
                        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 4, 4, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
                        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0], 
                        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            #Mapa 
            def dibujar_cuadros_desde_matriz(matriz):
                for fila in range(len(matriz)):
                    for columna in range(len(matriz[0])):
                        if matriz[fila][columna] == 0:
                            # Coordenadas del cuadro en el canvas
                            x1 = columna * 10
                            y1 = fila * 10
                            x2 = x1 + 10
                            y2 = y1 + 10
                            level2_canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            dibujar_cuadros_desde_matriz(tablero)
            # Clase base para los personajes
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
                    if self.posicion_y < 36 - 1:
                        self.posicion_y += 1

                def mover_arriba(self):
                    if self.posicion_x > 0:
                        self.posicion_x -= 1

                def mover_abajo(self):
                    if self.posicion_x < 40 - 1:
                        self.posicion_x += 1

                def comer_alimento(self):
                    # Lógica para comer alimento
                    pass

                def comer_capsula(self):
                    # Lógica para comer cápsula
                    pass

            # Clase para PacMan
            class PacMan(Personaje):
                def __init__(self, estado, posicion_x, posicion_y, velocidad):
                    super().__init__(estado, posicion_x, posicion_y, velocidad)
                    self.estado = 'ser comido'

                def comer_alimento(self):
                    # Lógica específica para PacMan al comer alimento
                    pass

                def comer_capsula(self):
                    # Lógica específica para PacMan al comer cápsula
                    pass
                
                def get_posX(self):
                    return self.posicion_x
                def get_posY(self):
                    return self.posicion_y

                def get_estado(self):
                    return self.estado 
                def change_estado(self, n):
                    if n == 1:
                        self.estado = 'comer'
                    else:
                        self.estado = 'ser comido'

            # Clase para Fantasma
            class Fantasma(Personaje):
                def __init__(self, estado, posicion_x, posicion_y, color):
                    # Velocidad dependiendo del color
                    if color == 'rojo':
                        velocidad = 'rápido'
                    else:
                        velocidad = 'normal'
                    
                    super().__init__(estado, posicion_x, posicion_y, velocidad)
                    self.color = color
                def get_posX(self):
                    return self.posicion_x
                def get_posY(self):
                    return self.posicion_y
                def get_coords(self):
                    return self.posicion_x, self.posicion_y

            # Crear una instancia de PacMan y configurar su posición inicial
            pacman = PacMan(estado=True, posicion_x=5, posicion_y=5, velocidad=1)
            # Lista de enemigos (cada enemigo es una instancia de Fantasma)
            enemigos = [Fantasma(estado=True, posicion_x=10, posicion_y=15, color='rojo'),
                        Fantasma(estado=True, posicion_x=20, posicion_y=25, color='celeste'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=5, color='rosado'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=10, color='naranja'),]
            # Función para imprimir el tablero con separación horizontal
            def imprimir_matriz():
                for n in range(len(tablero)):
                    row = ""
                    for x in range(len(tablero[0])):
                        if n == pacman.posicion_y and x == pacman.posicion_x:
                            row += "6"
                        else:
                            for enemigo in enemigos:
                                if n == enemigo.posicion_y and x == enemigo.posicion_x:
                                    row += "7"
                                    break
                            else:
                                if tablero[n][x] == 0:
                                    row += "0 "
                                else:
                                    row += "4 "
                    print(row)
                print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

            #Colisiones
            def colision_D():
                global score
                pacmanCoords = pacman.get_posX() + 1, pacman.get_posY()
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            def colision_I():
                global score
                pacmanCoords = pacman.get_posX() - 1, pacman.get_posY()
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            def colision_AB():
                global score
                pacmanCoords = pacman.get_posX(), pacman.get_posY() + 1
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1
            def colision_A():
                global score
                pacmanCoords = pacman.get_posX(), pacman.get_posY() - 1
                i = 0
                n = len(enemigos)
                while i != n:
                    if i == n:
                        break
                    if pacman.get_estado() == 'comer':
                        if pacmanCoords== enemigos[i].get_coords():
                            print('colision')
                            score += 2.5
                            score_text.config(text='Score: ' + str(score), bg='white')
                            i  += 1
                        else:
                            print('no colision')
                            i += 1
                    else:
                        if pacmanCoords == enemigos[i].get_coords():
                            print('colision')
                            lives -= 1
                            print(str(lives))
                            i += 1
                        else:
                            print('no colision')
                            i += 1

            #Comer 
            def comer_D():
                global score
                pacmanX = pacman.get_posX() + 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX - 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX - 1][pacmanY] = 0 
            def comer_I():
                global score
                pacmanX = pacman.get_posX() - 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX + 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX + 1][pacmanY] = 0 
            def comer_AB():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() + 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY - 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY - 1] = 0 
            def comer_A():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() - 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY + 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY + 1] = 0 
                
            def puede_mover(x, y):
                return 0 <= x < 36 and 0 <= y < 40 and tablero[y][x] != 0 and not any(enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos)

            # Función para mover al jugador
            def mover_jugador(dx, dy):
                nuevo_x = pacman.posicion_x + dx
                nuevo_y = pacman.posicion_y + dy
                print('prueba')
                if puede_mover(nuevo_x, nuevo_y):
                    pacman.posicion_x = nuevo_x
                    pacman.posicion_y = nuevo_y
                    imprimir_matriz()
                    print('no toca pared')
                else:
                    print('toca pared')

            # Asignar las funciones de movimiento a las teclas
            def mover_derecha():
                colision_D()
                comer_D()
                mover_jugador(+1, 0)

            def mover_izquierda():
                colision_I()
                comer_I()
                mover_jugador(-1, 0)

            def mover_abajo():
                colision_AB()
                comer_AB()
                mover_jugador(0, +1)

            def mover_arriba():
                colision_A()
                comer_A()
                mover_jugador(0, -1)

            teclas = ['a', 's', 'd', 'w']

            for tecla in teclas:
                if tecla == 'd':
                    keyboard.add_hotkey(tecla, mover_derecha)
                elif tecla == 's':
                    keyboard.add_hotkey(tecla, mover_abajo)
                elif tecla == 'w':
                    keyboard.add_hotkey(tecla, mover_arriba)
                elif tecla == 'a':
                    keyboard.add_hotkey(tecla, mover_izquierda)

            # Función para mover a los enemigos
            def mover_enemigos():
                for enemigo in enemigos:
                    movimiento_x = random.choice([-1, 0, 1])
                    movimiento_y = random.choice([-1, 0, 1])

                    nuevo_x = enemigo.posicion_x + movimiento_x
                    nuevo_y = enemigo.posicion_y + movimiento_y

                    if (0 <= nuevo_x < 36 and 0 <= nuevo_y < 40 and tablero[nuevo_y][nuevo_x] != 0):
                        enemigo.posicion_x = nuevo_x
                        enemigo.posicion_y = nuevo_y
            mover_enemigos()
            imprimir_matriz()

    #Instancias de las clases 
    def namePantalla():
        ventana_instance = Ventanas()
        ventana_instance.namePantalla()
    def highScores():
        ventana_instance = Ventanas()
        ventana_instance.highScores()
    def settings():
        ventana_instance = Ventanas()
        ventana_instance.settings()
    def aboutUs():
        ventana_instance = Ventanas()
        ventana_instance.aboutUs()
    def helpCenter():
        ventana_instance = Ventanas()
        ventana_instance.helpCenter()

    #Botones
    play_button = Button(r, text='PLAY', font='Courier 13', command=namePantalla)
    play_button.config(width=13, height=3)
    score_button = Button(r, text='High scores', font='Courier', command=highScores)
    config_button = Button(r, text='Settings', font='Courier', command=settings)
    info_button = Button(r, text='About us', font='Courier', command=aboutUs)
    help_button = Button(r, text='Help', command=helpCenter)
    play_window = mainmenu_canvas.create_window(600, 360, anchor="center", window=play_button)
    score_window = mainmenu_canvas.create_window(600, 510, anchor="n", window=score_button)
    config_window = mainmenu_canvas.create_window(600, 550, anchor="n", window=config_button)
    info_window = mainmenu_canvas.create_window(600, 590, anchor="n", window=info_button)
    help_window = mainmenu_canvas.create_window(1150, 600, anchor="n", window=help_button)
    
    r.mainloop()
ven0()