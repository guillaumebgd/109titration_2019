# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## titration.py
##

def deriv_stock(stock: list, i: int) :

    pHn_plus_1 = stock[i + 1][1]
    pHn_minus_1 = stock[i - 1][1]
    pHn = stock[i][1]
    Voln_plus_1 = stock[i + 1][0]
    Voln_minus_1 = stock[i - 1][0]
    Voln = stock[i][0]

    return (((pHn - pHn_minus_1) / (Voln - Voln_minus_1)) * ((Voln_plus_1 - Voln) / (Voln_plus_1 - Voln_minus_1))) + ((pHn_plus_1 - pHn) / (Voln_plus_1 - Voln) * ((Voln - Voln_minus_1) / (Voln_plus_1 - Voln_minus_1)))

def titration(stock: list) :

    result = [0] * (len(stock) - 2)

    for i in range(1, len(stock) - 1) :
        result[i - 1] = float(deriv_stock(stock, i))
    return result