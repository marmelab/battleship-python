import sys

from methods import initBoard, getBoardFromConfig, displayBoard

playerConfig = sys.argv[1].split("=")[1]

f = open("./config/" + playerConfig, "r")
config = f.read().splitlines()

board = initBoard(10)
board = getBoardFromConfig(config, board)
displayBoard(board)