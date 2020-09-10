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

def getShipsFromConfig(config):
    ships = []

    for shipCoords in config:
        coords = shipCoords.split(",")
        shipCoords = []
        for coord in coords:
            shipCoords.append(coord)

        ships.append(shipCoords)

    return ships

def updateBoardsAndHit(coord, gameState, currentPlayer, opponentPlayer):
    gameStateCopy = deepcopy(gameState)
    hit = False

    if (shipFoundAt(coord, gameState[opponentPlayer]["primary"])):
        gameStateCopy[currentPlayer]["opponent_board"] = updateBoard(gameState[currentPlayer]["opponent_board"], coord, SQUARE_SUCCESS_SHOT)
        hit = True
    else:
        gameStateCopy[currentPlayer]["opponent_board"] = updateBoard(gameState[currentPlayer]["opponent_board"], coord, SQUARE_FAILED_SHOT)

    return gameStateCopy, hit

def shipFoundAt(coord, board):
    x, y = getCoords(coord)

    return board[x][y] == SQUARE_SHIP

def updateBoard(board, coord, newState):
    boardCopy = deepcopy(board)
    x, y = getCoords(coord)
    
    boardCopy[x][y] = newState

    return boardCopy
