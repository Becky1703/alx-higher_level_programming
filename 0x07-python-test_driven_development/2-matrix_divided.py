#!/usr/bin/python3
"""A function that divides a matrix"""


def matrix_divided(matrix, div):
    """

    Divides all elements of a matrix by a given number

    Takes two arguments: matrix and div
    Returns:
         A new matrix where each element of the matrix is the
    corresponding element inputted and divided and rounded up
    to two decimal places.
    """

    if not all(isinstance(row, list)for row in matrix):
        raise TypeError("matrix must be(list of lists of integers/floats)")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be(list of lists of integers/floats)")
        new_row = [round(element / div, 2)for element in row]
        new.append(new_row)
    return new
