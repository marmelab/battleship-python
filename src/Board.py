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

def updateBoardsAndHit(coord, boards, currentPlayer, opponentPlayer):
    boardsCopy = deepcopy(boards)
    hit = False

    if (shipFoundAt(coord, boards[opponentPlayer]["primary"])):
        boardsCopy[currentPlayer]["opponent"] = updateBoard(boards[currentPlayer]["opponent"], coord, SQUARE_SUCCESS_SHOT)
        hit = True
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
