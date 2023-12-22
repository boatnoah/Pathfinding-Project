from tkinter import messagebox, Tk
import pygame
import sys
from settings import *
from box import Box
from button import Button
from queue import PriorityQueue




pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

priority_queue = PriorityQueue() #Dijkstra and A*
queue = [] #BFS
stack = [] #DFS
path = []

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def initialize_grid(rows, col):
    for i in range(rows):
        tmp = []
        for j in range(col):
            tmp.append(Box(i, j))
        GRID.append(tmp)
    
    for i in range(ROWS):
        for j in range(COLUMNS):
            GRID[i][j]._set_neighbors()
    


def heuristic(a, b):
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    return abs(x1 - x2) + abs(y1 - y2)


def algorithm_menu_screen(first_run=True):
    running = True
    button_height, button_spacing = 100, 50
    while running:
        screen.fill((50, 50, 50))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(35).render("Choose an Algorithm", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WINDOW_WIDTH // 2, 50))

        DIJKSTRA_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), 
                                 pos=(WINDOW_WIDTH // 2, 150), 
                                text_input="DIJKSTRA", font=get_font(40), 
                                base_color="#d7fcd4", hovering_color="White")
        
        ASTAR_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), 
                              pos=(WINDOW_WIDTH // 2, 150 + button_height + button_spacing),
                              text_input="A* Search", font=get_font(40), 
                              base_color="#d7fcd4", hovering_color="White")
        
        BFS_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), 
                            pos=(WINDOW_WIDTH // 2, 150 + 2 * (button_height + button_spacing)), 
                            text_input="BFS", font=get_font(40), 
                            base_color="#d7fcd4", hovering_color="White")
        
        DFS_BUTTON = Button(image=pygame.image.load("assets/buttonBG.png"), 
                            pos=(WINDOW_WIDTH // 2, 150 + 3 * (button_height + button_spacing)), 
                            text_input="DFS", font=get_font(40), 
                            base_color="#d7fcd4", hovering_color="White")
        
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
                    main("Dijkstra", first_run)
                if ASTAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("A-star", first_run)
                if BFS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("BFS", first_run)
                if DFS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("DFS", first_run)

        
        pygame.display.update()

def main(typeOfAlgo, first_run): #grid screen
    global priority_queue, queue, heap, stack, path, is_starting_set, is_target_set, start_cell, target_cell, algorithm_to_run, GRID
    algorithm_to_run = typeOfAlgo 
    print(algorithm_to_run)
    if first_run:
        is_starting_set = False
        is_target_set = False
    
    running = True
    begin_search = False
    searching = True
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
                if event.button == 1:
                    if not is_starting_set:
                        start_cell = GRID[i][j]
                        start_cell.isStart = True
                        is_starting_set = True
                        if algorithm_to_run == "Dijkstra":
                            start_cell.isQueued = True
                        elif algorithm_to_run == "BFS":
                            start_cell.isQueued = True
                    elif not is_target_set:
                        target_cell = GRID[i][j]
                        target_cell.isTarget = True
                        is_target_set = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: #clear the current state of the grid
                    GRID.clear()
                    initialize_grid(ROWS, COLUMNS)
                    is_starting_set = False
                    is_target_set = False 
                    begin_search = False
                    searching = True
                    path.clear()
                    priority_queue = PriorityQueue()
                    queue.clear()
                if event.key == pygame.K_ESCAPE: 
                    #still preserve the starting and target positions and walls
                    for i in range(ROWS):
                        for j in range(COLUMNS):
                            cell = GRID[i][j]
                            if cell.isVisited:
                                cell.isVisited = False
                            if cell.isQueued:
                                cell.isQueued = False
                            if cell.prior is not None:
                                cell.prior = None
                            if cell.distance != float("inf"):
                                cell.distance = float("inf")
                            
                    
                    path.clear()
                    priority_queue = PriorityQueue()
                    queue.clear()
                    stack.clear()
                    is_starting_set = True
                    is_target_set = True
                    
                    
                    algorithm_menu_screen(False)

                    
                if event.key == pygame.K_RETURN and is_starting_set and is_target_set: #to ensure algorithm will run with a start and end
                    begin_search = True

        if begin_search:
            if algorithm_to_run == "Dijkstra":
                print("Running Dijkstra")
                if priority_queue.empty() and searching:
                    priority_queue.put((0, start_cell))
                    start_cell.distance = 0
            

                if not priority_queue.empty() and searching:
                    # Step 2: Process nodes in the priority queue
                    current_distance, current_box = priority_queue.get()

                    if not current_box.isVisited:  # Skip if already visited
                
                        current_box.isVisited = True  # Mark as visited

                        if current_box.isTarget:
                            searching = False
                            while current_box.prior is not None:
                                path.append(current_box.prior)
                                current_box = current_box.prior
                                pygame.event.pump()  # Process events during delay

            
                        for neighbor, edge_weight in current_box.neighbors:
                            if not neighbor.isVisited and not neighbor.isWall:
                                tentative_distance = current_distance + edge_weight

                                if tentative_distance < neighbor.distance:
                                    neighbor.distance = tentative_distance
                                    neighbor.prior = current_box
                                    priority_queue.put((tentative_distance, neighbor))
                                    neighbor.isQueued = True  # Mark as queued


            elif algorithm_to_run == "A-star":
                print("Running A-star")
                if priority_queue.empty() and searching:
                    priority_queue.put((0, start_cell))
                    start_cell.distance = 0
                if not priority_queue.empty() and searching:
                    current_distance, current_box = priority_queue.get()

                    if not current_box.isVisited:
                        current_box.isVisited = True

                        if current_box.isTarget:
                            searching = False
                            while current_box.prior is not None:
                                path.append(current_box.prior)
                                current_box = current_box.prior
                                pygame.event.pump()
                    
                        for neighbor, edge_weight in current_box.neighbors:
                            if not neighbor.isVisited and not neighbor.isWall:
                                tentative_distance = current_distance + edge_weight + heuristic(neighbor, target_cell)

                                if tentative_distance < neighbor.distance:
                                    neighbor.distance = tentative_distance
                                    neighbor.prior = current_box
                                    priority_queue.put((tentative_distance, neighbor))
                                    neighbor.isQueued = True
            

            elif algorithm_to_run == "BFS":
                print("Running BFS")
                if not queue and searching:
                    queue.append(start_cell)
        
                if queue and searching:
                    print("made it here")
                    current_box = queue.pop(0)
                    current_box.isVisited = True
                    if current_box.isTarget:
                        searching = False
                        while current_box.prior != start_cell:
                            path.append(current_box.prior)
                            current_box = current_box.prior
                            pygame.event.pump()  # Process events during delay
                    else:
                        for neighbor, _ in current_box.neighbors:
                            if not neighbor.isQueued and not neighbor.isWall:
                                neighbor.isQueued = True
                                neighbor.prior = current_box
                                queue.append(neighbor)
        
            elif algorithm_to_run == "DFS":
                if not stack and searching:
                    stack.append(start_cell)
                
                if stack and searching:
                    current_box = stack.pop()
                    if not current_box.isVisited:
                        current_box.isVisited = True
                    
                    if current_box.isTarget:
                        searching = False
                        while current_box.prior != start_cell:
                            path.append(current_box.prior)
                            current_box = current_box.prior
                    
                    else:
                        for neighbor, _ in current_box.neighbors:
                            if not neighbor.isVisited and not neighbor.isWall:
                                neighbor.isQueued = True
                                neighbor.prior = current_box
                                stack.append(neighbor)
                        


            
        screen.fill((0, 0, 0))
        for i in range(ROWS):
            for j in range(COLUMNS):
                cell = GRID[i][j]
                cell.draw_box(screen, (50, 50, 50))
                if cell.isQueued:
                    cell.draw_box(screen, "yellow")
                if cell.isVisited:
                    cell.draw_box(screen, "green")
                if cell in path:
                    cell.draw_box(screen, "cyan")
                if cell.isWall:
                    cell.draw_box(screen, "black")
                if cell.isTarget:
                    cell.draw_box(screen, "red")
                if cell.isStart:
                    cell.draw_box(screen, "blue")
                
        pygame.display.flip()
        

initialize_grid(ROWS, COLUMNS)
algorithm_menu_screen()

