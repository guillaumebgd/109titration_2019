# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## check_pH_values.py
##

def check_pH_values(stock: str) :
    try :
        stock = float(stock)
    except :
        return False
    if not 0 < stock < 14 :
        return False
    return True