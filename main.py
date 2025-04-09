from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    maze = Maze(15, 15, 15, 15, 50, 50, win)
    maze.solve()
    win.wait_for_close()

main()