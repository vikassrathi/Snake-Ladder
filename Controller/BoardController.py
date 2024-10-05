from Models.Board import Board


class BoardController:

    def __init__(self):
        self.board=Board()
    def print_board(self):
        print(f'These are snake positions {self.board.get_snake_position()}')
        print(f'These are ladder positions {self.board.get_ladder_position()}')

    def set_board_object(self):
        self.board.set_snake_position()
        self.board.set_ladder_position()
        return self.board
