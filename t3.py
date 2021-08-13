from enum import Enum

class Cell(Enum):
    X = "X"
    O = "O"
    N = "•"

class Board:
    def __init__(self, board: list=[[Cell.N for _ in range(3)] for _ in range(3)]):
        self.board = board
    
    def __str__(self) -> str:
        string = ""
        for y in self.board:
            string += f"{' '.join(map(lambda k: k.value, y))}\n"
        return string
    
    def place(self, player: Cell, position: tuple):
        position_x, position_y = position
        self.board[position_y][position_x] = player
