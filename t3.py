from enum import Enum

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
