# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## compute_titration.py
##

from src import *

def is_list_constant(stock: list):
    first_occ = stock[0][1]
    for i in range(0, len(stock)):
        if stock[i][1] != first_occ:
            return False
    return True

def first_derivative(stock: list):
    print("Derivative:")
    stock = update_stock_to_derivative(stock, weighted_derivative(stock))
    print_derivative(stock)
    return stock

def second_derivative(stock: list):
    print("Second derivative:")
    stock = update_stock_to_derivative(stock, weighted_derivative(stock))
    print_derivative(stock)
    return stock

def second_derivative_estimated(stock: list, pos_eq: int):
    estimation = []
    list_pts_to_interpolate = []

    print("Second derivative estimated:")
    if pos_eq > 0:
        pos_eq -= 1
    if pos_eq > len(stock) - 1:
        pos_eq = len(stock) - 1
    if pos_eq > 0:
        list_pts_to_interpolate.append(stock[pos_eq - 1])
    list_pts_to_interpolate.append(stock[pos_eq])
    if pos_eq < len(stock) - 1:
        list_pts_to_interpolate.append(stock[pos_eq + 1])
    for i in range(0, len(list_pts_to_interpolate) - 1):
        linear_interpolation(estimation, list_pts_to_interpolate[i], list_pts_to_interpolate[i + 1], 0.1)
    estimation.append([list_pts_to_interpolate[-1][0], list_pts_to_interpolate[-1][1]])
    print_derivative(estimation)
    return estimation

def compute_titration(stock: list):
    stock = transform_to_float_array(stock)
    stock = first_derivative(stock)
    print()
    pos_eq = find_eq_pt(stock)
    first_eq_pt = stock[pos_eq][0]
    print("Equivalence point at %.1f ml" % first_eq_pt)
    print()
    stock = second_derivative(stock)
    print()
    if is_list_constant(stock) is not True :
        estimation = second_derivative_estimated(stock, pos_eq)
        print()
        estimated_eq_pt = find_estimated_eq_pt(estimation)
        print("Equivalence point at %.1f ml" % estimated_eq_pt[0])
    else:
        print("Equivalence point at %.1f ml" % first_eq_pt)
