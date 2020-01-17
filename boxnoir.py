#!/usr/bin/env python3

import re
import curses

from core.game import SquareGame
from core.view import View

def main(stdscr):
    curses.curs_set(0)

    the_game = SquareGame()
    the_view = View(the_game)
    solve_flag = False
    hints_flag = False
    status_text = "Hello!"

    def prompt_key(stdscr, status_text, prompt_text):
        stdscr.move(21, 0)
        stdscr.deleteln()
        stdscr.deleteln()
        stdscr.addstr(21, 0, status_text)
        stdscr.addstr(22, 0, prompt_text)
        return stdscr.getkey()

    while True:
        # Show board
        stdscr.erase()
        the_view.draw(stdscr, solve_flag, hints_flag)
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
            status_text = "See solution: {}".format(solve_flag)
        elif cmd == "h":          # (h)elp command
            hints_flag = not hints_flag
            status_text = "p = probe, s = toggle sol., " \
                "q = quit, h = help, r = reset"
        elif cmd == "r":           # (r)eset command
            the_game = SquareGame()
            the_view = View(the_game)
            solve_flag = False
            hints_flag = False
            status_text = "Reset done. Hello!"
        else:
            status_text = "Unknown commmand"

curses.wrapper(main)
