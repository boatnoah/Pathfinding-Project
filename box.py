from settings import *
import pygame


class Box:
    def __init__(self, i, j): # i will be the rows and j will the be columns
        self.x = i
        self.y = j
        self.isWall = False
        self.isTarget = False
        self.isStart = False
        self.isQueued = False
        self.isVisited = False
        self.prior = None
        self.distance = float("inf")
        self.neighbors = []
        
    def __lt__(self, other):
        return self.distance < other.distance


    def draw_box(self, canvas, color):
        pygame.draw.rect(canvas, color, (self.x * BOX_WIDTH, self.y * BOX_HEIGHT, BOX_WIDTH - 2, BOX_HEIGHT - 2))

    def _set_neighbors(self):
        if self.x > 0:
            self.neighbors.append((GRID[self.x - 1][self.y], 1 if not GRID[self.x - 1][self.y].isWall else 5))
        if self.x < COLUMNS - 1:
            self.neighbors.append((GRID[self.x + 1][self.y], 1 if not GRID[self.x + 1][self.y].isWall else 5))
        if self.y > 0:
            self.neighbors.append((GRID[self.x][self.y - 1], 1 if not GRID[self.x][self.y - 1].isWall else 5))
        if self.y < ROWS - 1:
            self.neighbors.append((GRID[self.x][self.y + 1], 1 if not GRID[self.x][self.y + 1].isWall else 5))
    
   

    

        


