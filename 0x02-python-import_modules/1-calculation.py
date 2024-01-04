#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import *

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print("Addition: {} + {} = {}".format(a, b, result_add))
print("Subtraction: {} - {} = {}".format(a, b, result_subtract))
print("Multiplication: {} * {} = {}".format(a, b, result_multiply))
print("Division: {} / {} = {}".format(a, b, result_divide))
