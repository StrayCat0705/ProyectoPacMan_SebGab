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
import os

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

    class Ventanas:
        def game_over():
            #TopLevel
            gameOver = tk.Toplevel()
            gameOver.geometry('1200x800')
            gameOver.config(bg='red')
            gameOver.title('ROBOTS-Gameover')
            #Canvas de lvl1
            gameover_canvas = Canvas(gameOver, width=1200, height=800, bg='red')
            gameover_canvas.pack()
            #Texto
            gameover_canvas.create_text(600, 400, text='GAME OVER', font='Verdana 85', fill='black')

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

        def aboutUs(self):
            #Top level
            about_us = tk.Toplevel()
            about_us.geometry('1200x700')
            about_us.config(bg='#242424')
            about_us.title('About Us')
            #Texto
            name1_label = Label(about_us, text = 'Nombre: Sebastian Delgado Brenes' , font = 'Terminal')
            name1_label.place(x = 150, y = 300)
            num1_label = Label(about_us, text = '2023086378', font = 'Terminal')
            num1_label.place(x = 150, y = 350)
            name2_label = Label(about_us, text = 'Nombre: Gabriel Arias Lara' , font = 'Terminal')
            name2_label.place(x = 650, y = 300)
            num2_label = Label(about_us, text = '2023086378', font = 'Terminal')
            num2_label.place(x = 650, y = 350)
            carrera_label = Label(about_us, text = 'Ingenieria en computadores', font = 'Terminal')
            carrera_label.place(x = 450, y = 400)
            curso_label = Label(about_us, text = 'Introduccion a la programación', font = 'Terminal')
            curso_label.place(x = 420, y = 450)
            ano_label = Label(about_us, text = '2023', font = 'Terminal')
            ano_label.place(x = 570, y = 500)
            prof_label = Label(about_us, text = 'Profesor Jeff Schmidt', font = 'Terminal')
            prof_label.place(x = 460, y = 550)
            pais_label = Label(about_us, text = 'Costa Rica', font = 'Terminal')
            pais_label.place(x = 530, y = 600)
            pais_label = Label(about_us, text = 'ver.1.0', font = 'Terminal')
            pais_label.place(x = 550, y = 650)
            #Imagenes 
            image_path = os.path.abspath('Sebas.png')
            sebas = PhotoImage(file=image_path)
            label_bg1 = Label(about_us, image=sebas)
            label_bg1.place(x=300, y=50)
            image_path = os.path.abspath('Ali.png')
            ali = PhotoImage(file=image_path)
            label_bg1 = Label(about_us, image=ali)
            label_bg1.place(x=720, y=25)
            about_us.update()

            about_us.mainloop()

        def helpCenter(self):
            #Top level
            help_center = tk.Toplevel()
            help_center.geometry('1200x700')
            help_center.config(bg='#242424')
            help_center.title('About Us')
            #texto
            historia_label = Label(help_center, text = 
            '''PacMan es un videojuego arcade creado por el diseñador de videojuegos Toru Iwatani de
            la empresa Namco, y distribuido por Midway Games al mercado estadounidense a
            principios de los años 1980.''' , font = 'Terminal')
            historia_label.place(x = 50, y = 500)
            controles_label = Label(help_center, text = 
            '''Utiliza WASD para navegar!''' , font = 'Terminal')
            controles_label.place(x = 450, y = 300)
            #Imagenes
            image_path = os.path.abspath('WASD.png')
            wasd = PhotoImage(file=image_path)
            label_bg1 = Label(help_center, image=wasd)
            label_bg1.place(x=500, y=50)

            help_center.mainloop()
        
        def highScores(self):
            salon_fama = tk.Toplevel(r)
            salon_fama.geometry('1200x675')
            salon_fama.title('Pantalla_name')

            file = open('database_scores.txt', 'r')
            read = file.readlines()
            
            read.sort(reverse = True)
            score1 = read[0]
            score2 = read[1]
            score3 = read[2]
            score4 = read[3]
            score5 = read[4]
            score6 = read[5]
            score7 = read[6]

            score1_label = Label(salon_fama, text = "1." + str(score1), font = 'Terminal')
            score1_label.place(x = 530, y = 250)
            score2_label = Label(salon_fama, text = "2." + str(score2), font = 'Terminal')
            score2_label.place(x = 530, y = 300)
            score3_label = Label(salon_fama, text = "3." + str(score3), font = 'Terminal')
            score3_label.place(x = 530, y = 350)
            score1_label = Label(salon_fama, text = "4." + str(score4), font = 'Terminal')
            score1_label.place(x = 530, y = 400)
            score2_label = Label(salon_fama, text = "5." + str(score5), font = 'Terminal')
            score2_label.place(x = 530, y = 450)
            score3_label = Label(salon_fama, text = "6." + str(score6), font = 'Terminal')
            score3_label.place(x = 530, y = 500)
            score3_label = Label(salon_fama, text = "7." + str(score7), font = 'Terminal')
            score3_label.place(x = 530, y = 550)

            Title_label = Label(salon_fama, text = "Estos son los 7 mejores puntajes:", font = 'Terminal 25', fg = '#0E52C9', height= 2)
            Title_label.place(x = 210, y = 70)        

            close_pantalla_puntajes = Button(salon_fama, text='X', fg='red', command=salon_fama.destroy).place(x =1180, y =0)

        def level_1(self):
            global score, Name
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
            if comida == 0:
                ventana_instance = Ventanas()
                ventana_instance.level_2(enemies)
            #Condicion de game over 
            if lives == 0:
                ventana_instance = Ventanas()
                ventana_instance.game_over()
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
                        [0, 3, 0, 4, 4, 0, 3, 0, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 3, 0, 4, 4, 4, 0, 3, 0], 
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
            pacman = PacMan(estado=True, posicion_x=18, posicion_y=28, velocidad=1)
            user_u = Image.open('pacman.png')
            user_i = ImageTk.PhotoImage(user_u)
            
            user = level1_canvas.create_image(175, 275, image=user_i, anchor='center')
            
            # Movimiento de pacman
            def moverDerecha(n):
                level1_canvas.move(user, n, 0)

            def moverIzquierda(n):
                level1_canvas.move(user, -n, 0)

            def moverArriba(n):
                level1_canvas.move(user, 0, -n)

            def moverAbajo(n):
                level1_canvas.move(user, 0, n)

            # Lista de enemigos (cada enemigo es una instancia de Fantasma)
            enemigos = [Fantasma(estado=True, posicion_x=10, posicion_y=15, color='rojo'),
                        Fantasma(estado=True, posicion_x=20, posicion_y=25, color='celeste'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=5, color='rosado'),
                        Fantasma(estado=True, posicion_x=30, posicion_y=10, color='naranja'),]
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
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX - 1][pacmanY] = 3 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX - 1][pacmanY] =  4
            def comer_I():
                global score
                pacmanX = pacman.get_posX() - 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX + 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX + 1][pacmanY] = 4 
            def comer_AB():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() + 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY - 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY - 1] = 4
            def comer_A():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() - 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY + 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY + 1] = 0 

            def puede_mover(x, y):
                return 0 <= x < len(tablero[0]) and 0 <= y < len(tablero) and tablero[y][x] != 0 and not any(enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos)


            # Función para mover al jugador
            def mover_jugador(dx, dy):
                nuevo_x = pacman.posicion_x + dx
                nuevo_y = pacman.posicion_y + dy
                print('prueba')
                if puede_mover(nuevo_x, nuevo_y):
                    pacman.posicion_x = nuevo_x
                    pacman.posicion_y = nuevo_y
                    print('no toca pared')
                else:
                    print('toca pared')

            # Asignar las funciones de movimiento a las teclas

            def mover_derecha():
                lista = [[5, 5], [5, 15], [5, 25], [5, 35], [5, 45], [5, 55], [5, 65], [5, 75], [5, 85], [5, 95], [5, 105], [5, 115], [5, 125], [5, 135], [5, 145], [5, 155], [5, 165], [5, 175], [5, 185], [5, 195], [5, 205], [5, 215], [5, 225], [5, 235], [5, 245], [5, 255], [5, 265], [5, 275], [5, 285], [5, 295], [5, 305], [5, 315], [5, 325], [5, 335], [5, 345], [5, 355], [15, 5], [15, 355], [25, 5], [25, 25], [25, 35], [25, 45], [25, 55], [25, 75], [25, 85], [25, 95], [25, 115], [25, 125], [25, 135], [25, 145], [25, 155], [25, 165], [25, 185], [25, 195], [25, 205], [25, 215], [25, 225], [25, 235], [25, 255], [25, 265], [25, 275], [25, 295], [25, 305], [25, 315], [25, 325], [25, 335], [25, 355], [35, 5], [35, 25], [35, 55], [35, 75], [35, 95], [35, 115], [35, 165], [35, 185], [35, 235], [35, 255], [35, 275], [35, 295], [35, 335], [35, 355], [45, 5], [45, 25], [45, 35], [45, 45], [45, 55], [45, 75], [45, 95], [45, 115], [45, 165], [45, 185], [45, 235], [45, 255], [45, 275], [45, 295], [45, 305], [45, 315], [45, 325], [45, 335], [45, 355], [55, 5], [55, 75], [55, 95], [55, 115], [55, 125], [55, 135], [55, 145], [55, 155], [55, 165], [55, 185], [55, 195], [55, 205], [55, 215], [55, 225], [55, 235], [55, 255], [55, 275], [55, 355], [65, 5], [65, 25], [65, 35], [65, 45], [65, 55], [65, 75], [65, 95], [65, 255], [65, 275], [65, 295], [65, 305], [65, 315], [65, 325], [65, 335], [65, 355], [75, 5], [75, 25], [75, 55], [75, 75], [75, 95], [75, 115], [75, 125], [75, 135], [75, 145], [75, 155], [75, 165], [75, 175], [75, 185], [75, 195], [75, 205], [75, 215], [75, 225], [75, 235], [75, 255], [75, 275], [75, 295], [75, 335], [75, 355], [85, 5], [85, 25], [85, 35], [85, 45], [85, 55], [85, 75], [85, 95], [85, 115], [85, 235], [85, 255], [85, 275], [85, 295], [85, 305], [85, 315], [85, 325], [85, 335], [85, 355], [95, 5], [95, 75], [95, 85], [95, 95], [95, 115], [95, 235], [95, 255], [95, 265], [95, 275], [95, 355], [105, 5], [105, 25], [105, 35], [105, 45], [105, 55], [105, 115], [105, 125], [105, 135], [105, 145], [105, 155], [105, 165], [105, 185], [105, 195], [105, 205], [105, 215], [105, 225], [105, 235], [105, 295], [105, 305], [105, 315], [105, 325], [105, 335], [105, 355], [115, 5], [115, 25], [115, 35], [115, 45], [115, 55], [115, 75], [115, 85], [115, 95], [115, 165], [115, 185], [115, 255], [115, 265], [115, 275], [115, 295], [115, 305], [115, 315], [115, 325], [115, 335], [115, 355], [125, 5], [125, 75], [125, 95], [125, 105], [125, 115], [125, 125], [125, 135], [125, 165], [125, 185], [125, 215], [125, 225], [125, 235], [125, 245], [125, 255], [125, 275], [125, 355], [135, 5], [135, 15], [135, 25], [135, 35], [135, 45], [135, 55], [135, 75], [135, 95], [135, 105], [135, 115], [135, 125], [135, 135], [135, 165], [135, 175], [135, 185], [135, 215], [135, 225], [135, 235], [135, 245], [135, 255], [135, 275], [135, 295], [135, 305], [135, 315], [135, 325], [135, 335], [135, 345], [135, 355], [145, 55], [145, 75], [145, 95], [145, 255], [145, 275], [145, 295], [155, 55], [155, 75], [155, 95], [155, 255], [155, 275], [155, 295], [165, 5], [165, 15], [165, 25], [165, 35], [165, 45], [165, 55], [165, 75], [165, 85], [165, 95], [165, 115], [165, 125], [165, 135], [165, 145], [165, 155], [165, 195], [165, 205], [165, 215], [165, 225], [165, 235], [165, 255], [165, 265], [165, 275], [165, 295], [165, 305], [165, 315], [165, 325], [165, 335], [165, 345], [165, 355], [175, 115], [175, 235], [185, 115], [185, 235], [195, 75], [195, 85], [195, 95], [195, 115], [195, 235], [195, 255], [195, 265], [195, 275], [205, 75], [205, 95], [205, 115], [205, 235], [205, 255], [205, 275], [215, 75], [215, 95], [215, 115], [215, 235], [215, 255], [215, 275], [225, 5], [225, 15], [225, 25], [225, 35], [225, 45], [225, 55], [225, 75], [225, 95], [225, 115], [225, 235], [225, 255], [225, 275], [225, 295], [225, 305], [225, 315], [225, 325], [225, 335], [225, 345], [225, 355], [235, 55], [235, 75], [235, 95], [235, 115], [235, 235], [235, 255], [235, 275], [235, 295], [245, 55], [245, 75], [245, 95], [245, 115], [245, 235], [245, 255], [245, 275], [245, 295], [255, 5], [255, 15], [255, 25], [255, 35], [255, 45], [255, 55], [255, 75], [255, 95], [255, 115], [255, 235], [255, 255], [255, 275], [255, 295], [255, 305], [255, 315], [255, 325], [255, 335], [255, 345], [255, 355], [265, 5], [265, 75], [265, 85], [265, 95], [265, 115], [265, 125], [265, 135], [265, 145], [265, 155], [265, 165], [265, 175], [265, 185], [265, 195], [265, 205], [265, 215], [265, 225], [265, 235], [265, 255], [265, 265], [265, 275], [265, 355], [275, 5], [275, 25], [275, 35], [275, 45], [275, 55], [275, 295], [275, 305], [275, 315], [275, 325], [275, 335], [275, 355], [285, 5], [285, 25], [285, 55], [285, 295], [285, 335], [285, 355], [295, 5], [295, 25], [295, 55], [295, 75], [295, 85], [295, 95], [295, 105], [295, 115], [295, 125], [295, 135], [295, 145], [295, 155], [295, 165], [295, 175], [295, 185], [295, 195], [295, 205], [295, 215], [295, 225], [295, 235], [295, 245], [295, 255], [295, 265], [295, 275], [295, 295], [295, 335], [295, 355], [305, 5], [305, 25], [305, 55], [305, 75], [305, 275], [305, 295], [305, 335], [305, 355], [315, 5], [315, 25], [315, 55], [315, 75], [315, 275], [315, 295], [315, 335], [315, 355], [325, 5], [325, 25], [325, 35], [325, 45], [325, 55], [325, 75], [325, 85], [325, 95], [325, 105], [325, 115], [325, 125], [325, 135], [325, 145], [325, 205], [325, 215], [325, 225], [325, 235], [325, 245], [325, 255], [325, 265], [325, 275], [325, 295], [325, 305], [325, 315], [325, 325], [325, 335], [325, 355], [335, 5], [335, 145], [335, 205], [335, 355], [345, 5], [345, 25], [345, 35], [345, 45], [345, 55], [345, 65], [345, 75], [345, 85], [345, 95], [345, 105], [345, 115], [345, 125], [345, 145], [345, 205], [345, 225], [345, 235], [345, 245], [345, 255], [345, 265], [345, 275], [345, 295], [345, 305], [345, 315], [345, 325], [345, 335], [345, 355], [355, 5], [355, 25], [355, 125], [355, 145], [355, 205], [355, 225], [355, 275], [355, 295], [355, 335], [355, 355], [365, 5], [365, 25], [365, 125], [365, 145], [365, 205], [365, 225], [365, 275], [365, 295], [365, 335], [365, 355], [375, 5], [375, 25], [375, 35], [375, 45], [375, 55], [375, 65], [375, 75], [375, 85], [375, 95], [375, 105], [375, 115], [375, 125], [375, 145], [375, 155], [375, 165], [375, 175], [375, 185], [375, 195], [375, 205], [375, 225], [375, 235], [375, 245], [375, 255], [375, 265], [375, 275], [375, 295], [375, 305], [375, 315], [375, 325], [375, 335], [375, 355], [385, 5], [385, 355], [395, 5], [395, 15], [395, 25], [395, 35], [395, 45], [395, 55], [395, 65], [395, 75], [395, 85], [395, 95], [395, 105], [395, 115], [395, 125], [395, 135], [395, 145], [395, 155], [395, 165], [395, 175], [395, 185], [395, 195], [395, 205], [395, 215], [395, 225], [395, 235], [395, 245], [395, 255], [395, 265], [395, 275], [395, 285], [395, 295], [395, 305], [395, 315], [395, 325], [395, 335], [395, 345], [395, 355]]     
                vcoords = level1_canvas.coords(user)
                print(vcoords)
                colision_D()
                comer_D()
                mover_jugador(+1, 0)
                moverDerecha(10)
                coords = level1_canvas.coords(user)
                print(coords)
                if coords in lista:
                    moverDerecha(-10)
                    mover_jugador(-1, 0)
                    colision_D()

            def mover_izquierda():
                lista = [[5, 5], [5, 15], [5, 25], [5, 35], [5, 45], [5, 55], [5, 65], [5, 75], [5, 85], [5, 95], [5, 105], [5, 115], [5, 125], [5, 135], [5, 145], [5, 155], [5, 165], [5, 175], [5, 185], [5, 195], [5, 205], [5, 215], [5, 225], [5, 235], [5, 245], [5, 255], [5, 265], [5, 275], [5, 285], [5, 295], [5, 305], [5, 315], [5, 325], [5, 335], [5, 345], [5, 355], [15, 5], [15, 355], [25, 5], [25, 25], [25, 35], [25, 45], [25, 55], [25, 75], [25, 85], [25, 95], [25, 115], [25, 125], [25, 135], [25, 145], [25, 155], [25, 165], [25, 185], [25, 195], [25, 205], [25, 215], [25, 225], [25, 235], [25, 255], [25, 265], [25, 275], [25, 295], [25, 305], [25, 315], [25, 325], [25, 335], [25, 355], [35, 5], [35, 25], [35, 55], [35, 75], [35, 95], [35, 115], [35, 165], [35, 185], [35, 235], [35, 255], [35, 275], [35, 295], [35, 335], [35, 355], [45, 5], [45, 25], [45, 35], [45, 45], [45, 55], [45, 75], [45, 95], [45, 115], [45, 165], [45, 185], [45, 235], [45, 255], [45, 275], [45, 295], [45, 305], [45, 315], [45, 325], [45, 335], [45, 355], [55, 5], [55, 75], [55, 95], [55, 115], [55, 125], [55, 135], [55, 145], [55, 155], [55, 165], [55, 185], [55, 195], [55, 205], [55, 215], [55, 225], [55, 235], [55, 255], [55, 275], [55, 355], [65, 5], [65, 25], [65, 35], [65, 45], [65, 55], [65, 75], [65, 95], [65, 255], [65, 275], [65, 295], [65, 305], [65, 315], [65, 325], [65, 335], [65, 355], [75, 5], [75, 25], [75, 55], [75, 75], [75, 95], [75, 115], [75, 125], [75, 135], [75, 145], [75, 155], [75, 165], [75, 175], [75, 185], [75, 195], [75, 205], [75, 215], [75, 225], [75, 235], [75, 255], [75, 275], [75, 295], [75, 335], [75, 355], [85, 5], [85, 25], [85, 35], [85, 45], [85, 55], [85, 75], [85, 95], [85, 115], [85, 235], [85, 255], [85, 275], [85, 295], [85, 305], [85, 315], [85, 325], [85, 335], [85, 355], [95, 5], [95, 75], [95, 85], [95, 95], [95, 115], [95, 235], [95, 255], [95, 265], [95, 275], [95, 355], [105, 5], [105, 25], [105, 35], [105, 45], [105, 55], [105, 115], [105, 125], [105, 135], [105, 145], [105, 155], [105, 165], [105, 185], [105, 195], [105, 205], [105, 215], [105, 225], [105, 235], [105, 295], [105, 305], [105, 315], [105, 325], [105, 335], [105, 355], [115, 5], [115, 25], [115, 35], [115, 45], [115, 55], [115, 75], [115, 85], [115, 95], [115, 165], [115, 185], [115, 255], [115, 265], [115, 275], [115, 295], [115, 305], [115, 315], [115, 325], [115, 335], [115, 355], [125, 5], [125, 75], [125, 95], [125, 105], [125, 115], [125, 125], [125, 135], [125, 165], [125, 185], [125, 215], [125, 225], [125, 235], [125, 245], [125, 255], [125, 275], [125, 355], [135, 5], [135, 15], [135, 25], [135, 35], [135, 45], [135, 55], [135, 75], [135, 95], [135, 105], [135, 115], [135, 125], [135, 135], [135, 165], [135, 175], [135, 185], [135, 215], [135, 225], [135, 235], [135, 245], [135, 255], [135, 275], [135, 295], [135, 305], [135, 315], [135, 325], [135, 335], [135, 345], [135, 355], [145, 55], [145, 75], [145, 95], [145, 255], [145, 275], [145, 295], [155, 55], [155, 75], [155, 95], [155, 255], [155, 275], [155, 295], [165, 5], [165, 15], [165, 25], [165, 35], [165, 45], [165, 55], [165, 75], [165, 85], [165, 95], [165, 115], [165, 125], [165, 135], [165, 145], [165, 155], [165, 195], [165, 205], [165, 215], [165, 225], [165, 235], [165, 255], [165, 265], [165, 275], [165, 295], [165, 305], [165, 315], [165, 325], [165, 335], [165, 345], [165, 355], [175, 115], [175, 235], [185, 115], [185, 235], [195, 75], [195, 85], [195, 95], [195, 115], [195, 235], [195, 255], [195, 265], [195, 275], [205, 75], [205, 95], [205, 115], [205, 235], [205, 255], [205, 275], [215, 75], [215, 95], [215, 115], [215, 235], [215, 255], [215, 275], [225, 5], [225, 15], [225, 25], [225, 35], [225, 45], [225, 55], [225, 75], [225, 95], [225, 115], [225, 235], [225, 255], [225, 275], [225, 295], [225, 305], [225, 315], [225, 325], [225, 335], [225, 345], [225, 355], [235, 55], [235, 75], [235, 95], [235, 115], [235, 235], [235, 255], [235, 275], [235, 295], [245, 55], [245, 75], [245, 95], [245, 115], [245, 235], [245, 255], [245, 275], [245, 295], [255, 5], [255, 15], [255, 25], [255, 35], [255, 45], [255, 55], [255, 75], [255, 95], [255, 115], [255, 235], [255, 255], [255, 275], [255, 295], [255, 305], [255, 315], [255, 325], [255, 335], [255, 345], [255, 355], [265, 5], [265, 75], [265, 85], [265, 95], [265, 115], [265, 125], [265, 135], [265, 145], [265, 155], [265, 165], [265, 175], [265, 185], [265, 195], [265, 205], [265, 215], [265, 225], [265, 235], [265, 255], [265, 265], [265, 275], [265, 355], [275, 5], [275, 25], [275, 35], [275, 45], [275, 55], [275, 295], [275, 305], [275, 315], [275, 325], [275, 335], [275, 355], [285, 5], [285, 25], [285, 55], [285, 295], [285, 335], [285, 355], [295, 5], [295, 25], [295, 55], [295, 75], [295, 85], [295, 95], [295, 105], [295, 115], [295, 125], [295, 135], [295, 145], [295, 155], [295, 165], [295, 175], [295, 185], [295, 195], [295, 205], [295, 215], [295, 225], [295, 235], [295, 245], [295, 255], [295, 265], [295, 275], [295, 295], [295, 335], [295, 355], [305, 5], [305, 25], [305, 55], [305, 75], [305, 275], [305, 295], [305, 335], [305, 355], [315, 5], [315, 25], [315, 55], [315, 75], [315, 275], [315, 295], [315, 335], [315, 355], [325, 5], [325, 25], [325, 35], [325, 45], [325, 55], [325, 75], [325, 85], [325, 95], [325, 105], [325, 115], [325, 125], [325, 135], [325, 145], [325, 205], [325, 215], [325, 225], [325, 235], [325, 245], [325, 255], [325, 265], [325, 275], [325, 295], [325, 305], [325, 315], [325, 325], [325, 335], [325, 355], [335, 5], [335, 145], [335, 205], [335, 355], [345, 5], [345, 25], [345, 35], [345, 45], [345, 55], [345, 65], [345, 75], [345, 85], [345, 95], [345, 105], [345, 115], [345, 125], [345, 145], [345, 205], [345, 225], [345, 235], [345, 245], [345, 255], [345, 265], [345, 275], [345, 295], [345, 305], [345, 315], [345, 325], [345, 335], [345, 355], [355, 5], [355, 25], [355, 125], [355, 145], [355, 205], [355, 225], [355, 275], [355, 295], [355, 335], [355, 355], [365, 5], [365, 25], [365, 125], [365, 145], [365, 205], [365, 225], [365, 275], [365, 295], [365, 335], [365, 355], [375, 5], [375, 25], [375, 35], [375, 45], [375, 55], [375, 65], [375, 75], [375, 85], [375, 95], [375, 105], [375, 115], [375, 125], [375, 145], [375, 155], [375, 165], [375, 175], [375, 185], [375, 195], [375, 205], [375, 225], [375, 235], [375, 245], [375, 255], [375, 265], [375, 275], [375, 295], [375, 305], [375, 315], [375, 325], [375, 335], [375, 355], [385, 5], [385, 355], [395, 5], [395, 15], [395, 25], [395, 35], [395, 45], [395, 55], [395, 65], [395, 75], [395, 85], [395, 95], [395, 105], [395, 115], [395, 125], [395, 135], [395, 145], [395, 155], [395, 165], [395, 175], [395, 185], [395, 195], [395, 205], [395, 215], [395, 225], [395, 235], [395, 245], [395, 255], [395, 265], [395, 275], [395, 285], [395, 295], [395, 305], [395, 315], [395, 325], [395, 335], [395, 345], [395, 355]]     
                colision_I()
                comer_I()
                mover_jugador(-1, 0)
                moverIzquierda(10)

            def mover_abajo():
                lista = [[5, 5], [5, 15], [5, 25], [5, 35], [5, 45], [5, 55], [5, 65], [5, 75], [5, 85], [5, 95], [5, 105], [5, 115], [5, 125], [5, 135], [5, 145], [5, 155], [5, 165], [5, 175], [5, 185], [5, 195], [5, 205], [5, 215], [5, 225], [5, 235], [5, 245], [5, 255], [5, 265], [5, 275], [5, 285], [5, 295], [5, 305], [5, 315], [5, 325], [5, 335], [5, 345], [5, 355], [15, 5], [15, 355], [25, 5], [25, 25], [25, 35], [25, 45], [25, 55], [25, 75], [25, 85], [25, 95], [25, 115], [25, 125], [25, 135], [25, 145], [25, 155], [25, 165], [25, 185], [25, 195], [25, 205], [25, 215], [25, 225], [25, 235], [25, 255], [25, 265], [25, 275], [25, 295], [25, 305], [25, 315], [25, 325], [25, 335], [25, 355], [35, 5], [35, 25], [35, 55], [35, 75], [35, 95], [35, 115], [35, 165], [35, 185], [35, 235], [35, 255], [35, 275], [35, 295], [35, 335], [35, 355], [45, 5], [45, 25], [45, 35], [45, 45], [45, 55], [45, 75], [45, 95], [45, 115], [45, 165], [45, 185], [45, 235], [45, 255], [45, 275], [45, 295], [45, 305], [45, 315], [45, 325], [45, 335], [45, 355], [55, 5], [55, 75], [55, 95], [55, 115], [55, 125], [55, 135], [55, 145], [55, 155], [55, 165], [55, 185], [55, 195], [55, 205], [55, 215], [55, 225], [55, 235], [55, 255], [55, 275], [55, 355], [65, 5], [65, 25], [65, 35], [65, 45], [65, 55], [65, 75], [65, 95], [65, 255], [65, 275], [65, 295], [65, 305], [65, 315], [65, 325], [65, 335], [65, 355], [75, 5], [75, 25], [75, 55], [75, 75], [75, 95], [75, 115], [75, 125], [75, 135], [75, 145], [75, 155], [75, 165], [75, 175], [75, 185], [75, 195], [75, 205], [75, 215], [75, 225], [75, 235], [75, 255], [75, 275], [75, 295], [75, 335], [75, 355], [85, 5], [85, 25], [85, 35], [85, 45], [85, 55], [85, 75], [85, 95], [85, 115], [85, 235], [85, 255], [85, 275], [85, 295], [85, 305], [85, 315], [85, 325], [85, 335], [85, 355], [95, 5], [95, 75], [95, 85], [95, 95], [95, 115], [95, 235], [95, 255], [95, 265], [95, 275], [95, 355], [105, 5], [105, 25], [105, 35], [105, 45], [105, 55], [105, 115], [105, 125], [105, 135], [105, 145], [105, 155], [105, 165], [105, 185], [105, 195], [105, 205], [105, 215], [105, 225], [105, 235], [105, 295], [105, 305], [105, 315], [105, 325], [105, 335], [105, 355], [115, 5], [115, 25], [115, 35], [115, 45], [115, 55], [115, 75], [115, 85], [115, 95], [115, 165], [115, 185], [115, 255], [115, 265], [115, 275], [115, 295], [115, 305], [115, 315], [115, 325], [115, 335], [115, 355], [125, 5], [125, 75], [125, 95], [125, 105], [125, 115], [125, 125], [125, 135], [125, 165], [125, 185], [125, 215], [125, 225], [125, 235], [125, 245], [125, 255], [125, 275], [125, 355], [135, 5], [135, 15], [135, 25], [135, 35], [135, 45], [135, 55], [135, 75], [135, 95], [135, 105], [135, 115], [135, 125], [135, 135], [135, 165], [135, 175], [135, 185], [135, 215], [135, 225], [135, 235], [135, 245], [135, 255], [135, 275], [135, 295], [135, 305], [135, 315], [135, 325], [135, 335], [135, 345], [135, 355], [145, 55], [145, 75], [145, 95], [145, 255], [145, 275], [145, 295], [155, 55], [155, 75], [155, 95], [155, 255], [155, 275], [155, 295], [165, 5], [165, 15], [165, 25], [165, 35], [165, 45], [165, 55], [165, 75], [165, 85], [165, 95], [165, 115], [165, 125], [165, 135], [165, 145], [165, 155], [165, 195], [165, 205], [165, 215], [165, 225], [165, 235], [165, 255], [165, 265], [165, 275], [165, 295], [165, 305], [165, 315], [165, 325], [165, 335], [165, 345], [165, 355], [175, 115], [175, 235], [185, 115], [185, 235], [195, 75], [195, 85], [195, 95], [195, 115], [195, 235], [195, 255], [195, 265], [195, 275], [205, 75], [205, 95], [205, 115], [205, 235], [205, 255], [205, 275], [215, 75], [215, 95], [215, 115], [215, 235], [215, 255], [215, 275], [225, 5], [225, 15], [225, 25], [225, 35], [225, 45], [225, 55], [225, 75], [225, 95], [225, 115], [225, 235], [225, 255], [225, 275], [225, 295], [225, 305], [225, 315], [225, 325], [225, 335], [225, 345], [225, 355], [235, 55], [235, 75], [235, 95], [235, 115], [235, 235], [235, 255], [235, 275], [235, 295], [245, 55], [245, 75], [245, 95], [245, 115], [245, 235], [245, 255], [245, 275], [245, 295], [255, 5], [255, 15], [255, 25], [255, 35], [255, 45], [255, 55], [255, 75], [255, 95], [255, 115], [255, 235], [255, 255], [255, 275], [255, 295], [255, 305], [255, 315], [255, 325], [255, 335], [255, 345], [255, 355], [265, 5], [265, 75], [265, 85], [265, 95], [265, 115], [265, 125], [265, 135], [265, 145], [265, 155], [265, 165], [265, 175], [265, 185], [265, 195], [265, 205], [265, 215], [265, 225], [265, 235], [265, 255], [265, 265], [265, 275], [265, 355], [275, 5], [275, 25], [275, 35], [275, 45], [275, 55], [275, 295], [275, 305], [275, 315], [275, 325], [275, 335], [275, 355], [285, 5], [285, 25], [285, 55], [285, 295], [285, 335], [285, 355], [295, 5], [295, 25], [295, 55], [295, 75], [295, 85], [295, 95], [295, 105], [295, 115], [295, 125], [295, 135], [295, 145], [295, 155], [295, 165], [295, 175], [295, 185], [295, 195], [295, 205], [295, 215], [295, 225], [295, 235], [295, 245], [295, 255], [295, 265], [295, 275], [295, 295], [295, 335], [295, 355], [305, 5], [305, 25], [305, 55], [305, 75], [305, 275], [305, 295], [305, 335], [305, 355], [315, 5], [315, 25], [315, 55], [315, 75], [315, 275], [315, 295], [315, 335], [315, 355], [325, 5], [325, 25], [325, 35], [325, 45], [325, 55], [325, 75], [325, 85], [325, 95], [325, 105], [325, 115], [325, 125], [325, 135], [325, 145], [325, 205], [325, 215], [325, 225], [325, 235], [325, 245], [325, 255], [325, 265], [325, 275], [325, 295], [325, 305], [325, 315], [325, 325], [325, 335], [325, 355], [335, 5], [335, 145], [335, 205], [335, 355], [345, 5], [345, 25], [345, 35], [345, 45], [345, 55], [345, 65], [345, 75], [345, 85], [345, 95], [345, 105], [345, 115], [345, 125], [345, 145], [345, 205], [345, 225], [345, 235], [345, 245], [345, 255], [345, 265], [345, 275], [345, 295], [345, 305], [345, 315], [345, 325], [345, 335], [345, 355], [355, 5], [355, 25], [355, 125], [355, 145], [355, 205], [355, 225], [355, 275], [355, 295], [355, 335], [355, 355], [365, 5], [365, 25], [365, 125], [365, 145], [365, 205], [365, 225], [365, 275], [365, 295], [365, 335], [365, 355], [375, 5], [375, 25], [375, 35], [375, 45], [375, 55], [375, 65], [375, 75], [375, 85], [375, 95], [375, 105], [375, 115], [375, 125], [375, 145], [375, 155], [375, 165], [375, 175], [375, 185], [375, 195], [375, 205], [375, 225], [375, 235], [375, 245], [375, 255], [375, 265], [375, 275], [375, 295], [375, 305], [375, 315], [375, 325], [375, 335], [375, 355], [385, 5], [385, 355], [395, 5], [395, 15], [395, 25], [395, 35], [395, 45], [395, 55], [395, 65], [395, 75], [395, 85], [395, 95], [395, 105], [395, 115], [395, 125], [395, 135], [395, 145], [395, 155], [395, 165], [395, 175], [395, 185], [395, 195], [395, 205], [395, 215], [395, 225], [395, 235], [395, 245], [395, 255], [395, 265], [395, 275], [395, 285], [395, 295], [395, 305], [395, 315], [395, 325], [395, 335], [395, 345], [395, 355]]     
                colision_AB()
                comer_AB()
                mover_jugador(0, +1)
                moverAbajo(10)

            def mover_arriba():
                lista = [[5, 5], [5, 15], [5, 25], [5, 35], [5, 45], [5, 55], [5, 65], [5, 75], [5, 85], [5, 95], [5, 105], [5, 115], [5, 125], [5, 135], [5, 145], [5, 155], [5, 165], [5, 175], [5, 185], [5, 195], [5, 205], [5, 215], [5, 225], [5, 235], [5, 245], [5, 255], [5, 265], [5, 275], [5, 285], [5, 295], [5, 305], [5, 315], [5, 325], [5, 335], [5, 345], [5, 355], [15, 5], [15, 355], [25, 5], [25, 25], [25, 35], [25, 45], [25, 55], [25, 75], [25, 85], [25, 95], [25, 115], [25, 125], [25, 135], [25, 145], [25, 155], [25, 165], [25, 185], [25, 195], [25, 205], [25, 215], [25, 225], [25, 235], [25, 255], [25, 265], [25, 275], [25, 295], [25, 305], [25, 315], [25, 325], [25, 335], [25, 355], [35, 5], [35, 25], [35, 55], [35, 75], [35, 95], [35, 115], [35, 165], [35, 185], [35, 235], [35, 255], [35, 275], [35, 295], [35, 335], [35, 355], [45, 5], [45, 25], [45, 35], [45, 45], [45, 55], [45, 75], [45, 95], [45, 115], [45, 165], [45, 185], [45, 235], [45, 255], [45, 275], [45, 295], [45, 305], [45, 315], [45, 325], [45, 335], [45, 355], [55, 5], [55, 75], [55, 95], [55, 115], [55, 125], [55, 135], [55, 145], [55, 155], [55, 165], [55, 185], [55, 195], [55, 205], [55, 215], [55, 225], [55, 235], [55, 255], [55, 275], [55, 355], [65, 5], [65, 25], [65, 35], [65, 45], [65, 55], [65, 75], [65, 95], [65, 255], [65, 275], [65, 295], [65, 305], [65, 315], [65, 325], [65, 335], [65, 355], [75, 5], [75, 25], [75, 55], [75, 75], [75, 95], [75, 115], [75, 125], [75, 135], [75, 145], [75, 155], [75, 165], [75, 175], [75, 185], [75, 195], [75, 205], [75, 215], [75, 225], [75, 235], [75, 255], [75, 275], [75, 295], [75, 335], [75, 355], [85, 5], [85, 25], [85, 35], [85, 45], [85, 55], [85, 75], [85, 95], [85, 115], [85, 235], [85, 255], [85, 275], [85, 295], [85, 305], [85, 315], [85, 325], [85, 335], [85, 355], [95, 5], [95, 75], [95, 85], [95, 95], [95, 115], [95, 235], [95, 255], [95, 265], [95, 275], [95, 355], [105, 5], [105, 25], [105, 35], [105, 45], [105, 55], [105, 115], [105, 125], [105, 135], [105, 145], [105, 155], [105, 165], [105, 185], [105, 195], [105, 205], [105, 215], [105, 225], [105, 235], [105, 295], [105, 305], [105, 315], [105, 325], [105, 335], [105, 355], [115, 5], [115, 25], [115, 35], [115, 45], [115, 55], [115, 75], [115, 85], [115, 95], [115, 165], [115, 185], [115, 255], [115, 265], [115, 275], [115, 295], [115, 305], [115, 315], [115, 325], [115, 335], [115, 355], [125, 5], [125, 75], [125, 95], [125, 105], [125, 115], [125, 125], [125, 135], [125, 165], [125, 185], [125, 215], [125, 225], [125, 235], [125, 245], [125, 255], [125, 275], [125, 355], [135, 5], [135, 15], [135, 25], [135, 35], [135, 45], [135, 55], [135, 75], [135, 95], [135, 105], [135, 115], [135, 125], [135, 135], [135, 165], [135, 175], [135, 185], [135, 215], [135, 225], [135, 235], [135, 245], [135, 255], [135, 275], [135, 295], [135, 305], [135, 315], [135, 325], [135, 335], [135, 345], [135, 355], [145, 55], [145, 75], [145, 95], [145, 255], [145, 275], [145, 295], [155, 55], [155, 75], [155, 95], [155, 255], [155, 275], [155, 295], [165, 5], [165, 15], [165, 25], [165, 35], [165, 45], [165, 55], [165, 75], [165, 85], [165, 95], [165, 115], [165, 125], [165, 135], [165, 145], [165, 155], [165, 195], [165, 205], [165, 215], [165, 225], [165, 235], [165, 255], [165, 265], [165, 275], [165, 295], [165, 305], [165, 315], [165, 325], [165, 335], [165, 345], [165, 355], [175, 115], [175, 235], [185, 115], [185, 235], [195, 75], [195, 85], [195, 95], [195, 115], [195, 235], [195, 255], [195, 265], [195, 275], [205, 75], [205, 95], [205, 115], [205, 235], [205, 255], [205, 275], [215, 75], [215, 95], [215, 115], [215, 235], [215, 255], [215, 275], [225, 5], [225, 15], [225, 25], [225, 35], [225, 45], [225, 55], [225, 75], [225, 95], [225, 115], [225, 235], [225, 255], [225, 275], [225, 295], [225, 305], [225, 315], [225, 325], [225, 335], [225, 345], [225, 355], [235, 55], [235, 75], [235, 95], [235, 115], [235, 235], [235, 255], [235, 275], [235, 295], [245, 55], [245, 75], [245, 95], [245, 115], [245, 235], [245, 255], [245, 275], [245, 295], [255, 5], [255, 15], [255, 25], [255, 35], [255, 45], [255, 55], [255, 75], [255, 95], [255, 115], [255, 235], [255, 255], [255, 275], [255, 295], [255, 305], [255, 315], [255, 325], [255, 335], [255, 345], [255, 355], [265, 5], [265, 75], [265, 85], [265, 95], [265, 115], [265, 125], [265, 135], [265, 145], [265, 155], [265, 165], [265, 175], [265, 185], [265, 195], [265, 205], [265, 215], [265, 225], [265, 235], [265, 255], [265, 265], [265, 275], [265, 355], [275, 5], [275, 25], [275, 35], [275, 45], [275, 55], [275, 295], [275, 305], [275, 315], [275, 325], [275, 335], [275, 355], [285, 5], [285, 25], [285, 55], [285, 295], [285, 335], [285, 355], [295, 5], [295, 25], [295, 55], [295, 75], [295, 85], [295, 95], [295, 105], [295, 115], [295, 125], [295, 135], [295, 145], [295, 155], [295, 165], [295, 175], [295, 185], [295, 195], [295, 205], [295, 215], [295, 225], [295, 235], [295, 245], [295, 255], [295, 265], [295, 275], [295, 295], [295, 335], [295, 355], [305, 5], [305, 25], [305, 55], [305, 75], [305, 275], [305, 295], [305, 335], [305, 355], [315, 5], [315, 25], [315, 55], [315, 75], [315, 275], [315, 295], [315, 335], [315, 355], [325, 5], [325, 25], [325, 35], [325, 45], [325, 55], [325, 75], [325, 85], [325, 95], [325, 105], [325, 115], [325, 125], [325, 135], [325, 145], [325, 205], [325, 215], [325, 225], [325, 235], [325, 245], [325, 255], [325, 265], [325, 275], [325, 295], [325, 305], [325, 315], [325, 325], [325, 335], [325, 355], [335, 5], [335, 145], [335, 205], [335, 355], [345, 5], [345, 25], [345, 35], [345, 45], [345, 55], [345, 65], [345, 75], [345, 85], [345, 95], [345, 105], [345, 115], [345, 125], [345, 145], [345, 205], [345, 225], [345, 235], [345, 245], [345, 255], [345, 265], [345, 275], [345, 295], [345, 305], [345, 315], [345, 325], [345, 335], [345, 355], [355, 5], [355, 25], [355, 125], [355, 145], [355, 205], [355, 225], [355, 275], [355, 295], [355, 335], [355, 355], [365, 5], [365, 25], [365, 125], [365, 145], [365, 205], [365, 225], [365, 275], [365, 295], [365, 335], [365, 355], [375, 5], [375, 25], [375, 35], [375, 45], [375, 55], [375, 65], [375, 75], [375, 85], [375, 95], [375, 105], [375, 115], [375, 125], [375, 145], [375, 155], [375, 165], [375, 175], [375, 185], [375, 195], [375, 205], [375, 225], [375, 235], [375, 245], [375, 255], [375, 265], [375, 275], [375, 295], [375, 305], [375, 315], [375, 325], [375, 335], [375, 355], [385, 5], [385, 355], [395, 5], [395, 15], [395, 25], [395, 35], [395, 45], [395, 55], [395, 65], [395, 75], [395, 85], [395, 95], [395, 105], [395, 115], [395, 125], [395, 135], [395, 145], [395, 155], [395, 165], [395, 175], [395, 185], [395, 195], [395, 205], [395, 215], [395, 225], [395, 235], [395, 245], [395, 255], [395, 265], [395, 275], [395, 285], [395, 295], [395, 305], [395, 315], [395, 325], [395, 335], [395, 345], [395, 355]]     
                colision_A()
                comer_A()
                mover_jugador(0, -1)
                moverArriba(10)

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
            ventana_instance.mainloop()


        def level_2(self, enemies):
            global score, Name
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
            #Condicion para que se abra el salon de la fama 
            if comida == 0:
                file = open('database_scores.txt', 'a')
                entry = str(score) + ' ' + str(Name) + '\n'
                file.write(entry)
                file.close()
                ventana_instance = Ventanas()
                ventana_instance.highScores()
            #Condicion de game over 
            if lives == 0:
                ventana_instance = Ventanas()
                ventana_instance.game_over()
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
            tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
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
            pacman = PacMan(estado=True, posicion_x=18, posicion_y=28, velocidad=1)
            user_u = Image.open('pacman.png')
            user_i = ImageTk.PhotoImage(user_u)
            
            user = level2_canvas.create_image(175, 275, image=user_i, anchor='center')
            
            # Movimiento de pacman
            def moverDerecha():
                level2_canvas.move(user, 10, 0)

            def moverIzquierda():
                level2_canvas.move(user, -10, 0)

            def moverArriba():
                level2_canvas.move(user, 0, -10)

            def moverAbajo():
                level2_canvas.move(user, 0, 10)

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
                            row = "6"
                        else:
                            for enemigo in enemigos:
                                if n == enemigo.posicion_y and x == enemigo.posicion_x:
                                    row = "7"
                                    break
                            else:
                                if tablero[n][x] == 0:
                                    row = "0 "
                                else:
                                    row = "4 "
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
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX - 1][pacmanY] = 3 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX - 1][pacmanY] =  4
            def comer_I():
                global score
                pacmanX = pacman.get_posX() - 1
                pacmanY = pacman.get_posY()
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX + 1][pacmanY] = 0 
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX + 1][pacmanY] = 4 
            def comer_AB():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() + 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY - 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY - 1] = 4
            def comer_A():
                global score
                pacmanX = pacman.get_posX() 
                pacmanY = pacman.get_posY() - 1
                if tablero[pacmanX][pacmanY] == 2:
                    pacman.change_estado(1)
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    time.sleep(15)
                    pacman.change_estado(2)
                    tablero[pacmanX][pacmanY + 1] = 0
                elif tablero[pacmanX][pacmanY] == 3:
                    score += 0.50
                    comida-=1
                    score_text.config(text='Score: ' + str(score), bg='white')
                    tablero[pacmanX][pacmanY + 1] = 0 

            def puede_mover(x, y):
                return 0 <= x < len(tablero[0]) and 0 <= y < len(tablero) and tablero[y][x] != 0 and not any(enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos)


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
                moverDerecha()

            def mover_izquierda():
                colision_I()
                comer_I()
                mover_jugador(-1, 0)
                moverIzquierda()

            def mover_abajo():
                colision_AB()
                comer_AB()
                mover_jugador(0, +1)
                moverAbajo()

            def mover_arriba():
                colision_A()
                comer_A()
                mover_jugador(0, -1)
                moverArriba()

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
            ventana_instance.mainloop()

    #Instancias de las clases 
    def namePantalla():
        ventana_instance = Ventanas()
        ventana_instance.namePantalla()
    def highScores():
        ventana_instance = Ventanas()
        ventana_instance.highScores()
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
    info_button = Button(r, text='About us', font='Courier', command=aboutUs)
    help_button = Button(r, text='Help', command=helpCenter)
    play_window = mainmenu_canvas.create_window(600, 460, anchor="center", window=play_button)
    score_window = mainmenu_canvas.create_window(600, 510, anchor="n", window=score_button)
    info_window = mainmenu_canvas.create_window(600, 550, anchor="n", window=info_button)
    help_window = mainmenu_canvas.create_window(1150, 600, anchor="n", window=help_button)

    r.mainloop()
ven0()