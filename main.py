from window import Window
from line import Line, Point

def main():
    win = Window(800, 600)
    start = Point(1, 100)
    end = Point(10, 100)
    line = Line(start, end)
    win.draw_line(line, "red")
    win.wait_for_close()

main()