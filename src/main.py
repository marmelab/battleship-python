import sys
import os
from Board import initBoard, getBoardFromConfig, displayBoard, shoot
from constants import UNICODE_FOR_A_CHAR
from Game import boards, getPrimaryBoard, getOpponentBoard, switchPlayer, initGame
from utils import isValid
from Config import getPlayersConfig

config1, config2 = getPlayersConfig()

boards, currentPlayer = initGame(config1, config2, 10)
hit = 0

while True:
    # TODO: extract this to a function like displayCurrentPlayerBoard
    if (boards["currentPlayer"] == 1 and not hit):
        os.system('clear')
        input("PLAYER 2, look away. PLAYER 1, press enter when ready")
        os.system('clear')
        displayBoard(boards["player1"]["opponent"], "PLAYER 1'S TURN")
        # displayBoard(boards["player1"]["primary"], "PLAYER 1")
    elif boards["currentPlayer"] == 2 and not hit:
        os.system('clear')
        input("PLAYER 1, look away. PLAYER 2, press enter when ready")
        os.system('clear')
        displayBoard(boards["player2"]["opponent"], "PLAYER 2'S TURN")


    while True:
        coord = input("Player " + str(boards["currentPlayer"]) + ", where do you want to fire ?")
        if isValid(coord):
            break
        print("Sorry, this value is incorrect. Example of valid coordinates: A1")

    boards, hit = shoot(coord, boards)

    # TODO: extract this to allow switching libs
    os.system('clear')

    if (boards["currentPlayer"] == 1):
        displayBoard(boards["player1"]["opponent"])
    else:
        displayBoard(boards["player2"]["opponent"])

    if hit:
        print("Well done, you blew up some ship. Play again!")
    else:
        boards = switchPlayer(boards)
        input("Too bad, you hit the water. Press enter to continue.")
