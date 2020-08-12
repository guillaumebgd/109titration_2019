# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## reattribute_stock.py
##

def update_stock_to_derivative(stock: list, derivative: list):

    stock = (stock[:-1])[1:]

    for i in range(0, len(stock)) :
        stock[i][1] = derivative[i]

    return (stock)