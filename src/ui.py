import os
from Game import switchPlayer
from copy import deepcopy
from constants import UNICODE_FOR_A_CHAR, SQUARE_EMPTY, SQUARE_SUCCESS_SHOT, SQUARE_FAILED_SHOT, SQUARE_SHIP, PLAYER_1, PLAYER_2

def clear():
    os.system('clear')

def displayPlayerBoard(boards, player, hit):
    if (player == PLAYER_1 and not hit):
        clear()
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
        clear()
        displayFleetLife(PLAYER_1, boards)
        displayBoard(boards[PLAYER_1]["opponent"], "PLAYER 1'S TURN")
    elif player == PLAYER_2 and not hit:
        clear()
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")
        clear()
        displayFleetLife(PLAYER_2, boards)
        displayBoard(boards[PLAYER_2]["opponent"], "PLAYER 2'S TURN")

def displayBoard(board, title="BOARD"):
    print(title)
    print(' ', end='')

    # print header
    for x in range(len(board)):
        print(" " + str(x+1) + " ", end='')

    # ascii codes for displaying grid
    # upperleftcorner = u'\u2554'  
    # downT = u'\u2569'
    # T = u'\u2566'
    # F = u'\u2560'
    # line = u'\u2550'
    # cross = u'\u256c'

    print()

    for x in range(len(board)):
        # display letters using their unicode (starting form A)
        line = chr(x + UNICODE_FOR_A_CHAR)

        for i in range(len(board)):
            if board[x][i] == SQUARE_SHIP:
                line += " S "
            elif board[x][i] == SQUARE_FAILED_SHOT:
                line += " O "
            elif board[x][i] == SQUARE_SUCCESS_SHOT:
                line += " X "
            else:
                line += "   "

        print(line)

def displayShootResult(hit, boards, currentPlayer):
    clear()

    if (currentPlayer == PLAYER_1):
        displayFleetLife(PLAYER_2, boards)
        displayBoard(boards[PLAYER_1]["opponent"])
    else:
        displayFleetLife(PLAYER_2, boards)
        displayBoard(boards[PLAYER_2]["opponent"])

    if hit:
        print("Well done, you blew up some ship. Play again!")
    else:
        input("Too bad, you hit the water. Press enter to continue.")

def displayFleetLife(player, boards):
    print('YOUR FLEET LIFE: ' + str(boards[player]["life"]))
