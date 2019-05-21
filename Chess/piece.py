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
    B.append(pygame.transform.scale(img, (60,60)))
for img in w:
    W.append(pygame.transform.scale(img, (60,60)))   


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
        self.move_list = []

    def move(self):
        pass

    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win):
        if self.colour == 'w':
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        if self.selected:
            moves = self.move_list

            for move in moves:
                x = 33 + round(self.startX + (move[0] * self.rect[2]/8))
                y = 33 + round(self.startY + (move[1] * self.rect[3]/8))
                if x > 33 and y > 33:
                    pygame.draw.circle(win, (255,0,0), (x,y), 10)
        

        x = 2 + round(self.startX + (self.col * self.rect[2]/8))
        y = 2 + round(self.startY + (self.row * self.rect[3]/8))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, 60,60), 2)

        win.blit(drawThis, (x,y))

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

class Bishop(piece):
    img = 0

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.colour != self.colour:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break

            djL += 1

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.colour != self.colour:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.colour != self.colour:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break
            djL += 1
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.colour != self.colour:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1

        return moves
        

class King(piece):
    img = 1

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.colour != self.colour:
                    moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.colour != self.colour:
                moves.append((j, i - 1))

            # TOP RIGHT
            if j < 7:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.colour != self.colour:
                    moves.append((j + 1, i - 1,))

        if i < 7:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.colour != self.colour:
                    moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.colour != self.colour:
                moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 7:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.colour != self.colour:
                    moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.colour != self.colour:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 7:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.colour != self.colour:
                moves.append((j + 1, i))

        return moves
                            


class Knight(piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        #Down Left
        if i < 6 and j > 0:
                p = board[i+2][j-1]
                if p == 0 or p.colour != self.colour:
                    moves.append((j-1, i+2))
        #Up Left
        if i > 1 and j > 0:
                p = board[i-2][j-1]
                if p == 0 or p.colour != self.colour:
                    moves.append((j-1, i-2))
        #Down Right
        if i < 6 and j < 7:
                p = board[i+2][j+1]
                if p == 0 or p.colour != self.colour:
                    moves.append((j+1, i+2))
        #Up Right
        if i > 1 and j < 7:
                p = board[i-2][j+1]
                if p == 0 or p.colour != self.colour:
                    moves.append((j+1, i-2))
                    
        return moves


class Queen(piece):
    img = 3

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.colour != self.colour:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9

            djL += 1

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.colour != self.colour:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.colour != self.colour:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9
            djL += 1
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.colour != self.colour:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -= 1

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.colour != self.colour:
                moves.append((j, x))
                break
            else:
                break

        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.colour != self.colour:
                moves.append((j, x))
                break
            else:
                break

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.colour != self.colour:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.colour != self.colour:
                moves.append((x, i))
                break
            else:
                break

        return moves


class Rook(piece):
    img = 4

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        #Up
        for x in range(i-1, -1,-1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.colour != self.colour:
                moves.append((j, x))
                break
            else:
                break

        #Down
        for x in range(i+1, 8,1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.colour != self.colour:
                moves.append((j, x))
                break
            else:
                break

        #Left
        for x in range(j-1, -1,-1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.colour != self.colour:
                moves.append((x, i))
                break
            else:
                break

        #Right
        for x in range(j+1, 8,1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.colour != self.colour:
                moves.append((x, i))
                break
            else:
                break

        return moves



class Pawn(piece):
    img = 5
    def __init__(self, row, col, colour):
        super().__init__(row,col, colour)
        self.first = True
        self.queen = False

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        if self.colour == 'b':
            if self.first:
                if i < 6:
                    p = board[i+2][j]
                    if p == 0:
                        moves.append((j, i+2))

            if i < 7:
                p = board[i+1][j]
                if p == 0:
                    moves.append((j, i+1))

                #diagonal taking
                if j < 7:
                    p = board[i+1][j+1]
                    if p != 0:
                        if p.colour != self.colour:
                            moves.append((j+1, i+1))

                if j > 0:
                    p = board[i+1][j-1]
                    if p != 0:
                        if p.colour != self.colour:
                            moves.append((j-1, i+1))
        #WHITE    
        else:
            if self.first:
                if i > 1:
                    p = board[i-2][j]
                    if p == 0:
                        moves.append((j, i-2))

            if i > 0:
                p = board[i-1][j]
                if p == 0:
                    moves.append((j, i-1))

                #diagonal taking
                if j < 7:
                    p = board[i-1][j+1]
                    if p != 0:
                        if p.colour != self.colour:
                            moves.append((j+1, i+1))

                if j > 0:
                    p = board[i-1][j-1]
                    if p != 0:
                        if p.colour != self.colour:
                            moves.append((j-1, i+1))
        
        return moves
                






