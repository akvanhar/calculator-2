"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
user_calc_input = raw_input("> ")
calc_list = user_calc_input.split(" ")
if calc_list[0] == "+":
    sum = add(int(calc_list[1]), int(calc_list[2]))
    print sum
else:
    print "I don't understand."