import unittest
import os

from Board import initBoard, getBoardFromConfig
from constants import PLAYER_1, PLAYER_2, FLEET_LIFE
import ui

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), '../config/player1')

class TestMainMethods(unittest.TestCase):

    def test_init_board(self):
    
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(initBoard(5), board)

    def test_board_config(self):
        with open("./config/player1", 'r') as f:
            config = f.read().splitlines()

        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
        ]

        self.assertEqual(getBoardFromConfig(config), board)
