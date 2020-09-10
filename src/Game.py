from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, updateBoardsAndHit, getShipsFromConfig
from random import randint
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE, SQUARE_SUCCESS_SHOT
from utils import getCoords

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
            "opponent": initBoard(10),
            "life": FLEET_LIFE,
            "ships": getShipsFromConfig(config1)
        },
        PLAYER_2: {
            "primary": getBoardFromConfig(config2),
            "opponent": initBoard(10),
            "life": FLEET_LIFE,
            "ships": getShipsFromConfig(config2)
        }
    }

    # pick the first player randomly
    if randint(1,2) == 1:
        currentPlayer = PLAYER_1
    else:
        currentPlayer = PLAYER_2

    return gameState, currentPlayer

def decrementTargetFleetLife(boards, attacker):
    boardsCopy = deepcopy(boards)

    if attacker == PLAYER_1:
        boardsCopy[PLAYER_2]["life"] -= 1
    else:
        boardsCopy[PLAYER_1]["life"] -= 1

    return boardsCopy

def gameIsWon(boards, player):
    gameIsWon = True

    # check all of the ships coords on the board and look if it contains SUCCESS
    for ship in boards[playerOpponent(player)]["ships"]:
        for coord in ship:
            if not isShipPartHit(coord, boards, playerOpponent(player)):
                gameIsWon = False
                break

    return gameIsWon

def playerOpponent(player):
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
        if currentPlayer == PLAYER_1:
            ships = gameState[PLAYER_2]["ships"]
        else:
            ships = gameState[PLAYER_1]["ships"]

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
            if updatedGameState[currentPlayer]["opponent"][x][y] != SQUARE_SUCCESS_SHOT:
                shipSunk = False
                break

        updatedGameState = decrementTargetFleetLife(updatedGameState, currentPlayer)

    return updatedGameState, hit, shipSunk

def isShipPartHit(shipPart, boards, player):
    x, y = getCoords(shipPart)

    if player == PLAYER_1:
        if boards[PLAYER_2]["opponent"][x][y] == SQUARE_SUCCESS_SHOT:
            return True    
    else:
        if boards[PLAYER_1]["opponent"][x][y] == SQUARE_SUCCESS_SHOT:
            return True

    return False
