import pygame
import os

b_bishop = pygame.image.load(os.path.join('img','black_bishop.png'))
b_king = pygame.image.load(os.path.join('img','black_king.png'))
b_knight = pygame.image.load(os.path.join('img','black_knight.png'))
b_queen = pygame.image.load(os.path.join('img','black_queen.png'))
b_rook = pygame.image.load(os.path.join('img','black_rook.png'))
b_pawn = pygame.image.load(os.path.join('img','black_pawn.png'))

w_bishop = pygame.image.load(os.path.join('img','white_bishop.png'))
w_king = pygame.image.load(os.path.join('img','white_king.png'))
w_knight = pygame.image.load(os.path.join('img','white_knight.png'))
w_queen = pygame.image.load(os.path.join('img','white_queen.png'))
w_rook = pygame.image.load(os.path.join('img','white_rook.png'))
w_pawn = pygame.image.load(os.path.join('img','white_pawn.png'))

b = [b_bishop, b_king, b_knight, b_queen, b_rook, b_pawn]
w = [w_bishop, w_king, w_knight, w_queen, w_rook, w_pawn]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (65,65)))
for img in w:
    W.append(pygame.transform.scale2x(img, (65,65)))   


class piece:
    img = -1
    rect = (113,113,525,525)
    startX = rect[0]
    startY = rect[1]
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False

    def move(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.colour == 'w':
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        x = round(self.startX + (self.col * self.rect[2]/8))
        y = round(self.startY + (self.row * self.rect[3]/8))

        win.blit(drawThis, (x,y))


class Bishop(piece):
    img = 0


class King(piece):
    img = 1


class Knight(piece):
    img = 2


class Queen(piece):
    img = 3


class Rook(piece):
    img = 4


class Pawn(piece):
    img = 5
