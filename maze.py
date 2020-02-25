#!/usr/bin/env python

import sys
import random
import argparse

if sys.version[0] == '2': input = raw_input

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
        self.path = False
        self.visited = False
        self.walls = {key: True for key in Cell.directions.keys()}

def get_shape(maze, x, y):
    val = maze[x][y]
    shape = Shape()
    rows = len(maze)
    cols = len(maze[0])

    if x == 0 and y == 0: shape.up = shape.right = True
    if x == 0 and y == cols - 1: shape.down = shape.right = True
    if x == rows - 1 and y == 0: shape.up = shape.left = True
    if x == rows - 1 and y == cols - 1: shape.down = shape.left = True

    if y + 1 < cols and maze[x][y+1] == val: shape.up = True
    if y > 0 and maze[x][y-1] == val: shape.down = True
    if x > 0 and maze[x-1][y] == val: shape.left = True
    if x + 1 < rows and maze[x+1][y] == val: shape.right = True

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
    rows = len(maze)
    cols = len(maze[0])

    return '\n'.join([''.join([str(cell_to_string(maze, x, y))
           for x in range(rows)])
           for y in range(cols-1, -1, -1)])

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
    mx, my = map_coord(x), map_coord(y)
    maze[map_coord(x)][map_coord(y)] = 0 if not grid[x][y].path else 2
    for key in Cell.directions.keys():
        dx, dy = Cell.directions[key]
        if grid[x][y].walls[key]: continue
        if (grid[x][y].path and
            ((mx + dx == 0 or mx + dx == len(maze) - 1 or
            my + dy == 0 or my + dy == len(maze[0]) - 1) or
            (x + dx >= 0 and x + dx < len(grid) and
            y + dy >= 0 and y + dy < len(grid[0]) and
            grid[x + dx][y + dy].path))): maze[mx + dx][my + dy] = 2
        else: maze[mx + dx][my + dy] = 0

def maze_cell_to_grid_cell(grid, maze, x, y):
    for key in Cell.directions.keys():
        dx, dy = Cell.directions[key]
        if maze[map_coord(x) + dx][map_coord(y) + dy] == 1: continue
        grid[x][y].walls[key] = False

def for_each_grid_cell(grid, func, *args):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols): func(i, j, *args)

def grid_to_maze(grid, maze):
    for_each_grid_cell(grid,
        lambda x, y: grid_cell_to_maze_cell(grid, maze, x, y))

def maze_to_grid(grid, maze):
    for_each_grid_cell(grid,
        lambda x, y: maze_cell_to_grid_cell(grid, maze, x, y))

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

def is_exit(grid, x, y):
    return (is_valid(grid, x, y) and
            x == 0 and not grid[x][y].walls['W'] or
            x == len(grid) - 1 and not grid[x][y].walls['E'] or
            y == 0 and not grid[x][y].walls['S'] or
            y == len(grid[0]) - 1 and not grid[x][y].walls['N'])

def solve_grid(grid, x = 0, y = 0):
    grid[x][y].visited = True
    for (key, val) in Cell.directions.items():
        if grid[x][y].walls[key] == True: continue
        dx, dy = val
        if (not is_valid(grid, x + dx, y + dy) or
            grid[x + dx][y + dy].visited): continue
        if is_exit(grid, x + dx, y + dy):
            grid[x + dx][y + dy].path = True
            grid[x][y].path = True
            return True
        if solve_grid(grid, x + dx, y + dy):
            grid[x][y].path = True
            return True
    return False

def find_entry(maze):
    rows = len(maze)
    cols = len(maze[0])

    for x in range(rows):
        if maze[x][0] == 0: return (x, 0)
        if maze[x][-1] == 0: return (x, cols - 1)
    for y in range(cols):
        if maze[0][y] == 0: return (0, y)
        if maze[-1][y] == 0: return (rows - 1, y)

def solve_maze(maze):
    grid = [[Cell() for i in range(1, len(maze[0]), 2)]
        for j in range(1, len(maze), 2)]
    if len(grid[0]) == 1 or len(grid) == 1:
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == 0: maze[x][y] = 2
    else:
        maze_to_grid(grid, maze)
        x, y = find_entry(maze)
        x, y = ((x - 1) if x else x) // 2, ((y - 1) if y else y) // 2
        solve_grid(grid, x, y)
        grid_to_maze(grid, maze)

def print_maze(maze):
    print('\n'.join([''.join([str(i) for i in row]) for row in maze]))

def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--solve', action = 'store_true',
        help = 'solve maze')
    group.add_argument('-g', '--generate', type = int, nargs = 2,
        metavar = ('rows', 'cols'),
        help = 'generate maze')
    parser.add_argument("--pretty", help = 'pretty-print the results',
        action="store_true")
    return parser.parse_args()

def main():
    args = parse_args()
    if args.generate:
        rows, cols = args.generate;
        if args.pretty: print(maze_to_string(generate_maze(rows, cols)))
        else: print_maze(generate_maze(cols, rows))
    else:
        maze = []
        try:
            line = ''
            while True:
                line = input()
                maze.append([int(i) for i in line])
        except EOFError: pass
        if args.solve: solve_maze(maze)
        if args.pretty: print(maze_to_string(maze))
        else: print_maze(maze)

if __name__ == '__main__':
	main()
