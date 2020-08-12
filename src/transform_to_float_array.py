# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## transform_to_float_array.py
##

from src.error_handling.error_handler import error_handler

def transform_to_float_array(stock: list) :

    result = list()

    try :
        for enumerate in stock :
            result.append([float(enumerate[0]), float(enumerate[1])])
    except :
        error_handler()
    return result
