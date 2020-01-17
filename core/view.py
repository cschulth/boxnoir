#!/usr/bin/env python3

import itertools as it
from core.game import SquareGame

class View():

    FIELD = ["┼────┼",
             "│    │",
             "┼────┼"]

    def __init__(self, game):
        self._game = game

    def draw(self, stdscr, atoms_visible=False):
        # Offsets for drawing tiled fields
        fsy, fsx = (len(View.FIELD)-1,
                len(View.FIELD[0])-1)
        # Draw fields one by one
        for (y, x) in it.product(range(1,9), repeat=2):
            self.draw_field(stdscr, fsy*y, fsx*x)
        if atoms_visible:
            for y_pos, x_pos in self._game.atoms:
                self.draw_field(stdscr, fsy*y_pos, fsx*x_pos, "ATOM")
        self.draw_labels(stdscr)

    def draw_labels(self, stdscr):
        """This function draws the individual labels for
        probe input and probe output coordinates. For each pair,
        a new letter is chosen from A..Z.
        """
        labels = map(chr, it.cycle(range(65,91)))
        # Offsets for drawing tiled fields
        fsy, fsx = (len(View.FIELD)-1,
                len(View.FIELD[0])-1)
        for start, end in self._game.probes:
            label = labels.__next__()
            y, x = start
            self.draw_field(stdscr, fsy*y, fsx*x, label + "in", False)
            # Check, if an end needs to be drawn. For absorbed
            # probes, the end is (None, None), so not drawn.
            if end != (None, None):
                y, x = end
                self.draw_field(stdscr, fsy*y, fsx*x, label + "out", False)

    def draw_field(self, stdscr, y, x, label=None, background=True):
        if(background):
            for y_offset, row in enumerate(View.FIELD):
                stdscr.addstr(y+y_offset, x, row)
        if label:
            stdscr.addnstr(y+1, x+1, label, 4)
