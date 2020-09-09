import os
from Board import displayBoard
from Game import switchPlayer
from copy import deepcopy
from constants import PLAYER_1, PLAYER_2

def clear():
    os.system('clear')

def displayPlayerBoard(boards, player, hit):
    if (player == PLAYER_1 and not hit):
        clear()
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
        clear()
        displayBoard(boards["player1"]["opponent"], "PLAYER 1'S TURN")
    elif player == PLAYER_2 and not hit:
        clear()
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")
        clear()
        displayBoard(boards["player2"]["opponent"], "PLAYER 2'S TURN")

def displayShootResult(hit, boards, currentPlayer):
    clear()

    if (currentPlayer == PLAYER_1):
        displayBoard(boards["player1"]["opponent"])
    else:
        displayBoard(boards["player2"]["opponent"])

    if hit:
        print("Well done, you blew up some ship. Play again!")
    else:
        input("Too bad, you hit the water. Press enter to continue.")
