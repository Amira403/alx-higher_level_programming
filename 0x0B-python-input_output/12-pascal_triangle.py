#!/usr/bin/python3
"""Module 12-pascal_triangle
Returns a list of list of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n

    Args:
        - n: size of the triangle(rows)

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    lst = [[0 for x in range(i + 1)] for i in range(n)]
    lst[0] = [1]

    for i in range(1, n):
        lst[i][0] = 1
        for j in range(1, i + 1):
            if j < len(lst[i - 1]):
                lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
            else:
                lst[i][j] = lst[i - 1][0]
    return lst
