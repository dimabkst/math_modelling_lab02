from sympy import Matrix, integrate, Symbol, simplify
from sympy.parsing.sympy_parser import parse_expr
from typing import List
from errors import BadMatrixEquationDimensionsError


def precision(A_t: List[List[str]], b: list, T: float):
    # A is list of lists of strings that describe functions of t, such as t**2 + 1.

    # A(t) looks like [[a11(t), ..., a1n(t)], ..., [am1(t), ..., amn(t)]]
    # b looks like [b1, ..., bm]

    # Check whether A is m x n and b is m x 1
    if len(A_t) != len(b):
        raise BadMatrixEquationDimensionsError

    temp_A_t = [[parse_expr(expr, transformations='all') for expr in A_t_row] for A_t_row in A_t]

    sympy_A_t = Matrix(temp_A_t)
    sympy_b = Matrix(b)

    N = 15

    t_s = [(s + 1) * T / N for s in range(N)]

    uniqueness_matrix = Matrix(
        [[calc_matrix(sympy_A_t.transpose(), t_s[i]) * calc_matrix(sympy_A_t, t_s[j]) for j in range(N)] for i in
         range(N)])

    return uniqueness_matrix.det() > 0


def calc_matrix(matrix, at):
    return Matrix([[el.subs(Symbol('t'), at) for el in matrix.row(i)] for i in range(matrix.rows)])
