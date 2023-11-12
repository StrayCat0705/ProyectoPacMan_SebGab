import keyboard
import random
import time
from threading import Timer
import copy

# Tamaño del tablero
filas = 15
columnas = 15

# Crear el tablero inicial
tablero = [[4 for _ in range(columnas)] for _ in range(filas)]

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



# Modificar la clase PacMan
class PacMan(Personaje):
    def __init__(self, estado, posicion_x, posicion_y, velocidad):
        super().__init__(estado, posicion_x, posicion_y, velocidad)
        self.tiempo_ayuda_activado = False
# ... (código existente

    def comer_capsula(self):
        global objetos_pizza, enemigos, timer_ayuda
        # Lógica específica para PacMan al comer cápsula
        if (self.posicion_x, self.posicion_y) in objetos_pizza:
            print("¡Pacman ha comido una pizza! Ahora es un comedor de cheeseburgers.")
            self.estado = "comedor de cheeseburger"
            objetos_pizza.remove((self.posicion_x, self.posicion_y))  # Eliminar el objeto "🍕" del tablero

            # Poner en estado "ayuda" a los enemigos y cambiar su representación a "🐶"
            for enemigo in enemigos:
                if enemigo.estado != "ayuda":
                    enemigo.estado = "ayuda"
                    enemigo.velocidad = 0  # Hacer que los enemigos no se muevan durante el estado "ayuda"
                    print(f"El fantasma {enemigo.color} está en estado de ayuda.")

            # Crear un temporizador para revertir el estado "ayuda" después de un tiempo
            def revertir_estado_ayuda():
                for enemigo in enemigos:
                    if enemigo.estado == "ayuda":
                        enemigo.estado = "normal"
                        enemigo.velocidad = 1  # Restaurar la velocidad normal
                        print(f"El estado de ayuda del fantasma {enemigo.color} ha terminado.")

            # Programar la reversión del estado "ayuda" después de un tiempo
            timer_ayuda = Timer(tiempo_ayuda, revertir_estado_ayuda)
            timer_ayuda.start()


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

    def reaparecer(self):
        # Reiniciar la posición y estado del fantasma con un color aleatorio
        self.posicion_x = random.randint(0, columnas - 1)
        self.posicion_y = random.randint(0, filas - 1)
        self.estado = "normal"
        self.color = random.choice(['rosado', 'naranja', 'rojo', 'celeste'])

# Crear instancias de PacMan y Fantasmas
pacman = PacMan(estado=True, posicion_x=5, posicion_y=5, velocidad=1)
enemigos = [
    Fantasma(estado=True, posicion_x=1, posicion_y=1, color='rojo'),
    Fantasma(estado=True, posicion_x=2, posicion_y=2, color='celeste'),
    Fantasma(estado=True, posicion_x=3, posicion_y=3, color='rosado'),
    Fantasma(estado=True, posicion_x=4, posicion_y=4, color='naranja')
]

# Lista de objetos "🍕"
objetos_pizza = [(8, 8), (7, 7), (6, 6)]

# Tiempo de duración del estado "ayuda" (en segundos)
tiempo_ayuda = 10

# Función para imprimir el tablero con separación horizontal
def imprimir_matriz():
    for n in range(len(tablero)):
        row = ""
        for x in range(len(tablero[0])):
            if n == pacman.posicion_y and x == pacman.posicion_x:
                row += "⍩⃝ "
            else:
                for enemigo in enemigos:
                    if n == enemigo.posicion_y and x == enemigo.posicion_x:
                        if enemigo.estado == "ayuda":
                            row += "🐶 "
                        else:
                            row += "👻 "
                        break
                else:
                    if (x, n) in objetos_pizza:
                        row += "🍕 "
                    elif tablero[n][x] == 0:
                        row += "0 "
                    else:
                        row += "4 "
        print(row)
    print(f"posx:{pacman.posicion_x}, posy: {pacman.posicion_y}\n")

# Restringir el movimiento del jugador solo cuando no hay enemigos en la casilla
def mover_jugador(dx, dy):
    nuevo_x = pacman.posicion_x + dx
    nuevo_y = pacman.posicion_y + dy

    pos_x_anterior = pacman.posicion_x
    pos_y_anterior = pacman.posicion_y

    if puede_mover(nuevo_x, nuevo_y):
        pacman.posicion_x = nuevo_x
        pacman.posicion_y = nuevo_y

        pacman.comer_capsula()

        # Verificar si hay un fantasma en las nuevas coordenadas
        for enemigo in enemigos:
            if enemigo.posicion_x == nuevo_x and enemigo.posicion_y == nuevo_y:
                manejar_colision_pacman_fantasma(enemigo)
                break

        imprimir_matriz()
    else:
        pacman.posicion_x = pos_x_anterior
        pacman.posicion_y = pos_y_anterior
# Restringir el movimiento del jugador solo cuando no hay enemigos en la casilla

def manejar_colision_pacman_fantasma(fantasma):
    if pacman.estado == "comedor de cheeseburger":
        print(f"Pacman ha comido al fantasma {fantasma.color}!")
        # Aquí puedes implementar la lógica para eliminar el fantasma de la matriz
        fantasma.reaparecer()  # Puedes ajustar esta función según tu lógica de reaparición
    else:
        # Aquí puedes implementar la lógica para manejar la colisión cuando PacMan no puede comer al fantasma
        print(f"Pacman no puede comer al fantasma {fantasma.color}. ¡Huye Pacman!")


def puede_mover(x, y):
    return (
        0 <= x < columnas
        and 0 <= y < filas
        and tablero[y][x] != 0
        and not any(
            enemigo.posicion_x == x and enemigo.posicion_y == y for enemigo in enemigos
        )
    )
# Importar la clase Timer para programar eventos temporizados
from threading import Timer

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

        if (0 <= nuevo_x < columnas and 0 <= nuevo_y < filas and tablero[nuevo_y][nuevo_x] != 0
                and nuevo_x != pacman.posicion_x and nuevo_y != pacman.posicion_y):
            enemigo.posicion_x = nuevo_x
            enemigo.posicion_y = nuevo_y
# Bucle principal
while True:
    mover_enemigos()
    imprimir_matriz()

    # Verificar si el temporizador de ayuda está activado
    if pacman.tiempo_ayuda_activado:
        # Verificar si el temporizador ha expirado
        if not timer_ayuda.is_alive():
            pacman.tiempo_ayuda_activado = False
            # Reaparecer los fantasmas con colores aleatorios
            for enemigo in enemigos:
                enemigo.reaparecer()

    keyboard.read_event()