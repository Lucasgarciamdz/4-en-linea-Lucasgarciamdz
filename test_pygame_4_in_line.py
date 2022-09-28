from unittest.mock import patch
from pygame_4_in_line import FourInLine2D
from pygame.locals import *
from pygame.event import Event

import unittest


@patch('pygame.display.update')
@patch('pygame.display.flip')
@patch('pygame.display.set_caption')
@patch('pygame.display.set_mode')
@patch('pygame.draw.line')
@patch('pygame.draw.circle')
@patch('pygame.time.Clock')
class TestFourInLine2D(unittest.TestCase):

    def setUp(self):
        with patch('random.randint', return_value=1):
            self.game2d = FourInLine2D()

    def test_init(self, *args):
        self.assertIsNotNone(self.game2d.game)

    @patch('pygame.quit')
    @patch('pygame.event.get', return_value=[Event(QUIT)])
    @patch('pygame.init')
    def test_run_and_quit(self, init_patched, event_get_patched, quit_patched,
                          *args):
        game2d = FourInLine2D()
        init_patched.assert_called_once()
        game2d.run()
        quit_patched.assert_called_once()

    @patch('pygame.init')
    @patch('pygame.quit')
    @patch('pygame.mouse.get_pos', return_value=(100, 100))
    @patch('pygame.event.get',
           return_value=[Event(MOUSEBUTTONDOWN),
                         Event(QUIT)])
    def test_click(self, event_get_patched, mouse_get_pos_patched,
                   quit_patched, *args):
        self.game2d.run()
        event_get_patched.assert_called_once()
        self.game2d.game.board[7][2] = 1

    @patch('pygame.init')
    @patch('pygame.draw.line')
    def test_draw_board(self, draw_line_patched, *args):
        self.game2d.draw_board()
        self.assertEqual(draw_line_patched.call_count, 18)


if __name__ == "__main__":
    unittest.main()
