import unittest
import os

from Board import initBoard, getBoardFromConfig

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
        
        # os.path.relpath('..\\subfldr1\\testfile.txt', os.path.dirname(__file__))
        # f = open("./config/player1", "r")
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
