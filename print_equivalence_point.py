# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_equivalence_point.py
##

def print_equivalence_point(stock: list) :

    eq_pt = float(stock[0][0])
    pos_eq = 0

    for i in range(0, len(stock)) :
        if float(stock[i][1]) > eq_pt :
            eq_pt = float(stock[i][0])
            pos_eq = i

    print("Equivalence point at %.1f ml" % eq_pt)
    return (pos_eq)