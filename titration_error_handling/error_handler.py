# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 109titration_2019
## File description:
## error_handler.py
##

import sys

from titration_error_handling.usage import usage

def error_handler() :
    usage()
    sys.exit(84)