import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 32
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells3(self):
        num_cols = 4
        num_rows = 2
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit1(self):
        num_cols = 1
        num_rows = 1
        m = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertEquals(m._cells[0][0].has_top_wall, False)
        self.assertEquals(m._cells[0][0].has_bottom_wall, False)

    def test_maze_break_entrance_and_exit2(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        self.assertFalse(m._cells[0][0].has_top_wall)
        self.assertFalse(m._cells[9][9].has_bottom_wall)

    def test_reset_all_visited(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_cols, num_rows, 10, 10, None)
        for col in m._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == '__main__':
    unittest.main()