# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_first_derivative.py
##

def print_first_derivative(first_deriv: list, stock: list) :

    print("Derivative:")

    for i in range(0, len(first_deriv)) :
        print("%.1fml -> %.2f" % (stock[i + 1][0], first_deriv[i]))