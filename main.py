from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    start = Point(1, 1)
    end = Point(600, 600)
    line = Line(start, end)
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.has_bottom_wall = False
    cell1.has_top_wall = False
    cell2 = Cell(125, 125, 200, 200, win)
    cell1.draw("blue")
    cell2.draw("green")
    win.draw_line(line, "red")
    win.wait_for_close()

main()