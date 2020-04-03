# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_equivalence_point.py
##

def print_equivalence_point(deriv: list, stock: list) :

    eq_pt = stock[1][0]
    pos_eq = 0

    for i in range(1, len(stock) - 1) :
        if deriv[i - 1] > eq_pt :
            eq_pt = stock[i][0]
            pos_eq = i - 1

    print("Equivalence point at %.1f ml" % eq_pt)
    return (pos_eq)