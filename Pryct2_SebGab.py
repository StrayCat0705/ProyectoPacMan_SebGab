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
        def __init__(self, score, name):
            self.name = name
            self.score = score

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
                    ventana_instance = Ventanas(self.score, self.name)
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
            #Variables
            lives = 3
            enemies = 5
            high_score = 999999999
            comida = 10
            #Top level
            level1 = tk.Toplevel()
            level1.geometry('400x400')
            level1.config(bg=white)
            level1.title('PUCKMAN-lvl1')
            #Canvas de lvl1
            level1_canvas = Canvas(level1, width=400, height=360, bg= 'black')
            level1_canvas.pack()
            #Condicion para que se abra el segundo nivel 
            if comida == 0:
                ventana_instance = Ventanas(self.score, self.name)
                ventana_instance.level_2(enemies)
            #Frame
            info_frame = tk.Frame(level1, bg=white)
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
            matriz =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
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
            dibujar_cuadros_desde_matriz(matriz)
        def level_2(self, enemies):
            #Variables
            lives = 3
            enemies = 5
            high_score = 999999999
            comida = 10
            #Top level
            level2 = tk.Toplevel()
            level2.geometry('300x300')
            level2.config(bg=white)
            level2.title('PUCKMAN-lvl2')
            #Canvas de lvl1
            level2_canvas = Canvas(level2, width=300, height=360, bg= 'black')
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

    #Instancias de las clases 
    def namePantalla():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()
    def highScores():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.highScores()
    def settings():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.settings()
    def aboutUs():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.aboutUs()
    def helpCenter():
        ventana_instance = Ventanas(score=0, name="DefaultName")
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