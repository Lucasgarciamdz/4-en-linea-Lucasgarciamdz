from sre_parse import WHITESPACE
import pygame
from pygame.locals import *
from rules_4_in_line import FourInLine, PLAYER_ONE, PLAYER_TWO
from exceptions_4_in_line import *

RED = (238, 96, 85)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (96, 211, 148)
BLACK = (2, 5, 8)
WIDTH = 900
HEIGHT = 500


class FourInLine2D:

    def __init__(self):
        pygame.init()

        self.game = FourInLine()

        pygame.display.set_caption('4 in line')
        self.DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw_board(self):
        self.DISPLAY.fill((255, 217, 125))

        for i in range(9):
            pygame.draw.line(self.DISPLAY, BLACK, (50, 50 + 50 * i),
                             (450, 50 + 50 * i), 3)
            pygame.draw.line(self.DISPLAY, BLACK, (50 + 50 * i, 50),
                             (50 + 50 * i, 450), 3)
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render('Turn', True, (2, 5, 8))
        textRect = text.get_rect()
        textRect.center = (675, 80)
        self.DISPLAY.blit(text, textRect)
        pygame.draw.circle(self.DISPLAY, BLACK, (680, 250), 55, 4)

    def run(self):

        self.draw_board()

        while self.game.winner == "":
            pygame.display.update()

            pygame.display.flip()
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game.winner = "quit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    try:
                        self.game.insert_chip(mouse_position[0] // 50)
                    except Overflow:
                        pass
                    except FullColumn:
                        pass
            if self.game.player == PLAYER_ONE:
                pygame.draw.circle(self.DISPLAY, RED, (680, 250), 50)
            else:
                pygame.draw.circle(self.DISPLAY, GREEN, (680, 250), 50)

            for row in range(8):
                for col in range(8):
                    if self.game.board[row][col] == PLAYER_ONE:
                        pygame.draw.circle(self.DISPLAY, RED,
                                           (75 + 50 * col, 75 + 50 * row), 20)
                    elif self.game.board[row][col] == PLAYER_TWO:
                        pygame.draw.circle(self.DISPLAY, GREEN,
                                           (75 + 50 * col, 75 + 50 * row), 20)

        if self.game.winner == PLAYER_ONE:
            winner_color = "Red"
        elif self.game.winner == PLAYER_TWO:
            winner_color = "Green"
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(winner_color + " player wins", True, BLUE, RED)
        textRect = text.get_rect()
        textRect.center = (450, 250)
        self.DISPLAY.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()


if __name__ == "__main__":
    FourInLine2D().run()
