from curses import wrapper
import curses
from t3.screen import WrappingPoint
from t3.formatter import Formatter


def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
    curses.cbreak()
    curses.start_color()
    stdscr.clear()
    stdscr.move(0,0)
    stdscr.refresh()
    y,x= stdscr.getyx()
    location  = WrappingPoint(stdscr.getmaxyx(),x=x,y=y)
    formatter = Formatter("import this",direct=True,language="python")
    stdscr.addstr(formatter.format())
    stdscr.move(0,0)

    while True:
        current = stdscr.getkey()
        if current == 'q':
            break
        else:
            location.x +=1
            if location.old.x==location.size.x-1 and location.x==0:
            	location.y+=1
            stdscr.move(location.y,location.x)
            stdscr.addstr(current,curses.color_pair(1))

            

        stdscr.refresh()


wrapper(main)
