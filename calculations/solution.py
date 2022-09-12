from sympy import Matrix, integrate, Symbol, simplify
from sympy.parsing.sympy_parser import parse_expr
from typing import List
from errors import BadMatrixEquationDimensionsError


def solution(A_t: List[List[str]], b: list, T: float):
    # A is list of lists of strings that describe functions of t, such as t**2 + 1.

    # A(t) looks like [[a11(t), ..., a1n(t)], ..., [am1(t), ..., amn(t)]]
    # b looks like [b1, ..., bm]

    # Check whether A is m x n and b is m x 1
    if len(A_t) != len(b):
        raise BadMatrixEquationDimensionsError

    temp_A_t = [[parse_expr(expr, transformations='all') for expr in A_t_row] for A_t_row in A_t]

    sympy_A_t = Matrix(temp_A_t)
    sympy_b = Matrix(b)

    temp_P1 = [[integrate(func, (Symbol('t'), 0, T)) for func in (sympy_A_t * sympy_A_t.transpose()).row(i)]
               for i in range(sympy_A_t.rows)]
    sympy_P1 = Matrix(temp_P1)

    x_circumflex = [simplify(el) for el in (sympy_A_t.transpose() * sympy_P1.pinv() * sympy_b)]

    return x_circumflex

