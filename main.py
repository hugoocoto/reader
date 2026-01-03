import time
import sys

wpm = 300

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
