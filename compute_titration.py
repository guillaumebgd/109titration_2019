# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## compute_titration.py
##

from titration_functions.find_estimated_eq_pt import find_estimated_eq_pt
from titration_functions.find_and_print_eq_pt import find_and_print_eq_pt
from titration_functions.linear_interpolation import linear_interpolation
from titration_functions.print_derivative import print_derivative
from titration_functions.transform_to_float_array import transform_to_float_array
from titration_functions.update_stock_to_derivative import update_stock_to_derivative
from titration_functions.weighted_derivative import weighted_derivative

def compute_titration(stock: list):

    stock = transform_to_float_array(stock)
    first_derivative = weighted_derivative(stock)
    stock = update_stock_to_derivative(stock, first_derivative)
    print("Derivative:")
    print_derivative(stock)
    print()
    pos_eq = find_and_print_eq_pt(stock)
    print()
    print("Second derivative:")
    second_derivative = weighted_derivative(stock)
    stock = update_stock_to_derivative(stock, second_derivative)
    print_derivative(stock)
    pos_eq -= 1
    print()
    print("Second derivative estimated:")
    estimation = []
    range_of_interpolations = []
    if pos_eq > 0:
        range_of_interpolations.append(stock[pos_eq - 1])
    range_of_interpolations.append(stock[pos_eq])
    if pos_eq < len(stock):
        range_of_interpolations.append(stock[pos_eq + 1])
    for i in range(0, len(range_of_interpolations) - 1):
        linear_interpolation(estimation, range_of_interpolations[i], range_of_interpolations[i + 1], 0.1)
    estimation.append([range_of_interpolations[-1][0], range_of_interpolations[-1][1]])
    print_derivative(estimation)
    print()
    estimated_eq_pt = find_estimated_eq_pt(estimation)
    print("Equivalence point at %.1f ml" % estimated_eq_pt[0])