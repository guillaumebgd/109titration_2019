# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## reattribute_stock.py
##

def reattribute_stock(stock: list, first_deriv: list) :
    stock = (stock[:-1])[1:]
    for i in range(0, len(stock)) :
        stock[i][1] = first_deriv[i]
    return (stock)