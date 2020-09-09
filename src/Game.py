from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, shoot
from random import randint
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE

def switchPlayer(currentPlayer):
    if currentPlayer == PLAYER_1:
        nextPlayer = PLAYER_2
    else:
        nextPlayer = PLAYER_1

    return nextPlayer

def initGame(config1, config2, size):
    player1Config, player2Config = getPlayersConfig()

    boards = {
        PLAYER_1: {
            "primary": getBoardFromConfig(player1Config),
            "opponent": initBoard(10),
            "life": FLEET_LIFE
        },
        PLAYER_2: {
            "primary": getBoardFromConfig(player2Config),
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

