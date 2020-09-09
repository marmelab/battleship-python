import sys
from Board import shoot
from Game import switchPlayer, initGame, decrementTargetFleetLife, gameIsWon
from utils import isValid
from Config import getPlayersConfig
import ui

config1, config2 = getPlayersConfig()

boards, currentPlayer = initGame(config1, config2, 10)
hit = 0

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

    # Decrement target's fleet life if hit or switch player
    if hit:
        boards = decrementTargetFleetLife(boards, currentPlayer)
    else: 
        currentPlayer = switchPlayer(currentPlayer)

ui.displayWinner(boards, currentPlayer)
