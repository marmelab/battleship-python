import os
import sys
from Game import switchPlayer, gameIsWon, isShipPartHit
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

def displayPlayerBoard(boards, player, hit):
    clear()

    if (player == PLAYER_1):
        displayPlayerFleet(boards, PLAYER_1)
        print()
        displayBoard(boards[PLAYER_1]["opponent"], "PLAYER 1'S TURN")
    elif player == PLAYER_2:
        displayPlayerFleet(boards, PLAYER_2)
        print()
        displayBoard(boards[PLAYER_2]["opponent"], "PLAYER 2'S TURN")
    
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

    # print numbers header
    for x in range(len(board)):
        print("  " + str(x+1) + " ", end='')

    print()

    for x in range(len(board)):
        print("   ", end="")

        for i in range(len(board)):
            print("--- ", end="")
        
        print()

        # display letters using their unicode (starting form A)
        line = chr(x + UNICODE_FOR_A_CHAR) + " |"

        for i in range(len(board)):

            if board[x][i] == SQUARE_SHIP:
                line += " S "
            elif board[x][i] == SQUARE_FAILED_SHOT:
                line += " O |"
            elif board[x][i] == SQUARE_SUCCESS_SHOT:
                line += " X |"
            else:
                line += "   |"

        print(line)

    print("   ", end="")

    for i in range(len(board)):
        print("--- ", end="")

    print()

def displayFleetLife(player, boards):
    print('YOUR FLEET LIFE: ' + str(boards[player]["life"]))

def displayWinner(boards, player):
    print()
    print("You blew up your oppponent's fleet! Congratulations " + getPlayerName(player) + "!")
    print()

def getPlayerName(player):
    name = 'PLAYER'

    if player == PLAYER_1:
        name = 'PLAYER 1'
    else:
        name = 'PLAYER 2'

    return name

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
