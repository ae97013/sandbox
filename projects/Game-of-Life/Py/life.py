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
GRAY  = (192, 192, 192)

def grid_draw_cell(canvas, grid, cell):
    x = cell[0] * CELLSIZE
    y = cell[1] * CELLSIZE
    if grid[cell] == 0:
        color = WHITE
    else:
        color = BLACK
    pygame.draw.rect(canvas, color, (x, y, CELLSIZE, CELLSIZE))

def grid_draw(canvas, grid):
    for cell in grid:
        grid_draw_cell(canvas, grid, cell)
    for x in range(0, CANVASWIDTH, CELLSIZE):
        pygame.draw.line(canvas, GRAY, (x, 0), (x, CANVASHEIGHT))
    for y in range (0, CANVASHEIGHT, CELLSIZE):
        pygame.draw.line(canvas, GRAY, (0, y), (CANVASWIDTH, y))

def grid_allocate():
    return dict(((x,y), False) for x in range(GRIDWIDTH) for y in range(GRIDHEIGHT))

def grid_randomize(grid):
    for cell in grid:
        grid[cell] = bool(random.getrandbits(1))
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
                    if grid[ncell]:
                        neighbors += 1
    return neighbors

#
# At each generation, the following transitions occur:
# 1. Any live cell with fewer than two live neighbors dies, (underpopulation).
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies (overpopulation).
# 4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
#
def grid_is_cell_alive(alive, neighbors):
    if alive:
        if neighbors < 2 or neighbors > 3:
            return False
        else:
            return True
    else:
        if neighbors == 3:
            return True
        else:
            return False
#
# Compute next generation.
#
def grid_tick(grid):
    nextgrid = {}
    for cell in grid:
        neighbors = grid_neighbor_count(grid, cell)
        nextgrid[cell] = grid_is_cell_alive(grid[cell], neighbors)
    return nextgrid

def main():
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((CANVASWIDTH, CANVASHEIGHT))
    pygame.display.set_caption('Game of Life')
    canvas.fill(WHITE)

    grid = grid_allocate()
    grid = grid_randomize(grid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        grid_draw(canvas, grid)
        pygame.display.update()
        grid = grid_tick(grid)
        clock.tick(FPS)

if __name__== '__main__':
    main()
