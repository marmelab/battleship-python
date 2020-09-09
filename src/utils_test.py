import unittest
import os

from utils import isValid

class TestUtilsMethods(unittest.TestCase):

    def test_valid_coord(self):
        self.assertTrue(isValid("A1"))
    
    def test_invalid_coord(self):
        self.assertFalse(isValid("K1"))
