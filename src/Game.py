from copy import deepcopy
from Config import getPlayersConfig
from Board import initBoard, getBoardFromConfig, displayBoard, shoot
from random import randint

# TODO: remove currentPlayer and hit from the structure and use variables in the main instead
boards = {
  "player1": {
    "primary": [],
    "opponent": [],
  },
  "player2": {
    "primary": [],
    "opponent": [],
  },
  "currentPlayer": 0,
}

def getPrimaryBoard(player):
    return boards[player]["primary"];

def getOpponentBoard(player):
    return boards[player]["opponent"];

def switchPlayer(boards):
    boardsCopy = deepcopy(boards)
    if boards["currentPlayer"] == 1:
        boardsCopy["currentPlayer"] = 2
    else:
        boardsCopy["currentPlayer"] = 1

    return boardsCopy

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
        },
        "currentPlayer": 0,
    }

    # pick the first player randomly
    boards["currentPlayer"] = randint(1,2)
    # currentPlayer = randint(1,2)

    return boards, boards["currentPlayer"]
