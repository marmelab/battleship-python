from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, displayBoard, shoot
from random import randint

def switchPlayer(currentPlayer):
    if currentPlayer == 1:
        nextPlayer = 2
    else:
        nextPlayer = 1

    return nextPlayer

def initGame(config1, config2, size):
    player1Config, player2Config = getPlayersConfig()

    boards = {
        "player1": {
            "primary": getBoardFromConfig(player1Config),
            "opponent": initBoard(10),
        },
        "player2": {
            "primary": getBoardFromConfig(player2Config),
            "opponent": initBoard(10),
        }
    }

    # pick the first player randomly
    currentPlayer = randint(1,2)

    return boards, currentPlayer
