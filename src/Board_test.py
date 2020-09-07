import unittest

from Board import initBoard

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