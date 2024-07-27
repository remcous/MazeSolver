from graphics import Window, Line, Point

def main():
    win = Window(800,600)
    l = Line(Point(0,0), Point(800,600))
    win.draw_line(l, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()