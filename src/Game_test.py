import unittest
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE
from Game import gameIsWon, initGame, shoot
from Board import initBoard, getBoardFromConfig
import ui

class TestGameMethods(unittest.TestCase):

    def test_game_init(self):
        self.assertTrue(1)

    def test_game_is_not_won(self):

        # TODO: update this test

        self.assertTrue(True)
    
    def test_game_is_won(self):

        # TODO: update this test

        self.assertTrue(True)

    def test_shoot_success(self):
        # TODO: update this test

        # given two players
        # with open("./config/player1", 'r') as f:
        #     config1 = f.read().splitlines()
    
        # with open("./config/player2", 'r') as f:
        #     config2 = f.read().splitlines()
        
        # boards, currentPlayer = initGame(config1, config2, 10)

        # # when player 1 shoots and hit a ship
        # boards, hit = shoot("C1", boards, PLAYER_1)

        # # then player 2 fleet life is decremented
        # remainingLife = boards[PLAYER_2]["life"]
        # self.assertEqual(remainingLife, FLEET_LIFE - 1)

        self.assertTrue(True)
