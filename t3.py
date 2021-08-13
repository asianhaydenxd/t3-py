class Board:
    def __init__(self, board: list=[[Cell.N for _ in range(3)] for _ in range(3)]):
        self.board = board
