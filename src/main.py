import sys
from random import randint
from Board import initBoard, getBoardFromConfig, displayBoard

# read configuration files from both players
player1ConfigFile = sys.argv[1].split("=")[1]
player2ConfigFile = sys.argv[2].split("=")[1]

with open("./config/" + player1ConfigFile, 'r') as f:
    player1Config = f.read().splitlines()

with open("./config/" + player2ConfigFile, 'r') as f:
    player2Config = f.read().splitlines()

# initialize the boards
player1PrimaryBoard = getBoardFromConfig(player1Config)
player1OpponentBoard = initBoard(10)

player2PrimaryBoard = getBoardFromConfig(player2Config)
player2OpponentBoard = initBoard(10)

# pick the first player randomly
currentPlayer = randint(1,2)

if (currentPlayer == 1):
    displayBoard(player1OpponentBoard, "OPPONENT")
    displayBoard(player1PrimaryBoard, "PLAYER 1")
else:
    displayBoard(player2OpponentBoard, "OPPONENT")
    displayBoard(player2PrimaryBoard, "PLAYER 2")
