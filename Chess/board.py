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

        self.board = [[0 for x in range(8)] for _ in range(rows)]
        self.board[0][0] = Rook(0,0, 'b')
        self.board[0][1] = Knight(0,1, 'b')
        self.board[0][2] = Bishop(0,2, 'b')
        self.board[0][3] = Queen(0,3, 'b')
        self.board[0][4] = King(0,4, 'b')
        self.board[0][5] = Bishop(0,5, 'b')
        self.board[0][6] = Knight(0,6, 'b')
        self.board[0][7] = Rook(0,7, 'b')
        
        '''self.board[1][0] = Pawn(1,0, 'b')
        self.board[1][1] = Pawn(1,1, 'b')
        self.board[1][2] = Pawn(1,2, 'b')
        self.board[1][3] = Pawn(1,3, 'b')
        self.board[1][4] = Pawn(1,4, 'b')
        self.board[1][5] = Pawn(1,5, 'b')
        self.board[1][6] = Pawn(1,6, 'b')
        self.board[1][7] = Pawn(1,7, 'b')'''

        self.board[7][0] = Rook(7,0, 'w')
        self.board[7][1] = Knight(7,1, 'w')
        self.board[7][2] = Bishop(7,2, 'w')
        self.board[7][3] = Queen(7,3, 'w')
        self.board[7][4] = King(7,4, 'w')
        self.board[7][5] = Bishop(7,5, 'w')
        self.board[7][6] = Knight(7,6, 'w')
        self.board[7][7] = Rook(7,7, 'w')
        
        '''self.board[6][0] = Pawn(6,0, 'w')
        self.board[6][1] = Pawn(6,1, 'w')
        self.board[6][2] = Pawn(6,2, 'w')
        self.board[6][3] = Pawn(6,3, 'w')
        self.board[6][4] = Pawn(6,4, 'w')
        self.board[6][5] = Pawn(6,5, 'w')
        self.board[6][6] = Pawn(6,6, 'w')
        self.board[6][7] = Pawn(6,7, 'w')'''

    def update_moves(self):
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)

    def draw(self, win):
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win)

    def select(self, col, row):
        prev = (-1,-1)
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] != 0:                        
                    if self.board[i][j].selected:
                        prev = (i,j)

        if self.board[row][col] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (col,row) in moves:
                self.move(prev, (row,col))
            self.reset_selected()
        else:
            if self.board[prev[0]][prev[1]].colour != self.board[row][col].colour:
                moves = self.board[prev[0]][prev[1]].move_list
                if (col,row) in moves:
                    self.move(prev, (row,col))
                self.board[row][col].selected = True
                self.reset_selected()
            else:
                self.reset_selected()
                self.board[row][col].selected = True

    def reset_selected(self):
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] != 0:                        
                    self.board[i][j].selected = False

    def move(self, start, end):
        nBoard = self.board[:]
        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard






    
