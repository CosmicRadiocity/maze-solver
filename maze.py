from cell import Cell
import time
import random

class Maze():
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        if seed != None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self.cells = []
        for i in range(0, self.num_rows):
            list = []
            for j in range(0, self.num_cols):
                new_x1 = self.x1 + j * self.cell_size_x
                new_y1 = self.y1 + i * self.cell_size_y
                new_x2 = new_x1 + self.cell_size_x
                new_y2 = new_y1 + self.cell_size_y
                list.append(Cell(new_x1, new_y1, new_x2, new_y2, self._win))
            self.cells.append(list)
        
        if self._win != None:
            for cell_list in self.cells:
                for cell in cell_list:
                    self._draw_cell(cell)
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()
        

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        exit = self.cells[-1][-1]
        entrance.has_left_wall = False
        exit.has_right_wall = False
        self._draw_cell(entrance)
        self._draw_cell(exit)
        
    def _break_walls_r(self, i, j):
        current = self.cells[i][j]
        self.cells[i][j].visited = True
        while True:
            directions = []
            bottom = None
            top = None
            right = None
            left = None
            if i < len(self.cells) - 1:
                bottom = self.cells[i + 1][j]
                if not bottom.visited:
                    directions.append(bottom)
            if i > 0:
                top = self.cells[i-1][j]
                if not top.visited:
                    directions.append(top)
            if j > 0:
                left = self.cells[i][j-1]
                if not left.visited:
                    directions.append(left)
            if j < len(self.cells[i]) - 1:
                right = self.cells[i][j+1]
                if not right.visited:
                    directions.append(right)
            
            if len(directions) == 0:
                self._draw_cell(current)
                return current
            
            next_cell = directions[random.randrange(0, len(directions))]

            if next_cell == bottom:
                current.has_bottom_wall = False
                next_cell.has_top_wall = False
                self._draw_cell(current)
                self._draw_cell(next_cell)
                self._break_walls_r(i+1, j)
            elif next_cell == top:
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
                self._draw_cell(current)
                self._draw_cell(next_cell)
                self._break_walls_r(i-1, j)
            elif next_cell == left:
                current.has_left_wall = False
                next_cell.has_right_wall = False
                self._draw_cell(current)
                self._draw_cell(next_cell)
                self._break_walls_r(i, j-1)
            elif next_cell == right:
                current.has_right_wall = False
                next_cell.has_left_wall = False
                self._draw_cell(current)
                self._draw_cell(next_cell)
                self._break_walls_r(i, j+1)

    def _reset_cells_visited(self):
        for cell_list in self.cells:
            for cell in cell_list:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        current = self.cells[i][j]
        self.cells[i][j].visited = True
        if current == self.cells[-1][-1]:
            return True
        bottom = None
        top = None
        right = None
        left = None
        if i < len(self.cells) - 1 and not current.has_bottom_wall:
            bottom = self.cells[i + 1][j]
            if not bottom.visited:
                current.draw_move(bottom)
                if self._solve_r(i+1, j):
                    return True
                else:
                    current.draw_move(bottom, True)
        if i > 0 and not current.has_top_wall:
            top = self.cells[i-1][j]
            if not top.visited:
                current.draw_move(top)
                if self._solve_r(i-1, j):
                    return True
                else:
                    current.draw_move(top, True)
        if j > 0 and not current.has_left_wall:
            left = self.cells[i][j-1]
            if not left.visited:
                current.draw_move(left)
                if self._solve_r(i, j-1):
                    return True
                else:
                    current.draw_move(left, True)
        if j < len(self.cells[i]) - 1 and not current.has_right_wall:
            right = self.cells[i][j+1]
            if not right.visited:
                current.draw_move(right)
                if self._solve_r(i, j+1):
                    return True
                else:
                    current.draw_move(right, True)

        return False

        
