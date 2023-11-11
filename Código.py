import keyboard
import random

# Tamaño del tablero
filas = 40
columnas = 36

# Crear el tablero inicial
tablero = [[4 if (n % 4) != 0 else 0 for _ in range(columnas)] for n in range(filas)]

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

# Clase para PacMan
class PacMan(Personaje):
    def __init__(self, estado, posicion_x, posicion_y, velocidad):
        super().__init__(estado, posicion_x, posicion_y, velocidad)

    def comer_alimento(self):
        # Lógica específica para PacMan al comer alimento
        pass

    def comer_capsula(self):
        # Lógica específica para PacMan al comer cápsula
        pass

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

# Crear instancias de PacMan y Fantasma
pacman = PacMan(estado=True, posicion_x=2, posicion_y=2, velocidad=1)
fantasma_rojo = Fantasma(estado=True, posicion_x=20, posicion_y=20, color='rojo')
