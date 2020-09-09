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
    # Display current player board
    ui.displayPlayerBoard(boards, currentPlayer, hit)
    
    # Ask for a coordinate
    coord = input("Player " + str(currentPlayer) + ", where do you want to fire ?")
    while not isValid(coord):
        print("Sorry, this value is incorrect. Example of valid coordinates: A1")
        coord = input("Player " + str(currentPlayer) + ", where do you want to fire ?")

    # Launch a missile to that coordinate
    boards, hit = shoot(coord, boards, currentPlayer)

    # Display result and get switch player if the shoot missed
    currentPlayer = ui.displayShootResult(hit, boards, currentPlayer)
