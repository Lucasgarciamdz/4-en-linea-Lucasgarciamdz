from unittest.mock import patch
from pygame_4_in_line import FourInLine2D
from pygame.locals import *
from pygame.event import Event

import unittest



@patch('pygame.display.set_caption')
@patch('pygame.display.set_mode')
@patch('pygame.draw.line')
@patch('pygame.draw.circle')
@patch('pygame.font.Font')
@patch('pygame.display')
@patch('pygame.display.update')
@patch('pygame.event.get')
@patch('pygame.event.Event')
@patch('pygame.time.Clock')
@patch('pygame.init')
class TestFourInLine2D(unittest.TestCase):

    def setUp(self):
        self.game = FourInLine2D()
    
    #test pygame init once
    def test_pygame_init_once(self, patched_init,*args):
        self.game.run()
        patched_init.assert_called_once()


if __name__ == "__main__":
    unittest.main()
