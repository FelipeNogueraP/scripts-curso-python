import random
from random import randrange
import time
import os


def presentacion1():

    print("Triqui")
    print("    1. Facil")
    print("    2. Dificil")

    nivel = ""

    while nivel != "1" and nivel != "2":
        nivel = input("         -->   ")
    return int(nivel)


def presentacion2():

    print()
    print("    Triqui")
    print()
    print()
    print("    Inicia el PC")
    print("    elige O / X")
    print()
    print()
    print()

    ficha = " "
    while ficha != "O" and ficha != "X":
        ficha = input("        --> ").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador


def DisplayBoard(board):

    print("Triqui")
    print("    1       |2      |3")
    print("      {}    |   {}  |   {}".format(board[0], board[1], board[2]))
    print("            |       |")
    print("    --------+-------+----------")
    print("    4       |5      |6")
    print("      {}    |   {}  |   {}".format(board[3], board[4], board[5]))
    print("            |       |")
    print("    --------+-------+----------")
    print("    7       |8      |9")
    print("      {}    |   {}  |   {}".format(board[6], board[7], board[8]))
    print("            |       |")
    print()


def keepPlaying():
    print()
    answer = input("       Marca S, si quieres inentar de nuevo").lower()
    if answer == S or answer == "si":
        return True
    else:
        return False


def VictoryFor(board, jugador):
    if (
        board[0] == board[1] == board[2] == jugador
        or board[3] == board[4] == board[5] == jugador
        or board[6] == board[7] == board[8] == jugador
        or board[0] == board[3] == board[6] == jugador
        or board[1] == board[4] == board[7] == jugador
        or board[2] == board[5] == board[8] == jugador
        or board[0] == board[4] == board[8] == jugador
        or board[2] == board[4] == board[6] == jugador
    ):
        return True
    else:
        return False


def fullBoard(board):

    for i in board:
        if i == " ":
            return False
        else:
            return True


def MakeListOfFreeFields(board, casilla):

    return board[casilla] == " "


def EnterMove(board):

    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position = None
    while True:
        if position not in positions:
            position = input(" Tu turno, selecciona un numero del 1 al 9: ")
        else:
            position = int(position)
            if not MakeListOfFreeFields(board, position - 1):
                print("    Esta posición está ocupada, intenta de nuevo")
            else:
                return position - 1


def pcMove1(board, jugador):

    for i in range(9):
        copia = list(board)
        if MakeListOfFreeFields(copia, i):
            copia[i] = jugador
            if VictoryFor(copia, jugador):
                return i

    while True:
        casilla = random.randrange(10)
        if not MakeListOfFreeFields(board, casilla):
            casilla = randon.randrange(10)

        else:
            return casilla


def pcMove2(board, usuario, maquina):

    for i in range(9):
        copia = list(board)
        if MakeListOfFreeFields(copia, i):
            copia[i] = maquina
            if VictoryFor(copia, maquina):
                return i

    for i in range(9):
        copia = list(board)
        if MakeListOfFreeFields(copia, i):
            copia[i] = usuario
            if VictoryFor(copia, usuario):
                return i

    if ordenador == "X":
        if board[4] == " ":
            return 4
        esquinasvacias = []
        for i in [0, 2, 6, 8]:
            if MakeListOfFreeFields(board, i):
                esquinasvacias.append(i)
        demasvacias = []
        for i in [1, 3, 5, 7]:
            if MakeListOfFreeFields(board, i):
                demasvacias.append(i)
        if len(esquinasvacias) > 0:
            return random.choise(esquinasvacias)

        else:

            return random.choise(demasvacias)

    if ordenador == "O":
        contador = 0
        for i in range(9):
            if MakeListOfFreeFields(board, i):
                contador += 1
            if contador == 7:
                if board[4] == " ":
                    return 4

    while True:

        casilla = random.randint(0, 8)
        if not MakeListOfFreeFields(board, casilla):
            casilla = random.randint(0, 8)
        else:
            return casilla


playing = True

while playing:

    board = [" "] * 9
    os.system("cls")
    nivel = presentacion1()
    os.system("cls")
    humano, ordenador = presentacion2()
    os.system("cls")
    DisplayBoard(board)

    if humano == "O":
        turno = "humano"

    else:
        turno = "ordenador"

    partida = True

    while partida:
        if fullBoard(board):
            print("     Empate")
            partida = False

        elif turno == "humano":
            casilla = EnterMove(board)
            board[casilla] = humano
            turno = "ordenador"
            os.system("cls")
            DisplayBoard(board)
            if VictoryFor(board, humano):
                print("Has Ganado")
                partida = False

        elif turno == "ordenador":
            print("El Ordenador está pensando...")
            time.sleep(3)
            if nivel == 1:
                casilla = pcMove1(board, humano)

            elif nivel == 2:
                casilla = pcMove2(board, ordenador, humano)
            board[casilla] = ordenador
            turno = "humano"
            os.system("cls")
            DisplayBoard(board)
            if VictoryFor(board, ordenador):
                print("Has Perdido")
                partida = False

playing = keepPlaying()
