import sys

playerConfig = sys.argv[1].split("=")[1]

f = open("./config/" + playerConfig, "r")
config = f.read().splitlines()
board = []

def initBoard(size):
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        board.append(line)

def getBoardFromConfig(config):
    for shipCoords in config:
        coords = shipCoords.split(",")
        
        for coord in coords:
            x = ord(coord[0]) - 65
            y = int(coord[1]) - 1
            
            board[x][y] = 1
    
def displayBoard(board):
    print(' ', end='')

    # print header
    for x in range(10):
        print(" " + str(x+1) + " ", end='')

    # upperleftcorner = u'\u2554'  
    # downT = u'\u2569'
    # T = u'\u2566'
    # F = u'\u2560'
    # line = u'\u2550'
    # cross = u'\u256c'

    print()
    # print(u'\u256c')

    # print(' ' + upperleftcorner)

    for x in range(10):

        # print(' ' + F)
        line = chr(x + 65)

        for i in range(10):
            
            if board[x][i]:
                line += " X "
            else:
                line += "   "

        print(line)

initBoard(10)
getBoardFromConfig(config)
displayBoard(board)