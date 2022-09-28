import unittest
from unittest.mock import patch
from exceptions_4_in_line import *
from rules_4_in_line import FourInLine
from cmd_4_in_line import main, print_board


class Test4InLine(unittest.TestCase):

    def setUp(self):
        with patch('random.randint', return_value=1):
            self.game = FourInLine()

    # def test_q_exit(self):
    #     with patch('builtins.input', return_value='q'):
    #         main()
            

if __name__ == '__main__':
    unittest.main()