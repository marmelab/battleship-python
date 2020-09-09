import unittest
from constants import PLAYER_1, PLAYER_2
from Game import gameIsWon

class TestGameMethods(unittest.TestCase):

    def test_game_init(self):
        self.assertTrue(1)

    def test_game_is_not_won(self):

        boards = {
            PLAYER_1: {
                "life": 17
            },
            PLAYER_2: {
                "life": 17
            }
        }

        self.assertFalse(gameIsWon(boards))
    
    def test_game_is_won(self):

        boards = {
            PLAYER_1: {
                "life": 0
            },
            PLAYER_2: {
                "life": 17
            }
        }

        self.assertTrue(gameIsWon(boards))
