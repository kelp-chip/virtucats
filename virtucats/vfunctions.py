import time
import sys

def pause(enter, secs, nline):
    if nline == 1:
        print("\n")
    print(".", end="")
    time.sleep(secs)
    print(".", end="")
    time.sleep(secs)
    if enter == 1:
        input(".")
    elif enter == 0:
        print(".", end="")
        time.sleep(secs)


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)