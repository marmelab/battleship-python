from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, updateBoardsAndHit
from random import randint
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE

def switchPlayer(currentPlayer):
    if currentPlayer == PLAYER_1:
        nextPlayer = PLAYER_2
    else:
        nextPlayer = PLAYER_1

    return nextPlayer

def initGame(config1, config2, size):
    boards = {
        PLAYER_1: {
            "primary": getBoardFromConfig(config1),
            "opponent": initBoard(10),
            "life": FLEET_LIFE
        },
        PLAYER_2: {
            "primary": getBoardFromConfig(config2),
            "opponent": initBoard(10),
            "life": FLEET_LIFE
        }
    }

    # pick the first player randomly
    if randint(1,2) == 1:
        currentPlayer = PLAYER_1
    else:
        currentPlayer = PLAYER_2

    return boards, currentPlayer

def decrementTargetFleetLife(boards, attacker):
    boardsCopy = deepcopy(boards)

    if attacker == PLAYER_1:
        boardsCopy[PLAYER_2]["life"] -= 1
    else:
        boardsCopy[PLAYER_1]["life"] -= 1

    return boardsCopy

def gameIsWon(boards):
    return boards[PLAYER_1]["life"] <= 0 or boards[PLAYER_2]["life"] <= 0

def shoot(coord, boards, currentPlayer):

    if (currentPlayer == PLAYER_1):
        updatedBoards, hit = updateBoardsAndHit(coord, boards, PLAYER_1, PLAYER_2)
    else:
        updatedBoards, hit = updateBoardsAndHit(coord, boards, PLAYER_2, PLAYER_1)

    if hit:
        updatedBoards = decrementTargetFleetLife(updatedBoards, currentPlayer)

    return updatedBoards, hit
