from enum import Enum

class Cell(Enum):
    X = "X"
    O = "O"
    N = "•"

class Board:
    def __init__(self, board: list = [[Cell.N for _ in range(3)] for _ in range(3)]):
        if len(set(map(len, board))) != 1: raise ValueError("board rows cannot have varying lengths")
        if len(board) != len(board[0]): raise ValueError("board must have equal amounts of rows and columns")

        self.board = board
    
    def __str__(self) -> str:
        return "\n".join([" ".join([cell.value for cell in row]) for row in board])
        
    def place(self, player: Cell, position_x: int, position_y: int):
        if type(cell) != Cell: raise TypeError("specified cell type is not of type Cell")

        self.board[position_y][position_x] = player
    
    def get_winner(self) -> Cell:
        for board in [self.board, self.transpose_board()]:
            if (result := self.check_rows(board)) != Cell.N:
                return result

        return self.check_diagonals()
    
    def transpose_board(self) -> list:
        return [[row[i] for row in self.board] for i in range(len(self.board[0]))]

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