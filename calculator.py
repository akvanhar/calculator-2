"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
calc_input = raw_input("> ").split(" ")

def calculator(calc_list):
    if calc_list[0] == "+":
        addition = add(int(calc_list[1]), int(calc_list[2]))
        print addition
    elif calc_list[0] == "-":
        subtraction = subtract(int(calc_list[1]), int(calc_list[2]))
        print subtraction
    elif calc_list[0] == "*":
        multiplication = multiply(int(calc_list[1]), int(calc_list[2]))
        print multiplication
    elif calc_list[0] == "/":
        division = divide(int(calc_list[1]), int(calc_list[2]))
        print division
    elif calc_list[0] == "square":
        squarednum = square(int(calc_list[1]), int(calc_list[2]))
        print squarednum
    elif calc_list[0] == "cube":
        cubenum = cube(int(calc_list[1]), int(calc_list[2]))
        print cubenum
    elif calc_list[0] == "pow":
        pownum = power(int(calc_list[1]), int(calc_list[2]))
        print pownum
    elif calc_list[0] == "mod":
        modulation = mod(int(calc_list[1]), int(calc_list[2]))
        print modulation
    elif calc_list[0] == "q":
        return
    else:
        print "I don't understand."



while calc_input != ["q"]:
    calculator(calc_input)
    calc_input = raw_input("> ").split(" ")
