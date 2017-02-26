#!/usr/bin/env python3

import sys
import pygame
import random

CANVASWIDTH = 800
CANVASHEIGHT = 800
CELLSIZE = 10

assert CANVASWIDTH % CELLSIZE == 0
assert CANVASHEIGHT % CELLSIZE == 0

GRIDWIDTH = CANVASWIDTH // CELLSIZE
GRIDHEIGHT = CANVASHEIGHT // CELLSIZE

FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (40, 40, 40)

def grid_draw_cell(grid, cell):
    x = cell[0] * CELLSIZE
    y = cell[1] * CELLSIZE
    if grid[cell] == 0:
        color = WHITE
    else:
        color = BLACK
    pygame.draw.rect(canvas, color, (x, y, CELLSIZE, CELLSIZE))
    return None

def grid_draw(grid):
    for cell in grid:
        grid_draw_cell(grid, cell)
    for x in range(0, CANVASWIDTH, CELLSIZE):
        pygame.draw.line(canvas, GRAY, (x, 0), (x, CANVASHEIGHT))
    for y in range (0, CANVASHEIGHT, CELLSIZE):
        pygame.draw.line(canvas, GRAY, (0, y), (CANVASWIDTH, y))

def grid_allocate():
    return dict(((x,y), 0) for x in range(GRIDWIDTH) for y in range(GRIDHEIGHT))

def grid_randomize(grid):
    for i in grid:
        grid[i] = random.randint(0,1)
    return grid

def grid_neighbor_count(grid, cell):
    neighbors = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            ncell = (cell[0] + x, cell[1] + y)
            if ncell[0] >= 0 and ncell[0] < GRIDWIDTH:
                if ncell[1] >= 0 and ncell[1] < GRIDHEIGHT:
                    if grid[ncell] == 1:
                        neighbors += 1
    return neighbors

#
# Compute next generation.
#
def grid_tick(grid):
    grid_nextgen = {}
    for cell in grid:
        neighbors = grid_neighbor_count(grid, cell)
        if grid[cell] == 1:
            if neighbors < 2 or neighbors > 3:
                grid_nextgen[cell] = 0
            else:
                grid_nextgen[cell] = 1
        elif grid[cell] == 0:
            if neighbors == 3:
                grid_nextgen[cell] = 1
            else:
                grid_nextgen[cell] = 0
    return grid_nextgen

def main():
    global canvas

    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((CANVASWIDTH, CANVASHEIGHT))
    pygame.display.set_caption('Game of Life')
    canvas.fill(WHITE)

    grid = grid_allocate()
    grid = grid_randomize(grid)
    grid_draw(grid)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        grid = grid_tick(grid)
        grid_draw(grid)
        pygame.display.update()
        clock.tick(FPS)

if __name__== '__main__':
    main()
