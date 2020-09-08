import sys

from Board import initBoard, getBoardFromConfig, displayBoard

playerConfig = sys.argv[1].split("=")[1]

with open("./config/" + playerConfig, 'r') as f:
    config = f.read().splitlines()

board = getBoardFromConfig(config)
displayBoard(board)
