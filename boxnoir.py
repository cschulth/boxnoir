#!/usr/bin/env python3

import re
import curses

from core.game import SquareGame
from core.view import View

def main(stdscr):
    curses.curs_set(0)
    the_game = SquareGame()
    the_view = View(the_game)

    # the_game.probe(2,0)
    # the_game.probe(3,0)
    # the_game.probe(2,9)
    # the_game.probe(4,0)
    # the_game.probe(9,2)
    # the_game.probe(9,4)

    solve_flag = False
    status_text = "Hello!"

    while True:
        # Show board
        stdscr.erase()
        the_view.draw(stdscr, solve_flag)
        stdscr.refresh()

        # Handle inputs
        cmd = prompt_key(stdscr, status_text, "Command?")
        if cmd == "q":            # (q)uit command
            break
        elif cmd == "p":          # (p)robe command
            y = prompt_key(stdscr, "Probe", "Y?")
            x = prompt_key(stdscr, "Probe", "X?")
            try:
                the_game.probe(int(y), int(x))
            except Exception as e:
                status_text = e.__str__()
            status_text = "Done"
        elif cmd == "s":          # (s)olve command
            solve_flag = not solve_flag
            status_text = "Done"
        elif cmd == "h":          # (h)elp command
            status_text = "p = probe, s = toggle solution, " \
                "q = quit, h = help"
        else:
            status_text = "Unknown commmand"

def prompt_key(stdscr, status_text, prompt_text):
    stdscr.move(21, 0)
    stdscr.deleteln()
    stdscr.deleteln()
    stdscr.addstr(21, 0, status_text)
    stdscr.addstr(22, 0, prompt_text)
    return stdscr.getkey()

curses.wrapper(main)
