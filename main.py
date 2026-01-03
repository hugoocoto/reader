import time
import sys

# speed (sleep time)
wpm = 300

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

def orp_print(l, m, r):
        print(f" {l:>10}{RED}{m}{RESET}{r:<10}", end='\r')

def read(text, wait):
    for c in text.split():
        if (c.endswith(".")): orp_print(*orp(c[:-1])); time.sleep(DOT_INC * wait)
        elif (c.endswith(";")): orp_print(*orp(c[:-1])); time.sleep(SC_INC * wait)
        elif (c.endswith(":")): orp_print(*orp(c)); time.sleep(CL_INC * wait)
        elif (c.endswith(",")): orp_print(*orp(c[:-1])); time.sleep(CM_INC * wait)
        else:
            orp_print(*orp(c))
            time.sleep(wait)

def main():
    while(len(sys.argv) > 1):
        orp_print(*orp("x"))
        time.sleep(1)
        with open(sys.argv.pop(1), "r") as f:
              while(line := f.readline()):
                read(line, 60.0 / wpm);
        print()

if __name__ == '__main__':
    main()
