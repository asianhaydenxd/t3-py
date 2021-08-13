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
            for x in y:
                string += f"{x.value} "
            string += "\n"
        return string
