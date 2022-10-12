import unittest
from unittest.mock import patch
from cmd_4_in_line import main


@patch('random.choice', return_value=1)
@patch("builtins.print")
@patch("builtins.input")
class Test4InLine(unittest.TestCase):

    def test_q_exit(self, patched_input, patched_print, *args):
        patched_input.return_value = "q"
        main()
        self.assertEqual(patched_print.call_count, 11)
        patched_input.assert_called_once()

    def test_1_wins(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "2", "1", "2", "1", "2", "1"]
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0],
                         "Player 1 wins!")

    def test_valuerror(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["a", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[11][0][0],
                         "You must enter a number")
        patched_input.return_value = "q"

    def test_overflow(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["9", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[11][0][0], "Overflow")

    def test_full_column(self, patched_input, patched_print, *args):
        patched_input.side_effect = [
            "1", "1", "1", "1", "1", "1", "1", "1", "1", "q"
        ]
        main()
        self.assertEqual(patched_print.call_args_list[99][0][0], "Full Column")

    def test_column_winner(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "2", "1", "2", "1", "2", "1", "q"]
        main()
        last_called = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_called - 1][0][0],
                         "Player 1 wins!")

    def test_row_winner(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "1", "2", "2", "3", "3", "4", "q"]
        main()
        last_called = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_called - 1][0][0],
                         "Player 1 wins!")

    def test_draw(self, patched_input, patched_print, *args):
        patched_input.side_effect = [
            "1", "1", "1", "1", "1", "1", "1", "1", "1", "2", "2", "2", "2",
            "2", "2", "2", "2", "4", "4", "4", "4", "4", "4", "4", "4", "6",
            "3", "3", "3", "3", "3", "3", "3", "3", "8", "8", "8", "8", "8",
            "8", "8", "8", "7", "7", "7", "7", "7", "7", "7", "7", "6", "6",
            "6", "6", "6", "6", "6", "6", "5", "5", "5", "5", "5", "5", "5",
            "5"
        ]
        main()
        last_called = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_called - 1][0][0],
                         "Draw!")


if __name__ == '__main__':
    unittest.main()
