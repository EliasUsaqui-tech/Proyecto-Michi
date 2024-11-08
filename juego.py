# juego.py

from tablero import crear_tablero, mostrar_tablero, verificar_ganador, tablero_lleno
from jugadores import jugar_jugador, jugar_computadora

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
            print(f"¡¡¡¡¡¡¡¡¡¡¡¡El jugador {jugador_actual} ha ganado!!!!!!!!!!!!")
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

# Iniciar el juego
if __name__ == "__main__":
    tic_tac_toe()
