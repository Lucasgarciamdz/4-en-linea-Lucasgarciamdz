from unittest.mock import patch
from pygame_4_in_line import FourInLine2D
from pygame.locals import *
from pygame.event import Event

import unittest


@patch('random.choice', return_value=1)
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
    pass

if __name__ == "__main__":
    unittest.main()
