# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## is_str_int.py
##

def is_str_int(stock: str) :
    try :
        stock = int(stock)
    except :
        return False
    return True