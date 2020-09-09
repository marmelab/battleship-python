from constants import UNICODE_FOR_A_CHAR, SQUARE_EMPTY, SQUARE_SUCCESS_SHOT, SQUARE_FAILED_SHOT, SQUARE_SHIP, PLAYER_1, PLAYER_2
from utils import getCoords
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

    if (currentPlayer == PLAYER_1):
        updatedBoards, hit = updateBoardsAndHit(coord, boards, PLAYER_1, PLAYER_2)
    else:
        updatedBoards, hit = updateBoardsAndHit(coord, boards, PLAYER_2, PLAYER_1)

    return updatedBoards, hit

def updateBoardsAndHit(coord, boards, currentPlayer, opponentPlayer):
    boardsCopy = deepcopy(boards)
    hit = 0

    if (shipFoundAt(coord, boards[opponentPlayer]["primary"])):
        boardsCopy[currentPlayer]["opponent"] = updateBoard(boards[currentPlayer]["opponent"], coord, SQUARE_SUCCESS_SHOT)
        hit = 1
    else:
        boardsCopy[currentPlayer]["opponent"] = updateBoard(boards[currentPlayer]["opponent"], coord, SQUARE_FAILED_SHOT)

    return boardsCopy, hit

def shipFoundAt(coord, board):
    x, y = getCoords(coord)

    return board[x][y] == SQUARE_SHIP

def updateBoard(board, coord, newState):
    boardCopy = deepcopy(board)
    x, y = getCoords(coord)
    
    boardCopy[x][y] = newState

    return boardCopy
