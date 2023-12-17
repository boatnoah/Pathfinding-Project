from settings import *
import pygame


class Box:
    def __init__(self, i, j): # i will be the rows and j will the be columns
        self.x = i
        self.y = j
        self.isWall = False
        self.isTarget = False
        self.isStart = False
    
    def draw_box(self, canvas, color):
        pygame.draw.rect(canvas, color, (self.x * BOX_WIDTH, self.y * BOX_HEIGHT, BOX_WIDTH - 2, BOX_HEIGHT - 2))




class DropDown:
    def __init__(self) -> None:
        pass