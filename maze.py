#!/usr/bin/env python

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

def get_shape(maze, x, y):
    val = maze[x][y]
    shape = Shape()
    cols = len(maze)
    rows = len(maze[0])

    if y + 1 < rows and maze[x][y+1] == val: shape.up = True
    if y > 0 and maze[x][y-1] == val: shape.down = True
    if x > 0 and maze[x-1][y] == val: shape.left = True
    if x + 1 < cols and maze[x+1][y] == val: shape.right = True

    return shape
