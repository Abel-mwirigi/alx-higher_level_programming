#!/bin/usr/python3

def print_last_digit(number):
    absolute_value = abs(number)
    last_digit = absolute_value % 10
    print(last_digit, end="")
    return last_digit
