import sys
from Game import shoot, switchPlayer, initGame, gameIsWon
from utils import isValid
from Config import getPlayersConfig
import ui

config1, config2 = getPlayersConfig()

newGame = True

while newGame:

    gameState, currentPlayer = initGame(config1, config2, 10)
    hit = False

    while not gameIsWon(gameState, currentPlayer):

        if not hit:
            ui.displayLookAwayMsg(currentPlayer)

        # Display current player board
        ui.displayPlayerBoard(gameState, currentPlayer, hit)
        
        # Ask for a coordinate
        print()
        coord = input(currentPlayer + ", where do you want to fire (example: A1)? ")
        while not isValid(coord):
            print("Sorry, this value is incorrect. Example of valid coordinates: A1")
            print()
            coord = input(currentPlayer + ", where do you want to fire (example: A1)?  ")

        # Launch a missile to that coordinate
        gameState, hit, shipSunk = shoot(coord, gameState, currentPlayer)

        # Display result
        ui.displayPlayerBoard(gameState, currentPlayer, hit)

        if gameIsWon(gameState, currentPlayer):
            break
        
        print()

        if shipSunk:
            input("Well done, you blew up an ENTIRE ship. Press enter to play again!")
        elif hit:
            input("Nice, you hit a ship. Press enter to play again!")
        else:
            input("Too bad, you hit the water. Press enter to continue.")
            currentPlayer = switchPlayer(currentPlayer)

    ui.displayWinner(gameState, currentPlayer)

    newGame = ui.queryYesNo("Do you want to start a new game?")
