import keyboard
import random

# Tamaño del tablero
filas = 7
columnas = 7

# Crear el tablero inicial
tablero1 = [[4 for _ in range(columnas)] for n in range(filas)]
tablero2 = [[4 for _ in range(columnas)] for n in range(filas)]


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
    #Conseguir las coordenadas de pacman 
    def get_posicionXY_pac(self):
        return self.posicion_x, self.posicion_y
    #Conseguir el estado de pacman
    def get_estadoPac(self):
        return self.estado
    #Cambiar de estado
    def cambio_de_estado(self):
        self.estado = 'comer'
    def cambio_de_estado2(self):
        self.estado = 'comida'
        
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
    #Conseguir las coordenadas del enemigo 
    def get_posicionXY_en(self):
        return self.posicion_x, self.posicion_y

# Crear una instancia de PacMan y configurar su posición inicial
pacman = PacMan(estado=True, posicion_x=5, posicion_y=5, velocidad=1)

# Lista de enemigos (cada enemigo es una instancia de Fantasma)
enemigos = [Fantasma(estado=True, posicion_x=6, posicion_y=5, color='rojo'),
            Fantasma(estado=True, posicion_x=20, posicion_y=25, color='celeste'),
            Fantasma(estado=True, posicion_x=30, posicion_y=5, color='rosado'),
            Fantasma(estado=True, posicion_x=30, posicion_y=10, color='naranja')]

# Función para imprimir el tablero con separación horizontal
def imprimir_matriz():
    for n in range(len(tablero1)):
        row = ""
        for x in range(len(tablero1[0])):
            if n == pacman.posicion_y and x == pacman.posicion_x:
                row += "⍩⃝ "
            else:
                for enemigo in enemigos:
                    if n == enemigo.posicion_y and x == enemigo.posicion_x:
                        row += "👻 "
                        break
                else:
                    if tablero1[n][x] == 0:
                        row += "0 "
                    else:
                        row += "4 "
        print(row)
    print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

def imprimir_matriz2():
    for n in range(len(tablero1)):
        row = ""
        for x in range(len(tablero1[0])):
            for enemigo in enemigos:
                if n == enemigo.posicion_y and x == enemigo.posicion_x:
                    row += "👻 "
                    break
                else:
                    if tablero1[n][x] == 0:
                        row += "0 "
                    else:
                        row += "4 "
        print(row)
    print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

# Función para mover al jugador
def mover_jugador(dx, dy):
    nuevo_x = pacman.posicion_x + dx
    nuevo_y = pacman.posicion_y + dy
    pacman.posicion_x = nuevo_x
    pacman.posicion_y = nuevo_y
    imprimir_matriz()
    colisiones()

#Colisiones
def colisiones():
    i = 0
    n = len(enemigos)
    while i != n:
        if enemigos[i].get_posicionXY_en() == pacman.get_posicionXY_pac():
            i+=1
            print('chocaron')
        elif i == n:
            break
        else:
            i+=1
            print('No chocaron')

# Asignar las funciones de movimiento a las teclas
def mover_derecha():
    mover_jugador(1, 0)

def mover_izquierda():
    mover_jugador(-1, 0)

def mover_abajo():
    mover_jugador(0, 1)

def mover_arriba():
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

        if (0 <= nuevo_x < columnas and 0 <= nuevo_y < filas and tablero2[nuevo_y][nuevo_x] != 0):
            enemigo.posicion_x = nuevo_x
            enemigo.posicion_y = nuevo_y

# Bucle principal
while True:
    #mover_enemigos()
    imprimir_matriz()
    keyboard.read_event()

