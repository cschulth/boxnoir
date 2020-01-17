#!/usr/bin/env python3

import cmath

class Direction():

    @staticmethod
    def is_valid_dir(y_dir, x_dir):
        if y_dir == 0 and x_dir == 0:
            return False
        return y_dir in [-1,0,1] and x_dir in [-1,0,1]

    @staticmethod
    def rotate_dir_ccw(y_dir, x_dir):
        # Rotate the given direction by 90 degrees
        assert Direction.is_valid_dir(y_dir, x_dir)
        complex_dir = y_dir + x_dir*1j
        complex_dir = complex_dir*1j
        return (round(complex_dir.real), round(complex_dir.imag))

    @staticmethod
    def rotate_dir_cw(y_dir, x_dir):
        # Rotate the given direction by -90 degrees
        assert Direction.is_valid_dir(y_dir, x_dir)
        complex_dir = y_dir + x_dir*1j
        complex_dir = complex_dir/1j
        return (round(complex_dir.real), round(complex_dir.imag))

    @staticmethod
    def rotate_dir_ccw_45(y_dir, x_dir):
        # Rotate the given direction by 45 degrees
        assert Direction.is_valid_dir(y_dir, x_dir)
        complex_dir = y_dir + x_dir*1j
        complex_dir = complex_dir*cmath.sqrt(1j)
        return (round(complex_dir.real), round(complex_dir.imag))

    @staticmethod
    def rotate_dir_cw_45(y_dir, x_dir):
        # Rotate the given direction by -45 degrees
        assert Direction.is_valid_dir(y_dir, x_dir)
        complex_dir = y_dir + x_dir*1j
        complex_dir = complex_dir/cmath.sqrt(1j)
        return (round(complex_dir.real), round(complex_dir.imag))

    @staticmethod
    def flip_dir(y_dir, x_dir):
        # Rotate the given direction by 180 degrees
        assert Direction.is_valid_dir(y_dir, x_dir)
        return (-y_dir, -x_dir)
