from curses import wrapper
import curses
from t3.screen import WrappingPoint
from t3.formatter import PlainFormatter


def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.cbreak()
    curses.start_color()
    stdscr.clear()
    stdscr.move(0,0)
    stdscr.refresh()
    y,x= stdscr.getyx()
    location  = WrappingPoint(stdscr.getmaxyx(),x=x,y=y)
    formatter = PlainFormatter("import this",direct=True,language="python")
    stdscr.addstr(formatter.format())
    stdscr.move(0,0)

    while True:
        current = stdscr.getkey()
        if current == 'q':
            break
        else:
            on_screen_char = stdscr.instr(1).decode()
            cp = 2 if on_screen_char == current else 1
            stdscr.addstr(on_screen_char,curses.color_pair(cp))

            location.x +=1
            if location.old.x==location.size.x-1 and location.x==0:
                location.y+=1
            stdscr.move(location.y,location.x)

        stdscr.refresh()


wrapper(main)
