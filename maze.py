from cell import Cell
from time import sleep
import random

class Maze():
    def __init__(self,
                 x1,
                 y1, 
                 num_cols,
                 num_rows,
                 cell_size_x,
                 cell_size_y,
                 win,
                 seed=None,
                 ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        self._cells[i][j].draw(x1, y1, x1+self._cell_size_x, y1+self._cell_size_y)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_moves = []

            # find possible moves
            if i > 0 and not self._cells[i-1][j].visited:
                possible_moves.append("left")
                
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                possible_moves.append("right")

            if j > 0 and not self._cells[i][j-1].visited:
                possible_moves.append("up")

            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible_moves.append("down")

            if len(possible_moves) == 0:
                self._draw_cell(i,j)
                return
            
            chosen_move = possible_moves[random.randrange(len(possible_moves))]

            if chosen_move == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            elif chosen_move == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            elif chosen_move == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            elif chosen_move == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        directions = ["up", "right", "down", "left"]

        if i <= 0:
            directions.remove("left")
        if i >= self._num_cols - 1:
            directions.remove("right")
        if j <= 0:
            directions.remove("up")
        if j >= self._num_rows - 1:
            directions.remove("down")

        for direction in directions:
            if direction == "up" and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)
            elif direction == "right" and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)
            elif direction == "down" and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)
            elif direction == "left" and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        return False