import numpy as np
from fractions import Fraction

def input_n():
    """Input number row column"""
    a = int(input("Please input number of row and column (n x n): "))
    return a

def fraction(a, b):
    """Fraction function"""
    return Fraction(a, b)

def printFrac(list1):
    """Print Fraction"""
    for i in range(len(list1)):
        for j in range(len(list1)):
            print(list1[i][j], end=" ")
        print('\n')

def sumFrac(list1):
    """Sum Fraction"""
    sum_val = 0
    for item in list1:
        sum_val += sum(item)
    return sum_val

if __name__=='__main__':
    n = input_n()  # number row, column
    template = [i for i in range(1, n + 1)]
    value = []

    for i in range(1, n + 1):
        temp1 = [j for j in range(i + 1, i + n + 1)]
        temp2 = map(fraction, template, temp1)
        value.append(list(temp2))

    printFrac(value)
    print(f"Where n = {n} the amount won or lost is: {sumFrac(value)}")





