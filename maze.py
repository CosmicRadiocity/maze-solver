from cell import Cell
import time

class Maze():
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
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

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)