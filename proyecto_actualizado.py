import keyboard
import random

# Tamaño del tablero
filas = 40
columnas = 36

# Crear el tablero inicial
tablero = [[4 for _ in range(columnas)] for n in range(filas)]


<<<<<<< HEAD
## borde de abajo
fila_deseada = 0  # La primera fila, ten en cuenta que la indexación comienza desde 0
columna_inicio = 0
columna_fin = 36

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for columna in range(columna_inicio, columna_fin):
    tablero[fila_deseada][columna] = valor

## borde de arriba
fila_deseada = 39  # La primera fila, ten en cuenta que la indexación comienza desde 0
columna_inicio = 0
columna_fin = 36

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for columna in range(columna_inicio, columna_fin):
    tablero[fila_deseada][columna] = valor

## borde de la derecha de abajo
columna_deseada = 0  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 0
fila_fin = 14

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    tablero[fila][columna_deseada] = valor

## borde de abajo a la izquierda
columna_deseada = 35  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 0
fila_fin = 14

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    tablero[fila][columna_deseada] = valor

##borde de arriba a la derecha
columna_deseada = 0  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 26
fila_fin = 39

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    tablero[fila][columna_deseada] = valor

##borde de arriba a la izquierda
columna_deseada = 35  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 26
fila_fin = 39

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    tablero[fila][columna_deseada] = valor

## primer cuadrado derecha abajo
columna_inicio = 2
columna_final = 5  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 2
fila_fin = 5

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    for columna in range(columna_inicio, columna_final):
        tablero[fila][columna] = valor

## segundo cuadrado
columna_inicio = 2
columna_final = 5  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 6
fila_fin = 9

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    for columna in range(columna_inicio, columna_final):
        tablero[fila][columna] = valor

## tercer cuadrado
columna_inicio = 2
columna_final = 5  # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 10
fila_fin = 12

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    for columna in range(columna_inicio, columna_final):
        tablero[fila][columna] = valor


##cuadrado al lado de los 3 cuadrados en la derecha abajo
columna_inicio = 7
columna_final = 10 # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 2
fila_fin = 10

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    for columna in range(columna_inicio, columna_final):
        tablero[fila][columna] = valor

##pared de en medio derecha abajo
columna_inicio = 7
columna_final = 10 # La primera fila, ten en cuenta que la indexación comienza desde 0
fila_inicio = 2
fila_fin = 10

# Valor a colocar en ese rango de columnas
valor = 0

# Asignar el valor en el rango específico de columnas en la fila
for fila in range(fila_inicio, fila_fin):
    for columna in range(columna_inicio, columna_final):
        tablero[fila][columna] = valor


=======
>>>>>>> 6c152cb119fabd46483b9efadb000499b8f7cba0

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
                row += "6 "
            else:
                for enemigo in enemigos:
                    if n == enemigo.posicion_y and x == enemigo.posicion_x:
                        row += "5 "
                        break
                else:
                    if tablero[n][x] == 0:
                        row += "0 "
                    else:
                        row += "4 "
        print(row)
    print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

# Restringir el movimiento del jugador solo cuando no hay enemigos en la casilla
def puede_mover(x, y):
    return (0 <= x < columnas and 0 <= y < filas and tablero[y][x] != 0 and not any(enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos))

# Función para mover al jugador
def mover_jugador(dx, dy):
    nuevo_x = pacman.posicion_x + dx
    nuevo_y = pacman.posicion_y + dy
    if puede_mover(nuevo_x, nuevo_y):
        pacman.posicion_x = nuevo_x
        pacman.posicion_y = nuevo_y
        imprimir_matriz()

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

        if (0 <= nuevo_x < columnas and 0 <= nuevo_y < filas and tablero[nuevo_y][nuevo_x] != 0):
            enemigo.posicion_x = nuevo_x
            enemigo.posicion_y = nuevo_y

# Bucle principal
while True:
    mover_enemigos()
    imprimir_matriz()
    keyboard.read_event()