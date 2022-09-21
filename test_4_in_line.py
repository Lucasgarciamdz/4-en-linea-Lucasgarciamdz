import unittest
from unittest.mock import patch
from exceptions_4_in_line import *
from rules_4_in_line import FourInLine


class Test4InLine(unittest.TestCase):

    def setUp(self):
        with patch('random.randint', return_value=1):
            self.game = FourInLine()

    def test_initial_blank_board(self):
        self.assertEqual(
            self.game.board,
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]])

    def test_insert_chip(self):
        self.game.insert_chip(1)
        self.assertEqual(
            self.game.board,
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0]])
    


    def test_change_turns(self):
        first = self.game.player
        self.game.insert_chip(1)
        self.assertNotEqual(self.game.player, first)

    def test_overflow(self):
        with self.assertRaises(Overflow):
            self.game.insert_chip(9)

    def test_full_column(self):
        with self.assertRaises(FullColumn):
            for i in range(9):
                self.game.insert_chip(1)

    def test_column_winner(self):
        for i in range(3):
            self.game.insert_chip(1)
            self.game.insert_chip(2)
        self.game.insert_chip(1)
        self.assertEqual(self.game.winner, 1)

    def test_row_winner(self):
        list = [1, 1, 2, 1, 3, 1, 4]
        for item in list:
            self.game.insert_chip(item)
        self.assertEqual(self.game.winner, 1)

    def test_diagonal_winner(self):
        list = [1, 2, 2, 3, 1, 3, 3, 4, 4, 4, 4]
        for item in list:
            self.game.insert_chip(item)
        self.assertEqual(self.game.winner, 1)

    def test_left_diagonal_winner(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.game.insert_chip(6)
        self.assertEqual(self.game.winner, 1)

    def test_right_diagonal_winner(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.game.insert_chip(4)
        self.assertEqual(self.game.winner, 1)

    def test_no_winner(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 0, 1]
        ]
        self.game.insert_chip(1)
        self.assertNotEqual(self.game.winner, 1)

    def test_insert_chip_last_row(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.game.insert_chip(1)
        self.assertEqual(
            self.game.board,
            [[1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0]])

if __name__ == "__main__":
    unittest.main()