from tkinter import messagebox, Tk
import pygame
import sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        screen.fill("white")
        pygame.display.flip()


main()