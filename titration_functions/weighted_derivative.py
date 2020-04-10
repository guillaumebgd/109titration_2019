# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## weighted_derivative.py
##

def deriv_stock(point_list: list, index: int) :

    pHn_plus_1 = point_list[index + 1][1]
    pHn_minus_1 = point_list[index - 1][1]
    pHn = point_list[index][1]
    Voln_plus_1 = point_list[index + 1][0]
    Voln_minus_1 = point_list[index - 1][0]
    Voln = point_list[index][0]

    left_d = (pHn - pHn_minus_1) / (Voln - Voln_minus_1)
    right_d = (pHn_plus_1 - pHn) / (Voln_plus_1 - Voln)

    return (left_d * ((Voln_plus_1 - Voln) / (Voln_plus_1 - Voln_minus_1))) + (right_d * ((Voln - Voln_minus_1) / (Voln_plus_1 - Voln_minus_1)))

def weighted_derivative(point_list: list) :

    deriv = [0] * (len(point_list) - 2)

    for i in range(1, len(point_list) - 1):
        deriv[i - 1] = float(deriv_stock(point_list, i))
    return deriv