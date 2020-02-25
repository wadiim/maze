from maze import Shape, get_shape, cell_to_string, maze_to_string, solve_maze
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

    def test_up(self):
        maze = [[0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' │ ')

    def test_down(self):
        maze = [[0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), ' │ ')

    def test_left(self):
        maze = [[0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '───')

    def test_right(self):
        maze = [[0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 1, y = 1), '───')

    def test_top_left_corner(self):
        maze = [[0, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 0, y = 3), ' ┌─')

    def test_top_right_corner(self):
        maze = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 1]]
        self.assertEqual(cell_to_string(maze, x = 3, y = 3), '─┐ ')

    def test_bottom_left_corner(self):
        maze = [[1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 0, y = 0), ' └─')

    def test_bottom_right_corner(self):
        maze = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0]]
        self.assertEqual(cell_to_string(maze, x = 3, y = 0), '─┘ ')

class MazeToStringTest(unittest.TestCase):

    def test_empty_maze(self):
        maze = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        str = ("            \n"
               "            \n"
               "            \n"
               "            ")
        self.assertEqual(maze_to_string(maze), str)

    def test_complex_maze(self):
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        str = (" ┌────    ┌──────────────┬─────┐ \n"
               " │        │              │     │ \n"
               " ├────    │     ┌────    │     │ \n"
               " │              │              │ \n"
               " │     ┌────────┴──┐    ───────┤ \n"
               " │     │           │           │ \n"
               " │     │     │     │     │     │ \n"
               " │           │     ├─────┼─────┤ \n"
               " │     ┌─────┘     │     │     │ \n"
               " │     │                       │ \n"
               " └─────┴────────────────   ────┘ ")
        self.assertEqual(maze_to_string(maze), str)

class SolveMazeTest(unittest.TestCase):

    def test_horizontal_single_path(self):
        maze =     [[1, 0, 1],
                    [1, 0, 1],
                    [1, 0, 1],
                    [1, 0, 1],
                    [1, 0, 1]]
        solution = [[1, 2, 1],
                    [1, 2, 1],
                    [1, 2, 1],
                    [1, 2, 1],
                    [1, 2, 1]]
        solve_maze(maze)
        self.assertEqual(maze, solution)

    def test_vertical_single_path(self):
        maze =     [[1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1]]
        solution = [[1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2],
                    [1, 1, 1, 1, 1]]
        solve_maze(maze)
        self.assertEqual(maze, solution)

    def test_curved_path(self):
        maze =     [[1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1]]
        solution = [[1, 1, 1, 1, 1],
                    [2, 2, 1, 2, 2],
                    [1, 2, 1, 2, 1],
                    [1, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1]]
        solve_maze(maze)
        self.assertEqual(maze, solution)

    def test_multiple_pathes(self):
        maze =     [[1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1]]
        solution = [[1, 1, 1, 1, 1],
                    [2, 2, 0, 0, 1],
                    [1, 2, 1, 1, 1],
                    [1, 2, 0, 0, 1],
                    [1, 2, 1, 1, 1]]
        solve_maze(maze)
        self.assertEqual(maze, solution)

    def test_complex_maze(self):
        maze =     [[1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 1]]
        solution = [[1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 2, 2, 2, 2],
                    [1, 1, 1, 2, 1, 1, 1],
                    [1, 0, 1, 2, 2, 2, 1],
                    [1, 0, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 1, 1]]
        solve_maze(maze, 2, 0)
        self.assertEqual(maze, solution)

if __name__ == '__main__':
    unittest.main()
