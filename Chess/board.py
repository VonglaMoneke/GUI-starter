import pygame
from piece import Bishop
from piece import King
from piece import Knight
from piece import Queen
from piece import Rook
from piece import Pawn

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = [[] for _ in range(rows)]
        self.board[0][0] = Rook(0,0, 'b')
        self.board[0][1] = Knight(0,1, 'b')
        self.board[0][2] = Bishop(0,2, 'b')
        self.board[0][3] = Queen(0,3, 'b')
        self.board[0][4] = King(0,4, 'b')
        self.board[0][5] = Bishop(0,5, 'b')
        self.board[0][6] = Knight(0,6, 'b')
        self.board[0][7] = Rook(0,7, 'b')
        
        self.board[1][0] = Pawn(1,0, 'b')
        self.board[1][1] = Pawn(1,1, 'b')
        self.board[1][2] = Pawn(1,2, 'b')
        self.board[1][3] = Pawn(1,3, 'b')
        self.board[1][4] = Pawn(1,4, 'b')
        self.board[1][5] = Pawn(1,5, 'b')
        self.board[1][6] = Pawn(1,6, 'b')
        self.board[1][7] = Pawn(1,7, 'b')

        self.board[7][0] = Rook(0,0, 'w')
        self.board[7][1] = Knight(0,1, 'w')
        self.board[7][2] = Bishop(0,2, 'w')
        self.board[7][3] = Queen(0,3, 'w')
        self.board[7][4] = King(0,4, 'w')
        self.board[7][5] = Bishop(0,5, 'w')
        self.board[7][6] = Knight(0,6, 'w')
        self.board[7][7] = Rook(0,7, 'w')
        
        self.board[6][0] = Pawn(1,0, 'w')
        self.board[6][1] = Pawn(1,1, 'w')
        self.board[6][2] = Pawn(1,2, 'w')
        self.board[6][3] = Pawn(1,3, 'w')
        self.board[6][4] = Pawn(1,4, 'w')
        self.board[6][5] = Pawn(1,5, 'w')
        self.board[6][6] = Pawn(1,6, 'w')
        self.board[6][7] = Pawn(1,7, 'w')







    
