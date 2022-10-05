from exceptions_4_in_line import FullColumn, Overflow
import random

PLAYER_ONE = 1
PLAYER_TWO = 2


class FourInLine:

    def __init__(self):
        self.board = [[0 for column in range(8)] for row in range(8)]
        self.winner = ""
        self.player = random.choice([PLAYER_ONE, PLAYER_TWO])

    def insert_chip(self, column):
        self.check_overflow(column)
        column -= 1
        self.board[self.free_row(column)][column] = self.player
        self.check_winner()
        self.change_player()

    def free_row(self, column):
        for row in range(7, -1, -1):
            if self.board[row][column] == (0):
                return row
        raise FullColumn

    def change_player(self):
        if self.player == PLAYER_ONE:
            self.player = PLAYER_TWO
        else:
            self.player = PLAYER_ONE

    def check_overflow(self, column):
        if column > 8 or column < 1:
            raise Overflow

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def check_winner(self):
        for row in range(8):
            for col in range(8):
                self.has_winner(row, col)

    def generate_directions(self):
        return [
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
        ]

    def in_board(self, row, col):
        return (row >= 0 and row <= 7 and col >= 0 and col <= 7)

    def generate_winner_coord(self, row, col):
        winner_directions = self.generate_directions()
        winner_coord = []
        for row_delta, col_delta in winner_directions:
            winner_coord_direction = []
            for delta in range(4):
                if self.in_board(row + (row_delta * delta),
                                 col + (col_delta * delta)):
                    winner_coord_direction.append((
                        row + (row_delta * delta),
                        col + (col_delta * delta),
                    ))
                else:
                    break
            if len(winner_coord_direction) == 4:
                winner_coord.append(winner_coord_direction)

        return winner_coord

    def has_winner(self, row, col):
        winner_coord = self.generate_winner_coord(row, col)
        for winner_coord_direction in winner_coord:
            count = 0
            for coord_direction_row, coord_direction_col in winner_coord_direction:
                if self.board[coord_direction_row][
                        coord_direction_col] == self.player:
                    count += 1
            if count == 4:
                self.winner = self.player
        return False


if __name__ == "__main__":
    game = FourInLine()
    game.insert_chip(1)
    game.insert_chip(1)
    game.insert_chip(1)
    game.insert_chip(1)
    print(game.winner)
