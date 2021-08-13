from enum import Enum
import numpy as np

class Cell(Enum):
    X = "X"
    O = "O"
    N = "•"

class Board:
    def __init__(self, board: list=[[Cell.N for _ in range(3)] for _ in range(3)]):
        self.board = board
    
    def __str__(self) -> str:
        return "\n".join([" ".join([cell.value for cell in row]) for row in self.board])
    
    def place(self, player: Cell, position: tuple):
        position_x, position_y = position
        self.board[position_y][position_x] = player
    
    def get_winner(self) -> Cell:
        for board in [self.board, np.transpose(self.board)]:
            result = self.check_rows(board)
            if result != Cell.N:
                return result
                
        return self.check_diagonals()

    def check_rows(self, board) -> Cell:
        for row in board:
            if len(set(row)) == 1:
                return row[0]

        return Cell.N

    def check_diagonals(self):
        if len(set([self.board[i][i] for i in range(len(self.board))])) == 1:
            return self.board[0][0]

        if len(set([self.board[i][-1-i] for i in range(len(self.board))])) == 1:
            return self.board[0][-1]

        return Cell.N