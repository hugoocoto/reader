from pypdf import PdfReader
from main import orp, orp_print, read
import curses
import sys
import time

wpm = 300

def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.curs_set(0)  
    startpage = 0

    while(len(sys.argv) > 1):
        if (sys.argv[1].isdecimal()):
            startpage = int(sys.argv.pop(1)) -1
            continue

        orp_print(*orp("x"), stdscr)
        time.sleep(1)

        with PdfReader(sys.argv.pop(1)) as f:
            for page in f.pages[startpage:]:
                read(page.extract_text(), 60.0 / wpm, stdscr);
        startpage = 0

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass

    curses.curs_set(1)  

