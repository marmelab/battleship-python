import sys

def getPlayersConfig():
    player1ConfigFile = sys.argv[1].split("=")[1]
    player2ConfigFile = sys.argv[2].split("=")[1]

    with open("./config/" + player1ConfigFile, 'r') as f:
        player1Config = f.read().splitlines()
    
    with open("./config/" + player2ConfigFile, 'r') as f:
        player2Config = f.read().splitlines()
    
    return player1Config, player2Config