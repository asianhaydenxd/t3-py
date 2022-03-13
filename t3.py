from enum import Enum

class Cell:
    def __init__(self, symbol: chr):
        self.symbol = symbol
    
    def __str__(self):
        return self.symbol

class Board:
    def __init__(self, width: int = 3, emptychar: chr = '•', playerchars: list[chr] = ['X', 'O']):
        self.emptycell = Cell(emptychar)
        self.playercells = [Cell(char) for char in playerchars]

        self.board = [[self.emptycell for _ in range(width)] for _ in range(width)]

        self._turn_number = 0
    
    def __str__(self) -> str:
        return "\n".join([" ".join([cell.__str__() for cell in row]) for row in self.board])
        
    def place(self, playercell: Cell, position_x: int, position_y: int):
        if playercell not in self.playercells: raise TypeError("specified cell is not in board's player cells")

        self.board[position_y][position_x] = playercell

    def get_turn(self):
        return self.playercells[self._turn_number]

    def iterate_turn(self):
        self._turn_number += 1
        if self._turn_number >= len(self.playercells): self._turn_number = 0
        return self.get_turn()
    
    def get_winner(self) -> Cell:
        for board in [self.board, self.transpose_board()]:
            if (result := self.check_rows(board)) != self.emptycell:
                return result

        return self.check_diagonals()
    
    def transpose_board(self) -> list:
        return [[row[i] for row in self.board] for i in range(len(self.board[0]))]

    def check_rows(self, board: list) -> Cell:
        for row in board:
            if len(set(row)) == 1:
                return row[0]

        return self.emptycell

    def check_diagonals(self) -> Cell:
        if len(set([row[index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][0]
        
        if len(set([row[-1-index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][-1]

        return self.emptycell