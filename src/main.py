import sys
import os
from Board import initBoard, getBoardFromConfig, displayBoard, shoot
from constants import UNICODE_FOR_A_CHAR
from Game import switchPlayer, initGame
from utils import isValid
from Config import getPlayersConfig
import ui

config1, config2 = getPlayersConfig()

boards, currentPlayer = initGame(config1, config2, 10)
hit = 0

while True:
    ui.displayPlayerBoard(boards, currentPlayer, hit)
    
    coord = input("Player " + str(currentPlayer) + ", where do you want to fire ?")

    while not isValid(coord):
        print("Sorry, this value is incorrect. Example of valid coordinates: A1")
        coord = input("Player " + str(currentPlayer) + ", where do you want to fire ?")

    boards, hit = shoot(coord, boards, currentPlayer)

    ui.clear()

    if (currentPlayer == 1):
        displayBoard(boards["player1"]["opponent"])
    else:
        displayBoard(boards["player2"]["opponent"])

    if hit:
        print("Well done, you blew up some ship. Play again!")
    else:
        currentPlayer = switchPlayer(currentPlayer)
        input("Too bad, you hit the water. Press enter to continue.")
