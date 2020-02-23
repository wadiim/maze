from maze import Shape, get_shape, cell_to_string
import unittest

class GetShapeTest(unittest.TestCase):

    def test_inner_cell(self):
        maze = [[0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
        shape = Shape(down = True, right = True)
        self.assertEqual(get_shape(maze, x = 1, y = 2), shape)

    def test_outer_cell(self):
        maze = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 0]]
        shape = Shape(left = True, up = True)
        self.assertEqual(get_shape(maze, x = 3, y = 0), shape)

    def test_different_values(self):
        maze = [[3, 1, 5, 4],
                [2, 2, 2, 8],
                [0, 2, 6, 7],
                [1, 7, 1, 3]]
        shape = Shape(up = True, down = True, right = True)
        self.assertEqual(get_shape(maze, x = 1, y = 1), shape)

class CellToStringTest(unittest.TestCase):

    def test_empty_cell(self):
        maze = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '   ')

    def test_horizontal(self):
        maze = [[0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '───')

    def test_vertical(self):
        maze = [[0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' │ ')

    def test_down_and_right(self):
        maze = [[0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' ┌─')

    def test_down_and_left(self):
        maze = [[0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┐ ')

    def test_up_and_right(self):
        maze = [[0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' └─')

    def test_up_and_left(self):
        maze = [[0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┘ ')

    def test_vertical_and_right(self):
        maze = [[0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' ├─')

    def test_vertical_and_left(self):
        maze = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┤ ')

    def test_down_and_horizontal(self):
        maze = [[0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┬─')

    def test_up_and_horizontal(self):
        maze = [[0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┴─')

    def test_vertical_and_horizontal(self):
        maze = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '─┼─')

if __name__ == '__main__':
    unittest.main()