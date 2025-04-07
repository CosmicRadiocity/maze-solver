from line import Line, Point

class Cell():

    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self, fill_color="black"):
        top_left = Point(self._x1, self._y1)
        print(top_left.x, top_left.y)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), fill_color)
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), fill_color)
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right), fill_color)

    def draw_move(self, to_cell, undo=False):
        center_self = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        print(center_self.x, center_self.y)
        center_target = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        print(center_target.x, center_target.y)
        fill_color = "gray"
        if undo:
            fill_color = "red"
        self._win.draw_line(Line(center_self, center_target), fill_color)
