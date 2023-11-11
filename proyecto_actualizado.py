import keyboard
import random

# Tamaño del tablero
filas = 40
columnas = 36

# Crear el tablero inicial
tablero = [[4 for _ in range(columnas)] for n in range(filas)]

# Lista de enemigos (cada enemigo es una tupla de coordenadas)
enemigos = [(10, 15), (20, 25), (30, 5)]

# Posición inicial del jugador en la matriz
posx = 5
posy = 5

# Función para imprimir el tablero con separación horizontal
def imprimir_matriz():
    for n in range(len(tablero)):
        row = ""
        for x in range(len(tablero[0])):
            if n == posy and x == posx:
                row += "⍩⃝ "
            elif (n, x) in enemigos:
                row += "👻 "
            else:
                if tablero[n][x] == 0:
                    row += "0 "
                else:
                    row += "4 "
        print(row)
    print(f"posx:{posx}, posy: {posy}\n")

# Función para actualizar la matriz con el movimiento de los enemigos
# Función para actualizar la matriz con el movimiento de los enemigos
def mover_enemigos():
    global posx, posy

    for i, (enemigo_x, enemigo_y) in enumerate(enemigos):
        # Generar un movimiento aleatorio para cada enemigo
        movimiento_x = random.choice([-1, 0, 1])
        movimiento_y = random.choice([-1, 0, 1])

        # Actualizar la posición del enemigo
        nuevo_x = enemigo_x + movimiento_x
        nuevo_y = enemigo_y + movimiento_y

        # Verificar que el enemigo no choque con una pared o salga del tablero
        if (0 <= nuevo_x < columnas and 0 <= nuevo_y < filas and tablero[nuevo_y][nuevo_x] != 0):
            enemigos[i] = (nuevo_x, nuevo_y)

    # Verificar si el jugador choca con un enemigo
    if (posx, posy) in enemigos:
        print("¡Has sido atrapado por un fantasma! Fin del juego.")
        exit()  # Puedes ajustar esto según tus necesidades


# Restringir el movimiento del jugador solo cuando no hay enemigos en la casilla
def puede_mover(x, y):
    return (0 <= x < columnas and 0 <= y < filas and tablero[y][x] != 0 and (x, y) not in enemigos)

# Función para mover al jugador
def mover_jugador(dx, dy):
    global posx, posy
    nuevo_x = posx + dx
    nuevo_y = posy + dy
    if puede_mover(nuevo_x, nuevo_y):
        posx = nuevo_x
        posy = nuevo_y
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

# Bucle principal
while True:
    mover_enemigos()  # Mover a los enemigos aleatoriamente
    imprimir_matriz()  # Actualizar y mostrar la matriz con separación horizontal
    keyboard.read_event()  # Leer eventos del teclado