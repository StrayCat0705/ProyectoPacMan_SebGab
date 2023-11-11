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

    class Ventanas:
        def __init__(self, score, name):
            self.name = name
            self.score = score

        def namePantalla(self):
            # Colores
            n_grey = '#242424'
            # Top level
            name_pantalla_TP = tk.Toplevel()
            name_pantalla_TP.geometry('600x650')
            name_pantalla_TP.config(bg='#242424')
            name_pantalla_TP.title('PACKUMAN-lvl1')

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

        def level_1(self):
            print(5, str(self.name), self.score)
            ventana_instance = Ventanas(self.score, self.name)
            ventana_instance.level_2()

        def level_2(self):
            print(6, str(self.name), self.score)

    # Create instances of the class
    def namePantalla():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()
    def highScores():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()
    def settings():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()
    def aboutUs():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()
    def helpCenter():
        ventana_instance = Ventanas(score=0, name="DefaultName")
        ventana_instance.namePantalla()

    #Botones
    play_button = Button(r, text='PLAY', font='Courier 14', command=namePantalla)
    play_button.config(width=14, height=3)
    score_button = Button(r, text='High scores', font='Courier', command=highScores)
    config_button = Button(r, text='Settings', font='Courier', command=settings)
    info_button = Button(r, text='About us', font='Courier', command=aboutUs)
    help_button = Button(r, text='Help', command=helpCenter)
    play_window = mainmenu_canvas.create_window(600, 460, anchor="center", window=play_button)
    score_window = mainmenu_canvas.create_window(600, 510, anchor="n", window=score_button)
    config_window = mainmenu_canvas.create_window(600, 550, anchor="n", window=config_button)
    info_window = mainmenu_canvas.create_window(600, 590, anchor="n", window=info_button)
    help_window = mainmenu_canvas.create_window(1150, 600, anchor="n", window=help_button)

    r.mainloop()
ven0()
