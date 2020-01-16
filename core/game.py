#!/usr/bin/env python3

import numpy as np
from itertools import cycle
import random
from core.board import SquareBoard, SquareField
from core.util import Direction

class InvalidMoveError(Exception):
    pass

class SquareGame():

    NUM_ATOMS=4

    def __init__(self):
        self.board = SquareBoard()
        self.place_atoms()
        # Assign labels "A" to "Z" for probes
        self._labels = map(chr, cycle(range(65,91)))

    def place_atoms(self):
        #for fld in random.sample(self.board.inner, self.NUM_ATOMS):
        #    fld.data = "ATOM"
        self.board.data[3][5].data = "ATOM"
        self.board.data[3][6].data = "ATOM"
        self.board.data[1][6].data = "ATOM"
        self.board.data[8][3].data = "ATOM"

    def draw(self, stdscr):
        self.board.draw(stdscr, 0, 0)

    def is_blocked(self, y, x):
        if not self.board.is_valid(y, x):
            raise ValueError()
        return self.board.data[y][x].data == "ATOM"

    def is_dir_blocked(self, y, x, y_dir, x_dir):
        return self.is_blocked(y+y_dir, x+x_dir)

    def is_cw_corner_blocked(self, y, x, y_dir, x_dir):
        y_dir, x_dir = Direction.rotate_dir_cw_45(y_dir, x_dir)
        return self.is_dir_blocked(y, x, y_dir, x_dir)

    def is_ccw_corner_blocked(self, y, x, y_dir, x_dir):
        y_dir, x_dir = Direction.rotate_dir_ccw_45(y_dir, x_dir)
        return self.is_dir_blocked(y, x, y_dir, x_dir)

    def trace(self, y, x, y_dir, x_dir):
        self.board.data[y][x].data=" XX "
        if self.is_dir_blocked(y, x, y_dir, x_dir):
            return (None, None);
        if self.is_cw_corner_blocked(y, x, y_dir, x_dir) and \
           self.is_ccw_corner_blocked(y, x, y_dir, x_dir):
            y_dir, x_dir = Direction.flip_dir(y_dir, x_dir)
        if self.is_cw_corner_blocked(y, x, y_dir, x_dir):
            if self.board.is_border(y, x):
                return (y, x)
            else:
                y_dir, x_dir = Direction.rotate_dir_ccw(y_dir, x_dir)
        if self.is_ccw_corner_blocked(y, x, y_dir, x_dir):
            if self.board.is_border(y, x):
                return (y, x)
            else:
                y_dir, x_dir = Direction.rotate_dir_cw(y_dir, x_dir)
        if self.board.is_border(y+y_dir, x+x_dir):
            return (y+y_dir, x+x_dir)
        return self.trace(y+y_dir, x+x_dir, y_dir, x_dir)

    def set(self, y, x, data):
        self.board.data[y][x].data = data
