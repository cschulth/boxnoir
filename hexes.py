#!/usr/bin/env python3

from itertools import *

from core.board import RectBoard

def print_hexes(n=3):
    fld_gen = count()
    for row in range(2*n+1):
        indent = abs(row-n)
        print(indent*"  ", end="")
        cols = range(2*n+1 -indent)
        flds = [ fld_gen.__next__() for _ in cols ]
        print("  ".join([ "{:02d}".format(fld) for fld in flds ]))
        print("")
    return

def print_hexes_xy(n=7):
    all = product(range(n), range(n))
    flds = filter(lambda s: sum(s) in range(n//2, n+n//2), all)
    print(list(flds))

#print_hexes_xy()

if __name__ == "__main__":
    SIZE = 8
    NATOMS = 4
    board = RectBoard(SIZE, NATOMS)
    while True:
        print("command?")
        inp = input().split()
        if inp == []:
            continue
        if inp[0] == "p":
            pos = tuple(map(int, inp[1:3]))
            print(list(board.step(start_pos=pos)))
        if inp[0] == "q":
            break

