# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## print_second_derivative.py
##

def print_second_derivative(second_deriv: list, stock: list) :

    print("Second derivative:")

    for i in range(0, len(second_deriv)) :
        print("%.1fml -> %.2f" % (stock[i + 1][0], second_deriv[i]))