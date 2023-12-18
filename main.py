from tkinter import messagebox, Tk
import pygame
import sys
from settings import *
from box import Box
from button import Button



#Initialize grid
GRID = []


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def initialize_grid(rows, col):
    for i in range(rows):
        tmp = []
        for j in range(col):
            tmp.append(Box(i, j))
        GRID.append(tmp) 

def create_grid(rows, col):
    for i in range(col):
        for j in range(rows):
            cell = GRID[i][j]
            cell.draw_box(screen, (50, 50, 50))
            if cell.isWall:
                cell.draw_box(screen, "black")
            if cell.isTarget:
                cell.draw_box(screen, "red")
            if cell.isStart:
                cell.draw_box(screen, "blue")

def algorithm_menu_screen():
    running = True
    button_height, button_spacing = 100, 50
    while running:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(35).render("Choose an Algorithm", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WINDOW_WIDTH // 2, 50))
        DIJKSTRA_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), pos=(WINDOW_WIDTH // 2, 150), 
                                text_input="DIJKSTRA", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        ASTAR_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), pos=(WINDOW_WIDTH // 2, 150 + button_height + button_spacing), 
                            text_input="A* Search", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        BFS_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), pos=(WINDOW_WIDTH // 2, 150 + 2 * (button_height + button_spacing)), 
                            text_input="BFS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        DFS_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), pos=(WINDOW_WIDTH // 2, 150 + 3 * (button_height + button_spacing)), 
                            text_input="DFS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [DIJKSTRA_BUTTON, ASTAR_BUTTON, BFS_BUTTON, DFS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DIJKSTRA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("Dijkstra")
                if ASTAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("A-star")
                if BFS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("BFS")
                if DFS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("DFS")

        
        pygame.display.update()

def main(typeOfAlgo): #grid screen
    algorithm_to_run = typeOfAlgo 
    print(algorithm_to_run)
    is_starting_set = False
    is_target_set = False
    running = True
    initialize_grid(ROWS, COLUMNS) 
    while running:
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: #clear the current state of the grid
                    GRID.clear()
                    initialize_grid(ROWS, COLUMNS)
                    create_grid(ROWS, COLUMNS)
                    is_starting_set = False
                    is_target_set = False
                    typeOfAlgo = "" 
                
                if event.key == pygame.K_ESCAPE:
                    GRID.clear()
                    initialize_grid(ROWS, COLUMNS)
                    create_grid(ROWS, COLUMNS)
                    is_starting_set = False
                    is_target_set = False
                    algorithm_menu_screen()
                    
                if event.key == pygame.K_RETURN and is_starting_set and is_target_set:
                    if algorithm_to_run == "Dijkstra":
                        pass
                    elif algorithm_to_run == "A-star":
                        pass
                    elif algorithm_to_run == "BFS":
                        pass
                    elif algorithm_to_run == "DFS":
                        pass

        screen.fill((0, 0, 0))

        create_grid(ROWS, COLUMNS)
        pygame.display.flip()
        


algorithm_menu_screen()

