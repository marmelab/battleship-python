from constants import UNICODE_FOR_A_CHAR, UNICODE_FOR_J_CHAR

def getCoords(coord):
    x = ord(coord[0]) - UNICODE_FOR_A_CHAR
    y = int(coord[1:]) - 1

    return x, y

def isValid(coord):
    return coord and ord(coord[0]) >= UNICODE_FOR_A_CHAR and ord(coord[0]) <= UNICODE_FOR_J_CHAR and int(coord[1:]) >= 1 and int(coord[1:]) <= 10
