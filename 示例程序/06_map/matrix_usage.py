#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import random

"""思考：
1. 构造一个全0矩阵， generate_zeros_matrix(rows=3, cols=3)
2. 构造一个单位矩阵, generate_identity_matrix(rows=3)
3. 访问第i列，get_column(matrix, column=0)

"""

def generate_random_matrix(rows=3, cols=3):
    matrix = []  # Create an empty list
    for rownum in range(rows):
        row = []
        for colnum in range(cols):  
            row.append(random.randint(0, 99))
        matrix.append(row)  
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()  # Print a new line


def print_matrix_2(matrix):
    for rownum in range(len(matrix)):
        for colnum in range(len(matrix[rownum])):
            print(matrix[rownum][colnum], end=" ")
        print()  # Print a new line

def transpose_matrix(matrix):
    # 采用zip实现矩阵转置
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix_transpose = list(zip(*matrix))
    print(matrix_transpose)
    matrix_transpose2 = [list(item) for item in matrix_transpose]
    print(matrix_transpose2)
    matrix_transpose3 = [list(item) for item in zip(*matrix)]

    matrix_transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return matrix_transpose3


if __name__ == '__main__':
    matrix = generate_random_matrix()
    print_matrix(matrix)
    print()
    print_matrix_2(matrix)
