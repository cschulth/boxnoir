#!/usr/bin/env python3

import itertools as it
import random
from core.util import Direction

class SquareGame():
    """This class implements the game mechanic

    .. note:: All directions are tuples (y_dir, x_dir) where
    the y_dir and x_dir are -1, 0 or 1. So there are 8 legal
    directions.
    """

    SIZE=10
    NUM_ATOMS=4

    def __init__(self):
        #self._atoms = random.sample(list(
        #    it.product(range(1,9), repeat=2)), NUM_ATOMS)
        self.atoms = [(3, 5), (3, 6), (1, 6), (8, 3)]
        self.probes = []

    def is_valid(self, y, x):
        if y<0 or y>=self.SIZE: return False
        if x<0 or x>=self.SIZE: return False
        return True

    def is_border(self, y, x):
        if y in [0, self.SIZE-1] or \
           x in [0, self.SIZE-1]:
            return True
        return False

    def is_blocked(self, y, x):
        if not self.is_valid(y, x):
            raise ValueError()
        return (y, x) in self.atoms

    def is_dir_blocked(self, y, x, y_dir, x_dir):
        return self.is_blocked(y+y_dir, x+x_dir)

    def is_cw_corner_blocked(self, y, x, y_dir, x_dir):
        y_dir, x_dir = Direction.rotate_dir_cw_45(y_dir, x_dir)
        return self.is_dir_blocked(y, x, y_dir, x_dir)

    def is_ccw_corner_blocked(self, y, x, y_dir, x_dir):
        y_dir, x_dir = Direction.rotate_dir_ccw_45(y_dir, x_dir)
        return self.is_dir_blocked(y, x, y_dir, x_dir)

    def probe(self, y, x):
        if y == 0 and x in range(1,9):
            y_dir, x_dir = (1, 0)
        elif y == 9 and x in range(1,9):
            y_dir, x_dir = (-1, 0)
        elif y in range(1,9) and x == 0:
            y_dir, x_dir = (0, 1)
        elif y in range(1,9) and x == 9:
            y_dir, x_dir = (0, -1)
        else:
            raise ValueError("Bad coordinates: {}, {}".format(y,x))
        self.probes.append([(y,x), self.trace(y, x, y_dir, x_dir)])

    def trace(self, y, x, y_dir, x_dir):
        """Returns the output coordinates for a ray

        Follows the rules for absorption and reflection of the
        original BlackBox game, rectangular version.

        :param y: starting point, y coordinate
        :param x: starting point, x coordinate:
        :param y_dir: starting direction, y coordinate
        :param x_dir: starting direction, x coordinate
        :return: output coordinates as tuple (y, x)
        """
        if self.is_dir_blocked(y, x, y_dir, x_dir):
            return (None, None);
        if self.is_cw_corner_blocked(y, x, y_dir, x_dir) and \
           self.is_ccw_corner_blocked(y, x, y_dir, x_dir):
            y_dir, x_dir = Direction.flip_dir(y_dir, x_dir)
        if self.is_cw_corner_blocked(y, x, y_dir, x_dir):
            if self.is_border(y, x):
                return (y, x)
            else:
                y_dir, x_dir = Direction.rotate_dir_ccw(y_dir, x_dir)
        if self.is_ccw_corner_blocked(y, x, y_dir, x_dir):
            if self.is_border(y, x):
                return (y, x)
            else:
                y_dir, x_dir = Direction.rotate_dir_cw(y_dir, x_dir)
        if self.is_border(y+y_dir, x+x_dir):
            return (y+y_dir, x+x_dir)
        return self.trace(y+y_dir, x+x_dir, y_dir, x_dir)
