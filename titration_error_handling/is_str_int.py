# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## is_str_int.py
##

def is_str_int(string: str) :
    try :
        string = int(string)
    except :
        return False
    return True