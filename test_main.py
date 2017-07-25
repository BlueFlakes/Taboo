# main start module
from models.time_board import TimeBoard

def main():
    time_board = TimeBoard()
    time_board.create_board()
    print(time_board)


if __name__ == '__main__':
    main()
