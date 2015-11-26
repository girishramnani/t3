import curses
stdscr = curses.initscr()

def curses_up():
    """
    all the initallization of the curses here

    """
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def curses_down():
    """
    function to get everything back to normal
    """
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

