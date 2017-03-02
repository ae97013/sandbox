#!/usr/bin/env python3

import getopt
import sys
import pygame
import random

SCREENWIDTH = 1200
SCREENHEIGHT = 1200
SCREENBORDER = 100
CELLSIZE = 10
POINTSIZE = 5
NUMPOINTS = 100
FPS = 10

assert (SCREENWIDTH - 2 * SCREENBORDER) % CELLSIZE == 0
assert (SCREENHEIGHT - 2 * SCREENBORDER) % CELLSIZE == 0
assert CELLSIZE > POINTSIZE

GRIDWIDTH = (SCREENWIDTH - 2 * SCREENBORDER) // CELLSIZE
GRIDHEIGHT = (SCREENHEIGHT - 2 * SCREENBORDER) // CELLSIZE

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# 2D cross product of OA and OB vectors.
# If OAB makes a counter-clockwise turn return positive value.
# If OAB makes a clockwise turn return a negative value.
# if OA is collinear returns zero.
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist(o, a):
    return (a[0] - o[0])**2 + (a[1] - o[1])**2

def draw_point(screen, p):
    x = p[0] * CELLSIZE + SCREENBORDER
    y = p[1] * CELLSIZE + SCREENBORDER
    pygame.draw.circle(screen, BLACK, (x, y), POINTSIZE, 1)

def draw_points(screen, points):
    for p in points:
        draw_point(screen, p)

def draw_line(screen, a, b, color):
    a_x = a[0] * CELLSIZE + SCREENBORDER
    a_y = a[1] * CELLSIZE + SCREENBORDER
    b_x = b[0] * CELLSIZE + SCREENBORDER
    b_y = b[1] * CELLSIZE + SCREENBORDER
    pygame.draw.line(screen, color, (a_x, a_y), (b_x, b_y), 1)

def draw_hull(screen, hull, complete):
    p1 = hull[0]
    for p2 in hull[1:]:
        draw_line(screen, p1, p2, RED)
        p1 = p2
    if complete:
        draw_line(screen, p2, hull[0], RED)

#
# Computes the convex hull of a set of 2D points using the
# gift-wrapping algorithm. Outputs a list of vertices of the
# convex hull in counter-clockwise order, starting from the
# vertex with the lexicographically smallest coordinates.
#
def giftwrap(screen, clock, points):
    points = sorted(set(points))
    if len(points) <= 3:
        return points

    hull = []
    hullpoint = points[0]
    while True:
        hull.append(hullpoint)
        endpoint = points[0]
        for p in points[1:]:
            if endpoint == hullpoint:
                endpoint = p
            cp = cross(hullpoint, endpoint, p)
            if cp > 0:
                endpoint = p
            if cp == 0:
                if dist(hullpoint, p) > dist(hullpoint, endpoint):
                    endpoint = p
            # Animation
            screen.fill(WHITE)
            draw_points(screen, points)
            draw_hull(screen, hull, False)
            draw_line(screen, hullpoint, endpoint, BLACK)
            draw_line(screen, hullpoint, p, GREEN)
            pygame.display.update()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if endpoint == points[0]:
            break
        hullpoint = endpoint

    return hull

def usage():
    print("Usage: %s [--help] [--testcase] [--npoints N]" % sys.argv[0])
    sys.exit()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "htn:", ["help", "testcase", "npoints="])
    except getopt.GetoptError as err:
        print(err)
        usage()

    npoints = NUMPOINTS
    rand = True
    for o, a in opts:
        if o in ("-n", "--npoints"):
            npoints = int(a)
        elif o in ("-t", "--testcase"):
            rand = False
        elif o in ("-h", "--help"):
            usage()
        else:
            assert False, "unhandled option"

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("Convex Hull")

    if rand:
        points = [(random.randint(0, GRIDWIDTH), random.randint(0, GRIDHEIGHT)) for _ in range(npoints)]
        hull = giftwrap(screen, clock, points)
    else:
        points = [((i // 10) * 10, (i % 10) * 10) for i in range(100)]
        hull = giftwrap(screen, clock, points)
        assert hull == [(0, 0), (90, 0), (90, 90), (0, 90)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_points(screen, points)
        draw_hull(screen, hull, True)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
