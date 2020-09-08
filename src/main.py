import sys
import os
from random import randint
from Board import initBoard, getBoardFromConfig, displayBoard, shoot
from constants import UNICODE_FOR_A_CHAR
from Game import boards, getPrimaryBoard, getOpponentBoard, switchPlayer
from utils import isValid
from Config import getPlayersConfig


player1Config, player2Config = getPlayersConfig()

# initialize the boards
boards["player1"]["primary"] = getBoardFromConfig(player1Config)
boards["player1"]["opponent"] = initBoard(10)

boards["player2"]["primary"] = getBoardFromConfig(player2Config)
boards["player2"]["opponent"] = initBoard(10)

# pick the first player randomly
boards["currentPlayer"] = randint(1,2)

while True:
    if (boards["currentPlayer"] == 1 and boards["hit"] == 0):
        os.system('clear')
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
        os.system('clear')
        displayBoard(boards["player1"]["opponent"], "PLAYER 1'S TURN")
        # displayBoard(boards["player1"]["primary"], "PLAYER 1")
    elif boards["currentPlayer"] == 2 and boards["hit"] == 0:
        os.system('clear')
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")
        os.system('clear')
        displayBoard(boards["player2"]["opponent"], "PLAYER 2'S TURN")


    while True:
        coord = input("Player " + str(boards["currentPlayer"]) + ", where do you want to fire ?")
        if isValid(coord):
            break
        print("Sorry, this value is incorrect. Example of valid coordinates: A1")

    boards = shoot(coord, boards)

    os.system('clear')

    if (boards["currentPlayer"] == 1):
        displayBoard(boards["player1"]["opponent"])
    else:
        displayBoard(boards["player2"]["opponent"])

    if boards["hit"] == 1:
        print("Well done, you blew up some ship. Play again!")
    else:
        boards = switchPlayer(boards)
        input("Too bad, you hit the water. Press enter to continue.")
