from copy import deepcopy

boards =	{
  "player1": {
    "primary": [],
    "opponent": [],
  },
  "player2": {
    "primary": [],
    "opponent": [],
  },
  "currentPlayer": 0,
  "hit": 0
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
