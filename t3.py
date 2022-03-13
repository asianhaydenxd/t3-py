from enum import Enum
from typing import Union

class Cell:
    # To store different cell types as cell objects rather than relying on using different characters
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
        
    def place(self, x_pos: int, y_pos: int, playercell: Cell = None):
        if playercell == None: playercell = self.get_turn() # Automatically get whose turn it is if no specific player is specified
        if playercell not in self.playercells: raise TypeError("specified cell is not in board's player cells")

        self.board[y_pos][x_pos] = playercell

    def get_turn(self):
        return self.playercells[self._turn_number]

    def iterate_turn(self):
        # Go to the next player (according to the order specified in the playerchars parameter)
        self._turn_number += 1
        if self._turn_number >= len(self.playercells): self._turn_number = 0
        return self.get_turn()
    
    def get_winner(self) -> Union[Cell, None]:
        # Check for any 3-in-a-row in the board
        for board in [self.board, self.transpose_board()]: # Check for 3-in-a-rows in rows as well as columns 
            if (result := self.check_rows(board)) != self.emptycell:
                return result

        if (result := self.check_diagonals()) != self.emptycell:
            return result
        
        # Just return None if the only 3-in-a-rows found were empty cells
        return None

    def check_rows(self, board: list) -> Cell:
        # Check for a 3-in-a-row in the rows
        for row in board:
            if len(set(row)) == 1:
                return row[0]

        return self.emptycell

    def check_diagonals(self) -> Cell:
        # Check for a 3-in-a-row in the top-left to bottom-right diagonal
        if len(set([row[index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][0]
        
        # Check for a 3-in-a-row in the top-right to bottom-left diagonal
        if len(set([row[-1-index] for index, row in enumerate(self.board)])) == 1:
            return self.board[0][-1]

        return self.emptycell
    
    def transpose_board(self) -> list:
        # Return an alternate version of the board where rows are columns and columns are rows
        return [[row[i] for row in self.board] for i in range(len(self.board[0]))]