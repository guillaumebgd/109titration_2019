# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## find_eq_pt.py
##

def find_eq_pt(stock: list) :
    pos_eq = 0
    for i in range(1, len(stock)) :
        if stock[i][1] > stock[pos_eq][1] :
            pos_eq = i
    return (pos_eq)