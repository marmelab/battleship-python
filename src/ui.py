import os
from Board import displayBoard
from Game import switchPlayer
from copy import deepcopy

def clear():
    os.system('clear')

def displayPlayerBoard(boards, player, hit):
    if (player == 1 and not hit):
        clear()
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
        clear()
        displayBoard(boards["player1"]["opponent"], "PLAYER 1'S TURN")
        # displayBoard(boards["player1"]["primary"], "PLAYER 1")
    elif player == 2 and not hit:
        clear()
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")
        clear()
        displayBoard(boards["player2"]["opponent"], "PLAYER 2'S TURN")

def displayShootResult(hit, boards, currentPlayer):
    nextPlayer = deepcopy(currentPlayer)

    clear()

    if (currentPlayer == 1):
        displayBoard(boards["player1"]["opponent"])
    else:
        displayBoard(boards["player2"]["opponent"])

    if hit:
        print("Well done, you blew up some ship. Play again!")
    else:
        nextPlayer = switchPlayer(currentPlayer)
        input("Too bad, you hit the water. Press enter to continue.")
    
    return nextPlayer
