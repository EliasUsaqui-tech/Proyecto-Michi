# tablero.py

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
