from enum import Enum
import numpy as np

class Cell(Enum):
    X = "X"
    O = "O"
    N = "•"

class Board:
    def __init__(self, board: list=[[Cell.N for _ in range(3)] for _ in range(3)]):
        self.raise_if_rows_uneven(board)
        self.raise_if_not_square(board)

        self.str = self.get_string()
        self.board = board
    
    def __str__(self) -> str:
        return self.str
    
    def get_string(self):
        try:
            return "\n".join([" ".join([cell.value for cell in row]) for row in self.board])
        except AttributeError:
            raise TypeError("board cannot contain non-Cell type values")
    
    def raise_if_rows_uneven(self, board):
        if len(set(map(len, board))) != 1:
            raise ValueError("board rows cannot have varying lengths")
    
    def raise_if_not_square(self, board):
        if len(board) != len(board[0]):
            raise ValueError("board must have equal amounts of rows and columns")
    
    def place(self, player: Cell, position: tuple):
        self.raise_if_not_cell(player)
        self.raise_if_not_tuple(position)

        position_x, position_y = position
        self.board[position_y][position_x] = player
    
    def raise_if_not_cell(self, cell):
        if type(cell) != Cell:
            raise TypeError("specified cell type is not of type Cell")
    
    def raise_if_not_tuple(self, _tuple):
        if type(_tuple) != tuple:
            raise TypeError(f"cannot determine coordinates from type {type(_tuple).__name__}")
    
    def get_winner(self) -> Cell:
        for board in [self.board, np.transpose(self.board)]:
            result = self.check_rows(board)
            if result != Cell.N:
                return result

        return self.check_diagonals()

    def check_rows(self, board: list) -> Cell:
        for row in board:
            if len(set(row)) == 1:
                return row[0]

        return Cell.N

    def check_diagonals(self) -> Cell:
        if len(set([row[index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][0]
        
        if len(set([row[-1-index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][-1]

        return Cell.N