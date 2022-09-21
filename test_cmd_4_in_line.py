import unittest
from unittest.mock import patch
from exceptions_4_in_line import *
from rules_4_in_line import FourInLine


class Test4InLine(unittest.TestCase):

    def setUp(self):
        with patch('random.randint', return_value=1):
            self.game = FourInLine()


if __name__ == '__main__':
    unittest.main()