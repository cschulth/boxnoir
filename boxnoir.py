#!/usr/bin/env python3

import curses

from core.game import SquareGame

def main(stdscr):
    curses.curs_set(0)
    the_game = SquareGame()

    y_out, x_out = the_game.trace(2,0,0,1)
    l = the_game._labels.__next__()
    the_game.set(2, 0, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    y_out, x_out = the_game.trace(3,0,0,1)
    l = the_game._labels.__next__()
    the_game.set(3, 0, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    y_out, x_out = the_game.trace(2,9,0,-1)
    l = the_game._labels.__next__()
    the_game.set(2, 9, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    y_out, x_out = the_game.trace(4,0,0,1)
    l = the_game._labels.__next__()
    the_game.set(4, 0, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    y_out, x_out = the_game.trace(9,2,-1,0)
    l = the_game._labels.__next__()
    the_game.set(9, 2, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    y_out, x_out = the_game.trace(9,4,-1,0)
    l = the_game._labels.__next__()
    the_game.set(9, 4, l + "in")
    if y_out != None and x_out != None:
        the_game.set(y_out, x_out, l + "out")

    while True:
        stdscr.clear()
        the_game.draw(stdscr)
        stdscr.addstr(22, 0, "Command? ")
        stdscr.refresh()

        curses.echo()
        curses.curs_set(1)
        cmd = stdscr.getstr()
        curses.noecho()
        curses.curs_set(0)

curses.wrapper(main)
