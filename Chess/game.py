import pygame
import os
from piece import Bishop
from board import Board


board = pygame.transform.scale(pygame.image.load(os.path.join('img','board_alt.png')), (750,750))
rect = (113,113,525,525)


def redraw_gamewindow():
    global win
    b = Bishop(1,1,'w')
    win.blit(board, (0,0))
    b.draw(win)
    pygame.display.update()

def main():
    board = Board(8,8)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)

        redraw_gamewindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
width = 750
height = 750
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chess Game')
main()
