from rules_4_in_line import FourInLine
from exceptions_4_in_line import *


def main():
    game = FourInLine()
    playing = True
    while playing:
        print_board(game.board)
        playing = play(game)

def play(game):

    try:
        column_input = input("Player {}, choose a column: ".format(game.player))
        if column_input == 'q':
            return False
        column = int(column_input)
        game.insert_chip(column)
    except ValueError:
        print("You must enter a number")
    except Overflow:
        print("Overflow")
    except FullColumn:
        print("Full Column")
    if game.winner:
        print_board(game.board)
        print(f"Player {game.winner} wins!")
        return False
    if game.is_full():
        print_board(game.board)
        print("Draw!")
        return False
    return True
        

def print_board(board):
    # prepare the empty content
    rows = 8
    cols = 8
    content = [["."] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                content[i][j] = "X"
            elif board[i][j] == 2:
                content[i][j] = "O"

    # build frame
    width = len(str(max(rows, cols) - 1))
    contentLine = "# | values |"

    dashes = "-".join("-" * width for _ in range(cols))
    frameLine = contentLine.replace("values", dashes)
    frameLine = frameLine.replace("#", " " * width)
    frameLine = frameLine.replace("| ", "+-").replace(" |", "-+")

    # print grid
    print(frameLine)
    for i, row in enumerate((content), 1):
        values = " ".join(f"{v:{width}s}" for v in row)
        line = contentLine.replace("values", values)
        line = line.replace("#", f"{(rows+1)-i:{width}d}")
        print(line)
    print(frameLine)

    # x-axis numbers
    numLine = contentLine.replace("|", " ")
    numLine = numLine.replace("#", " " * width)
    colNums = " ".join(f"{i:<{width}d}" for i in range(1, cols + 1))
    numLine = numLine.replace("values", colNums)
    print(numLine)


if __name__ == "__main__":
    main()