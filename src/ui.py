import os
import sys
from Game import switchPlayer, gameIsWon, isShipPartHit, getOpponent
from copy import deepcopy
from constants import UNICODE_FOR_A_CHAR, SQUARE_EMPTY, SQUARE_SUCCESS_SHOT, SQUARE_FAILED_SHOT, SQUARE_SHIP, PLAYER_1, PLAYER_2

def clear():
    os.system('clear')

def displayPlayerFleet(boards, player):
    print("MY FLEET STATE")
    
    for ship in boards[player]["ships"]:
        displayShip(ship, boards, player)

def displayLookAwayMsg(player):
    clear()
    if (player == PLAYER_1):
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
    elif player == PLAYER_2:
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")

def displayPlayerBoard(gameState, player, hit):
    clear()

    displayPlayerFleet(gameState, player)
    print()

    timeLeft = f' ({gameState[player]["time"]} seconds left)'
    displayBoard(gameState[player]["opponent_board"], getPlayerName(player) + "'S TURN" + timeLeft)
    
def displayShip(ship, boards, player):
    for shipPart in ship:
        line = ""
        if (isShipPartHit(shipPart, boards, player)):
            line += "[X]"
        else:
            line += "[ ]"

        print(line, end = " ")

    print()

def displayBoard(board, title="BOARD"):
    print(title)
    print('  ', end='')

    # numbers header
    for x in range(len(board)):
        print("  " + str(x+1) + " ", end='')

    print()

    # upper left corner
    print("  " + u'\u250c', end="")

    # top border
    for x in range(len(board)):
        if x < len(board) - 1:
            print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u252c', end="")
        else:
            print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u2510')

    for x in range(len(board)):

        # line separator between letters (after A)
        if x > 0:
            print("  ", end="")

            print(u'\u251c', end="")
            
            for i in range(len(board)):
                if i < len(board) - 1:
                    print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u253c', end="")
                else:
                    print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u2524', end="")
            
            print()
        
        # display letters using their unicode (starting form A)
        line = chr(x + UNICODE_FOR_A_CHAR) + " " + u'\u2502'

        for i in range(len(board)):

            if board[x][i] == SQUARE_SHIP:
                line += " S "
            elif board[x][i] == SQUARE_FAILED_SHOT:
                line += " O " + u'\u2502'
            elif board[x][i] == SQUARE_SUCCESS_SHOT:
                line += " X " + u'\u2502'
            else:
                line += "   " + u'\u2502'

        print(line)

    print("  ", end="")

    print(u'\u2514', end="")

    # border bottom
    for i in range(len(board)):
        if i < len(board) - 1:
            print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u2534' , end="")
        else:
            print(u'\u2500' + u'\u2500' + u'\u2500' + u'\u2518' , end="")

    print()

def displayFleetLife(player, boards):
    print('YOUR FLEET LIFE: ' + str(boards[player]["life"]))

def displayWinner(boards, player, timeOver):
    print()
    if timeOver:
        print("TIME'S OVER! " + getPlayerName(getOpponent(player)) + " won this game.")
    else:
        print("You blew up your oppponent's fleet! Congratulations " + getPlayerName(player) + "!")
    print()

def getPlayerName(player):
    if player == PLAYER_1:
        return 'PLAYER 1'
    else:
        return 'PLAYER 2'

def queryYesNo(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
