from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, updateBoardsAndHit, getShipsFromConfig
from random import randint
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE, SQUARE_SUCCESS_SHOT, GAME_TIME
from utils import getCoords
import time

def switchPlayer(currentPlayer):
    if currentPlayer == PLAYER_1:
        nextPlayer = PLAYER_2
    else:
        nextPlayer = PLAYER_1

    return nextPlayer

def initGame(config1, config2, size):
    gameState = {
        PLAYER_1: {
            "primary": getBoardFromConfig(config1),
            "opponent_board": initBoard(10),
            "life": FLEET_LIFE,
            "ships": getShipsFromConfig(config1),
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

    diff = stop - start

    newGameState = updatePlayerTimeLeft(diff, player, gameState)
    
    return newGameState

def updatePlayerTimeLeft(time, player, gameState):
    gameStateCopy = deepcopy(gameState)

    gameStateCopy[player]["time"] -= time

    return gameStateCopy
