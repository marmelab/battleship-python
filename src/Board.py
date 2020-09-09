from constants import UNICODE_FOR_A_CHAR, SQUARE_EMPTY, SQUARE_SUCCESS_SHOT, SQUARE_FAILED_SHOT, SQUARE_SHIP
from utils import getX, getY
from copy import deepcopy
import os

def initBoard(size):
    board = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        board.append(line)

    return board

def getBoardFromConfig(config):
    board = initBoard(10)

    for shipCoords in config:
        coords = shipCoords.split(",")
        for coord in coords:
            x = ord(coord[0]) - UNICODE_FOR_A_CHAR
            y = int(coord[1]) - 1
            
            board[x][y] = 1

    return board
    
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

def shoot(coord, boards, currentPlayer):
    boardsCopy = deepcopy(boards)
    hit = 0

    if (currentPlayer == 1):
        if (shipAt(coord, boards["player2"]["primary"])):
            boardsCopy["player1"]["opponent"] = updateBoard(boards["player1"]["opponent"], coord, SQUARE_SUCCESS_SHOT)
            hit = 1
        else:
            boardsCopy["player1"]["opponent"] = updateBoard(boards["player1"]["opponent"], coord, SQUARE_FAILED_SHOT)
    else:
        if (shipAt(coord, boards["player1"]["primary"])):
            boardsCopy["player2"]["opponent"] = updateBoard(boards["player2"]["opponent"], coord, SQUARE_SUCCESS_SHOT)
            hit = 1
        else:
            boardsCopy["player2"]["opponent"] = updateBoard(boards["player2"]["opponent"], coord, SQUARE_FAILED_SHOT)

    return boardsCopy, hit


def shipAt(coord, board):
    x = getX(coord)
    y = getY(coord)
    
    return board[x][y] == SQUARE_SHIP

def updateBoard(board, coord, newState):
    boardCopy = deepcopy(board)
    x = getX(coord)
    y = getY(coord)
    
    boardCopy[x][y] = newState

    return boardCopy
