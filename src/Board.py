from constants import UNICODE_FOR_A_CHAR

def initBoard(size):
    board = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        board.append(line)

    return board

def getBoardFromConfig(config, board):
    for shipCoords in config:
        coords = shipCoords.split(",")
        
        for coord in coords:
            x = ord(coord[0]) - UNICODE_FOR_A_CHAR
            y = int(coord[1]) - 1
            
            board[x][y] = 1

    return board
    
def displayBoard(board):
    print(' ', end='')

    # print header
    for x in range(len(board)):
        print(" " + str(x+1) + " ", end='')

    # ascii codes for displaying grid
    # upperleftcorner = u'\u2554'  
    # downT = u'\u2569'
    # T = u'\u2566'
    # F = u'\u2560'
    # line = u'\u2550'
    # cross = u'\u256c'

    print()

    for x in range(len(board)):
        # display letters using their unicode (starting form A)
        line = chr(x + UNICODE_FOR_A_CHAR)

        for i in range(len(board)):
            
            if board[x][i]:
                line += " X "
            else:
                line += "   "

        print(line)
