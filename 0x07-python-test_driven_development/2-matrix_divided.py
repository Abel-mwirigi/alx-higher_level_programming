#!/usr/bin/python3
"""function that divides each element of a matrix"""

def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
       raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all(isinstance(row, list)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
            