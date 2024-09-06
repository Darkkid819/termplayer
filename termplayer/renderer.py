import curses

def render_frame(stdscr, frame):
    stdscr.clear()
    stdscr.addstr(0, 0, frame)
    stdscr.refresh()
