# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## linar_interpolation.py
##

import sys

def taylors_interpolation_process(xa: float, xb: float, ya: float, yb: float, x: float):
    result = 0
    try:
        result = ya + (x - xa) * ((yb - ya) / (xb - xa))
    except:
        sys.exit(84)
    return result

def linear_interpolation(estimation: list, a: list, b: list, increaser: float):

    i = 0
    x = a[0]

    if increaser == 0:
        return False
    while i < int((b[0] - a[0]) / increaser):
        estimation.append([x, taylors_interpolation_process(a[0], b[0], a[1], b[1], x)])
        x += increaser
        i += 1
    return True