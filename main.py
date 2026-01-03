import time
import sys
import curses

# speed (sleep time)
wpm = 300
x, y = 800, 600

# sleep factor for puntuation
CM_INC = 2 # comma
CL_INC = 3 # colon
SC_INC = 3 # semicolon
DOT_INC = 4 # dot

def orp(c:str):
    l = len(c)
    if (l <= 0): return "", "", ""
    elif (l == 1): return "", c, ""
    elif (2 <= l <= 5): return c[:1], c[1], c[2:]
    elif (6 <= l <= 9): return c[:2], c[2], c[3:]
    elif (10 <= l <= 13): return c[:3], c[3], c[4:]
    else: return c[:4], c[4], c[5:]

RED = "\033[31m"
RESET = "\033[0m"

def orp_print(l, m, r, scr):
    y, x = scr.getmaxyx()
    curses.flushinp()
    scr.move(y//2, 0)
    scr.clrtoeol()   
    scr.addstr(y//2, x//2 - len(l), l)
    scr.addstr(y//2, x//2, m, curses.color_pair(1))
    scr.addstr(y//2, x//2 + 1, r)
    scr.refresh()

def read(text, wait, scr):
    for c in text.split():
        if (c.endswith(".")): 
              orp_print(*orp(c[:-1]), scr); time.sleep(DOT_INC * wait)
        elif (c.endswith(";")): 
              orp_print(*orp(c[:-1]), scr); time.sleep(SC_INC * wait)
        elif (c.endswith(":")): 
              orp_print(*orp(c), scr); time.sleep(CL_INC * wait)
        elif (c.endswith(",")): 
              orp_print(*orp(c[:-1]), scr); time.sleep(CM_INC * wait)
        else:
            orp_print(*orp(c), scr)
            time.sleep(wait)


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.curs_set(0)  

    while(len(sys.argv) > 1):
        orp_print(*orp("x"), stdscr)
        time.sleep(1)
        with open(sys.argv.pop(1), "r") as f:
              while(line := f.readline()):
                read(line, 60.0 / wpm, stdscr);
        print()

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass

    curses.curs_set(1)  
