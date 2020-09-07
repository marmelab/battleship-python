import sys

playerConfig = sys.argv[1].split("=")[1]

f = open("./config/" + playerConfig, "r")
config = f.read().splitlines()
board = []

# init board
for i in range(10):
    line = []
    for j in range(10):
        line.append(0)
    board.append(line)

# setup ships
for shipCoords in config:
    coords = shipCoords.split(",")
    
    for coord in coords:
        x = ord(coord[0]) - 65
        y = int(coord[1]) - 1
        
        # print(coord + "=>" + str(x) + "-" + str(y))
        
        board[x][y] = 1
        
# print header
# for i in range(10):
#     for j in range(10):
#         board.append(0)

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

    


# for line in f:
#     print(line)

""" for line in f:
    for x in range(len(board)):
        for y in range(len(board[x])):
            symbol = get_symbol(board[x][y])
            tile_text = f'\t[{symbol}]'
            if (x, y) in movables:
                tile_text = f'{tile_text}({movables.index((x, y)) + 1})'
            if (x, y) == selected:
                tile_text = f'\033[5m{tile_text}\033[0m'
            print(f'{tile_text}', end='\t')
        print('\n')
    print('') """