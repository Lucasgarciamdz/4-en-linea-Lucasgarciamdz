import unittest
from unittest.mock import patch
from exceptions_4_in_line import Overflow
from exceptions_4_in_line import FullColumn
from rules_4_in_line import FourInLine
from parameterized import parameterized


class Test4InLine(unittest.TestCase):

    def setUp(self):
        with patch('random.choice', return_value=1):
            self.game = FourInLine()

    @parameterized.expand([
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
        (8, 1),
    ])
    def test_insert_chip(self, column, expected):
        self.game.insert_chip(column)
        self.assertEqual(self.game.board[7][column - 1], expected)

    @parameterized.expand([
        (9, Overflow),
        (0, Overflow),
        (-1, Overflow),
    ])
    def test_insert_chip_overflow(self, column, expected):
        with self.assertRaises(expected):
            self.game.insert_chip(column)

    @parameterized.expand([
        (1, FullColumn),
        (2, FullColumn),
        (3, FullColumn),
        (4, FullColumn),
        (5, FullColumn),
        (6, FullColumn),
        (7, FullColumn),
        (8, FullColumn),
    ])
    def test_insert_chip_full_column(self, column, expected):
        for i in range(8):
            self.game.insert_chip(column)
        with self.assertRaises(expected):
            self.game.insert_chip(column)

    def test_change_player(self):
        self.game.change_player()
        self.assertEqual(self.game.player, 2)

    def test_is_full(self):
        for i in range(8):
            for j in range(8):
                self.game.board[i][j] = 1
        self.assertTrue(self.game.is_full())

    def test_is_full2(self):
        for i in range(8):
            for j in range(8):
                self.game.board[i][j] = 1
        self.game.board[0][0] = 0
        self.assertFalse(self.game.is_full())

    def test_initial_blank_board(self):
        self.assertEqual(self.game.board,
                         [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])

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
        self.game.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.game.insert_chip(6)
        self.assertEqual(self.game.winner, 1)

    def test_right_diagonal_winner(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.game.insert_chip(4)
        self.assertEqual(self.game.winner, 1)

    def test_no_winner(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1, 0, 1]]
        self.game.insert_chip(1)
        self.assertNotEqual(self.game.winner, 1)

    def test_insert_chip_last_row(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
        self.game.insert_chip(1)
        self.assertEqual(self.game.board,
                         [[1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])

    def test_is_not_full(self):
        self.game.board = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.game.is_full())


if __name__ == "__main__":
    unittest.main()
