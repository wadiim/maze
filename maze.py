#!/usr/bin/env python

import random

class Shape:

    def __init__(self, up = False, down = False, left = False, right = False):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Shape): return NotImplemented
        return (self.up == other.up and self.down == other.down and
                self.left == other.left and self.right == other.right)

class Cell:

    directions = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    opposite = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    def __init__(self):
        self.visited = False
        self.walls = {key: True for key in Cell.directions.keys()}

def get_shape(maze, x, y):
    val = maze[x][y]
    shape = Shape()
    cols = len(maze)
    rows = len(maze[0])

    if x == 0 and y == 0: shape.up = shape.right = True
    if x == 0 and y == rows - 1: shape.down = shape.right = True
    if x == cols - 1 and y == 0: shape.up = shape.left = True
    if x == cols - 1 and y == rows - 1: shape.down = shape.left = True

    if y + 1 < rows and maze[x][y+1] == val: shape.up = True
    if y > 0 and maze[x][y-1] == val: shape.down = True
    if x > 0 and maze[x-1][y] == val: shape.left = True
    if x + 1 < cols and maze[x+1][y] == val: shape.right = True

    return shape

def cell_to_string(maze, x, y):
    if maze[x][y] == 0: return '   '

    shape = get_shape(maze, x, y)

    if shape.up and shape.down and shape.left and shape.right: return '─┼─'

    if shape.up and shape.down and shape.right: return ' ├─'
    if shape.up and shape.down and shape.left: return '─┤ '
    if shape.down and shape.left and shape.right: return '─┬─'
    if shape.up and shape.left and shape.right: return '─┴─'

    if shape.down and shape.right: return ' ┌─'
    if shape.down and shape.left: return '─┐ '
    if shape.up and shape.right: return ' └─'
    if shape.up and shape.left: return '─┘ '

    if shape.up or shape.down: return ' │ '
    if shape.left or shape.right: return '───'

def maze_to_string(maze):
    cols = len(maze)
    rows = len(maze[0])

    return '\n'.join([''.join([str(cell_to_string(maze, x, y))
           for x in range(cols)])
           for y in range(rows-1, -1, -1)])

def is_valid(grid, x, y):
    return (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and
            grid[x][y].visited == False)

def generate_grid(grid, x = 0, y = 0):
    grid[x][y].visited = True
    for key in random.sample(list(Cell.directions.keys()),
                             len(Cell.directions)):
        dx, dy = Cell.directions[key]
        if not is_valid(grid, x + dx, y + dy): continue
        grid[x][y].walls[key] = False
        grid[x+dx][y+dy].walls[Cell.opposite[key]] = False
        generate_grid(grid, x + dx, y + dy)

def map_coord(c):
    return 2*c + 1

def grid_cell_to_maze_cell(grid, maze, x, y):
    maze[map_coord(x)][map_coord(y)] = 0
    for key in Cell.directions.keys():
        dx, dy = Cell.directions[key]
        if grid[x][y].walls[key]: continue
        maze[map_coord(x) + dx][map_coord(y) + dy] = 0

def grid_to_maze(grid, maze):
    cols = len(grid)
    rows = len(grid[0])
    for i in range(cols):
        for j in range(rows):
            grid_cell_to_maze_cell(grid, maze, i, j)

def make_entry_and_exit(maze):
    maze[-2][0] = maze[0][-2] = 0

def generate_maze(rows, cols):
    grid = [[Cell() for i in range(rows)] for j in range(cols)]
    generate_grid(grid)
    mrows = map_coord(rows)
    mcols = map_coord(cols)
    maze = [[1 for i in range(mrows)] for j in range(mcols)]
    grid_to_maze(grid, maze)
    make_entry_and_exit(maze)
    return maze
