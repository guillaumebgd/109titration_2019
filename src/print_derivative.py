# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_derivative.py
##

def print_derivative(stock: list) :

    for i in range(0, len(stock)) :
        print("%.1f ml -> %.2f" % (stock[i][0], stock[i][1]))