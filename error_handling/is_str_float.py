# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## is_str_float.py
##

def is_str_float(stock: str) :
    try :
        stock = float(stock)
    except :
        return False
    return True