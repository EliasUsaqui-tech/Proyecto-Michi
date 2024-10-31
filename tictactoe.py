import random

def crear_tablero(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

def mostrar_tablero(tablero):
    n = len(tablero)
    if n == 3 or n == 4:
        print("  ┌" + "─────┬" * (n - 1) + "─────┐")
        for i, fila in enumerate(tablero):
            print("  │  " + "  │  ".join(fila) + "  │")
            if i < n - 1:
                print("  ├" + "─────┼" * (n - 1) + "─────┤")
        print("  └" + "─────┴" * (n - 1) + "─────┘")

def verificar_ganador(tablero, jugador):
    n = len(tablero)

    # Verificar filas y columnas
    for i in range(n):
        if all(tablero[i][j] == jugador for j in range(n)) or all(tablero[j][i] == jugador for j in range(n)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(n)) or all(tablero[i][n - 1 - i] == jugador for i in range(n)):
        return True

    return False

def tablero_lleno(tablero):
    return all(celda != ' ' for fila in tablero for celda in fila)

def jugar_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila: ")) - 1
            col = int(input(f"Jugador {jugador}, ingresa la columna: ")) - 1
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
            print(f"La computadora ha jugado en ({fila + 1}, {col + 1})")
            break

def tic_tac_toe():
    while True:
        try:
            n = int(input("Elige el tamaño del tablero (3 o 4): "))
            if n in (3, 4):
                break
            else:
                print("El tamaño debe ser 3 o 4.")
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")

    tablero = crear_tablero(n)
    modo = input("¿Jugar contra la computadora (1) o contra otra persona (2)? Ingresa 1 o 2: ")
    jugador_actual = 'X'

    while True:
        mostrar_tablero(tablero)
        if modo == '2' or (modo == '1' and jugador_actual == 'X'):
            jugar_jugador(tablero, jugador_actual)
        else:
            jugar_computadora(tablero, jugador_actual)

        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

# Iniciar el juego
tic_tac_toe()




