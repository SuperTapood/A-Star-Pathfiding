"""
0. create grid
1. set start and goal
2. reset open_set to [start] and closed set to []
3. while open_set is not empty
    1. set new current based on lowest fscore in openset
    2. if the new current is the goal
        1. break and done
    3. remove current from open_set
    4. for each of the current's neighbors
        1. t_score is current.g_score + d(current, neighbor)
        2. if t_score < neighbor.g_score
            1. neighbor.parent is current
            2. neighbor.g_score is t_score
            3. neighbor.f_score is g_score + h(neighbor)
            4. if neighbor not is open_set
                1. add neighbor to open_set
4. there is no solution
5. display solution
"""

from cell import Cell
import numpy as np
import pygame
from time import time


def h(node):
    # pythagoras theroem
    return np.sqrt(np.square(abs(node.i - end.i)) + np.square(abs(node.j - end.j)))

def get_min(arr):
    min_item = arr[0]
    mini = min_item.f_score
    for i in range(1, len(arr)):
        if arr[i].f_score < mini:
            min_item = arr[i]
            mini = min_item.f_score
    return min_item


while True:
    s = time()
    grid = []
    cols, rows = 40, 40
    for i in range(cols):
        grid.append([Cell(i, j) for j in range(rows)])
    grid = np.array(grid)
    width, height = 600, 600
    scr = pygame.display.set_mode((width, height))
    pygame.display.set_caption("A* Pathfinding")
    cell_width = (width - 50) / cols
    cell_height = (height - 50) / rows
    start = grid[0][0]
    start.wall = False
    end = grid[-1][-1]
    end.wall = False
    start.g_score = 0
    start.f_score = h(start)
    open_set = [start]
    path = []

    while True:
        scr.fill((0, 0, 0))
        if open_set == []:
            # no solution
            break
        current = get_min(open_set)
        current.visited = True
        if current == end:
            break
        open_set.remove(current)
        for neighbor in current.get_pals(grid):
            if current.g_score < neighbor.g_score and not neighbor.wall:
                neighbor.parent = current
                neighbor.g_score = current.g_score
                neighbor.f_score = neighbor.g_score + h(neighbor)
                if not neighbor in open_set:
                    open_set.append(neighbor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for cell in grid.flatten():
            cell.draw(cell_width, cell_height, scr)
        current.draw_green(cell_width, cell_height, scr)
        pygame.display.update()
    if open_set == []:
        print("Failed in ", end="")
    else:
        print("Done in ", end="")
    print(time() - s, end=" seconds\n")

par = current
while True:
    while True:
        try:
            path.append(par)
            par = par.parent
        except:
            break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for cell in grid.flatten():
        cell.draw(cell_width, cell_height, scr)
    for cell in path:
        if cell is not None:
            cell.draw_green(cell_width, cell_height, scr)
    pygame.display.update()