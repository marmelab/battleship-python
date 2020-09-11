from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, updateBoardsAndHit, getShipsFromConfig
from random import randint
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE, SQUARE_SUCCESS_SHOT, GAME_TIME, UNICODE_FOR_A_CHAR
from utils import getCoords
import time
import os

def switchPlayer(currentPlayer):
    if currentPlayer == PLAYER_1:
        nextPlayer = PLAYER_2
    else:
        nextPlayer = PLAYER_1

    return nextPlayer

def initGame(config1, config2, size):
    # 1 - ask 5 times a start coordinate, a length and an orientation
    os.system('clear')

    # f = open("custom1", "w")
    # f.write("Hello")
    board = initBoard(size)
    playerShips = []

    for i in range(2):
        position = input(str(i + 1) + " => position the boat (B1,2,H) ")

        position = position.split(",")

        coord = position[0]
        length = int(position[1])
        orientation = position[2]
        
        letter = coord[0]
        column = coord[1:]

        shipCoords = []

        if (orientation == "H"):
            for i in range(int(column), length + 1):
                shipCoords.append(letter + str(i))

        else:
            for i in range(ord(letter), ord(letter) + length):
                shipCoords.append(chr(i) + column)

        print(shipCoords)
        playerShips.append(shipCoords)

        for coord in shipCoords:
            x = ord(coord[0]) - UNICODE_FOR_A_CHAR
            y = int(coord[1:]) - 1
            
            board[x][y] = 1

    input()

    # f.close()

    gameState = {
        PLAYER_1: {
            "primary": board,
            "opponent_board": initBoard(10),
            "life": FLEET_LIFE,
            "ships": playerShips,
            "time": GAME_TIME
        },
        PLAYER_2: {
            "primary": getBoardFromConfig(config2),
            "opponent_board": initBoard(10),
            "life": FLEET_LIFE,
            "ships": getShipsFromConfig(config2),
            "time": GAME_TIME
        }
    }

    # pick the first player randomly
    if randint(1,2) == 1:
        currentPlayer = PLAYER_1
    else:
        currentPlayer = PLAYER_2

    return gameState, currentPlayer

def gameIsWon(boards, player):
    # check all of the ships coords on the board and look if it contains SUCCESS
    for ship in boards[getOpponent(player)]["ships"]:
        for coord in ship:
            if not isShipPartHit(coord, boards, getOpponent(player)):
                return False

    return True

def getOpponent(player):
    if player == PLAYER_1:
        return PLAYER_2
    else:
        return PLAYER_1

def shoot(coord, gameState, currentPlayer):

    if (currentPlayer == PLAYER_1):
        updatedGameState, hit = updateBoardsAndHit(coord, gameState, PLAYER_1, PLAYER_2)
    else:
        updatedGameState, hit = updateBoardsAndHit(coord, gameState, PLAYER_2, PLAYER_1)

    shipSunk = False

    if hit:
        # check entire ship:
        # 1 find ship line in opponent ships
        ships = gameState[getOpponent(currentPlayer)]["ships"]

        shipLine = []

        for ship in ships:
            for partCoord in ship:
                if partCoord == coord:
                    shipLine = ship
                    break

        # 2 check each coord of the ship with isShipPartHit
        shipSunk = True

        for i in shipLine:
            x, y = getCoords(i)
            if updatedGameState[currentPlayer]["opponent_board"][x][y] != SQUARE_SUCCESS_SHOT:
                shipSunk = False
                break

    return updatedGameState, hit, shipSunk

def isShipPartHit(shipPart, gameState, player):
    board = getOpponentBoard(player, gameState)
    x, y = getCoords(shipPart)

    if board[x][y] == SQUARE_SUCCESS_SHOT:
        return True

    return False

def getOpponentBoard(player, gameState):
    return gameState[getOpponent(player)]["opponent_board"]

def startCountDown():
    return time.perf_counter()

def stopCountDown(start, player, gameState):
    stop = time.perf_counter()

    diff = int(round(stop - start))

    newGameState = updatePlayerTimeLeft(diff, player, gameState)
    
    return newGameState

def updatePlayerTimeLeft(time, player, gameState):
    gameStateCopy = deepcopy(gameState)

    gameStateCopy[player]["time"] -= time

    return gameStateCopy
