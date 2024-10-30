def imprimir_tablero_cuadrado(tablero):
    print("┌─────┬─────┬─────┐")
    print(f"│  {tablero[0]}  │  {tablero[1]}  │  {tablero[2]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {tablero[3]}  │  {tablero[4]}  │  {tablero[5]}  │")
    print("├─────┼─────┼─────┤")
    print(f"│  {tablero[6]}  │  {tablero[7]}  │  {tablero[8]}  │")
    print("└─────┴─────┴─────┘")

# Inicializar el tablero vacío
tablero = [" " for _ in range(9)]
imprimir_tablero_cuadrado(tablero)
