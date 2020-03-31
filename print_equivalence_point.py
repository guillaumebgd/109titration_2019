# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_equivalence_point.py
##

def print_equivalence_point(deriv: list, stock: list, offset: int) :

    eq_pt = 0

    for i in range(0, len(deriv)) :
        if deriv[i] > eq_pt :
            eq_pt = i

    print("Equivalence point at %.1fml" % stock[eq_pt + offset][0])