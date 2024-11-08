import random

def jugar_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila: "))
            col = int(input(f"Jugador {jugador}, ingresa la columna: "))
            if tablero[fila][col] == ' ':
                tablero[fila][col] = jugador
                break
            else:
                print("Esa posición ya está ocupada, elige otra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Intenta nuevamente.")

def jugar_computadora(tablero, jugador):
    n = len(tablero)
    while True:
        fila, col = random.randint(0, n - 1), random.randint(0, n - 1)
        if tablero[fila][col] == ' ':
            tablero[fila][col] = jugador
            print(f"La computadora ha jugado en ({fila}, {col})")
            break
