# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## is_str_float.py
##

def is_str_positive_float(string: str) :
    try :
        string = float(string)
    except :
        return False
    return True if string >= 0 else False