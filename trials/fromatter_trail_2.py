
import pygments
import pygments.lexers
import pygments.formatters
import curses

formatter_default = pygments.formatters.TerminalFormatter()

def highlight(code):
	lexer = pygments.lexers.get_lexer_by_name('python')
	return pygments.highlight(code, lexer, formatter_default)

STR = '''
def start(self):
    key = 0
    page_size = len(context)
    current_page = -1
'''

if __name__ == '__main__':

	stdscr = curses.initscr()
	curses.start_color()

	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	stdscr.addstr(3, 0, highlight(STR))
	stdscr.refresh()
	stdscr.getkey()
