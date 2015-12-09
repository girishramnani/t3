from curses import wrapper
import curses
from t3.screen import WrappingPoint
curses.initscr()
curses.cbreak()



def main(stdscr):
    stdscr.clear()

    stdscr.move(0,0)
    stdscr.refresh()
    y,x= stdscr.getyx()
    location  = WrappingPoint(stdscr.getmaxyx(),x=x,y=y)
    while True:
        current = stdscr.getkey()
        if current == 'q':
            break
        else:
            location.y +=1
            if location.old.y==location.size.y-1 and location.y==0:
            	location.x+=1
            stdscr.move(location.y,location.x)
            stdscr.addstr(current)

            

        stdscr.refresh()


wrapper(main)

