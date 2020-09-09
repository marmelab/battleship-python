import sys
from Game import shoot, switchPlayer, initGame, gameIsWon
from utils import isValid
from Config import getPlayersConfig
import ui

config1, config2 = getPlayersConfig()

newGame = True

while newGame:

    boards, currentPlayer = initGame(config1, config2, 10)
    hit = False

    while not gameIsWon(boards):
        # Display current player board
        ui.displayPlayerBoard(boards, currentPlayer, hit)
        
        # Ask for a coordinate
        coord = input(currentPlayer + ", where do you want to fire ? ")
        while not isValid(coord):
            print("Sorry, this value is incorrect. Example of valid coordinates: A1")
            coord = input(currentPlayer + ", where do you want to fire ? ")

        # Launch a missile to that coordinate
        boards, hit = shoot(coord, boards, currentPlayer)

        # Display result
        ui.displayShootResult(hit, boards, currentPlayer)

        if not hit: 
            currentPlayer = switchPlayer(currentPlayer)

    ui.displayWinner(boards, currentPlayer)

    newGame = ui.queryYesNo("Do you want to start a new game?")
