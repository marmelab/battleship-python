import sys
from Game import shoot, switchPlayer, initGame, gameIsWon, startCountDown, stopCountDown
from utils import isValid
from Config import getPlayersConfig
from constants import PLAYER_1, PLAYER_2
import ui
import time

config1, config2 = getPlayersConfig()
        


newGame = True

while newGame:

    ui.displayLookAwayMsg(PLAYER_1)
    fleet1 = ui.askForPlayerFleet()

    ui.displayLookAwayMsg(PLAYER_2)
    fleet2 = ui.askForPlayerFleet()

    gameState, currentPlayer = initGame(fleet1, fleet2, 10)
    hit = False
    timeOver = False

    while not gameIsWon(gameState, currentPlayer) and not timeOver:

        if not hit:
            ui.displayLookAwayMsg(currentPlayer)

        turnStart = startCountDown()

        # Display current player board
        ui.displayPlayerBoard(gameState, currentPlayer, hit)
        
        # Ask for a coordinate
        print()
        coord = input(ui.getPlayerName(currentPlayer) + ", where do you want to fire (example: A1)? ")
        while not isValid(coord):
            print("Sorry, this value is incorrect. Example of valid coordinates: A1")
            print()
            coord = input(ui.getPlayerName(currentPlayer) + ", where do you want to fire (example: A1)?  ")

        # Launch a missile to that coordinate
        gameState, hit, shipSunk = shoot(coord, gameState, currentPlayer)

        gameState = stopCountDown(turnStart, currentPlayer, gameState)
        if gameState[currentPlayer]["time"] <= 0:
            timeOver = True
            break

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

    ui.displayWinner(gameState, currentPlayer, timeOver)

    newGame = ui.queryYesNo("Do you want to start a new game?")

print("Goodbye!")
