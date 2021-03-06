# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## find_estimated_eq_pt.py
##

def abs(nb: float):
    return nb if nb >= 0 else -nb

def get_signof(nb: float):
    return -1 if nb < 0 else 1

def find_closest_to_zero(estimation: list):
    closest = estimation[0]

    for i in range(1, len(estimation)):
        if closest[1] < estimation[i][1]:
            closest = estimation[i]
    return closest

def find_estimated_eq_pt(estimation: list):
    i = 1
    signof_first = get_signof(estimation[0][1])

    while i < len(estimation):
        if get_signof(estimation[i][1]) != signof_first:
            break
        i += 1
    if i == len(estimation):
        return find_closest_to_zero(estimation)
    first = estimation[i - 1]
    second = estimation[i]
    if abs(first[1]) > abs(second[1]):
        return second
    return first