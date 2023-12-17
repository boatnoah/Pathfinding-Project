from tkinter import messagebox, Tk
import pygame
import sys
from settings import *
from box import Box


pygame.init()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
GRID = []
for i in range(COLUMNS):
    tmp = []
    for j in range(ROWS):
        tmp.append(Box(i, j))
    GRID.append(tmp)


def main():
    is_starting_set = False
    is_target_set = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION: #allows user to draw out the walls.
                x, y = pygame.mouse.get_pos()
                i = x // BOX_WIDTH
                j = y // BOX_HEIGHT
                if event.buttons[2]:
                    wall_cell = GRID[i][j]
                    wall_cell.isWall = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #allows the user to choose the starting position.
                x, y = pygame.mouse.get_pos()
                i = x // BOX_WIDTH
                j = y // BOX_HEIGHT
                if event.button == 1 and not is_starting_set:
                    start_cell = GRID[i][j]
                    start_cell.isStart = True
                    is_starting_set = True
                elif event.button == 1 and not is_target_set:
                    target_cell = GRID[i][j]
                    target_cell.isTarget = True
                    is_target_set = True





        screen.fill((0, 0, 0))
        for i in range(COLUMNS):
            for j in range(ROWS):
                cell = GRID[i][j]
                cell.draw_box(screen, (50, 50, 50))
                if cell.isWall:
                    cell.draw_box(screen, "black")
                if cell.isTarget:
                    cell.draw_box(screen, "red")
                if cell.isStart:
                    cell.draw_box(screen, "blue")

        pygame.display.flip()


main()