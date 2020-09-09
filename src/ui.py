import os
from Board import displayBoard

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
