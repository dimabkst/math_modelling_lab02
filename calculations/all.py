from sympy import Matrix, integrate, Symbol, simplify
from sympy.parsing.sympy_parser import parse_expr
from typing import List
from errors import BadMatrixEquationDimensionsError


def all(A_t: List[List[str]], b: list, T: float) -> dict:
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

    v_list = [Matrix([a * Symbol('t') for _ in range(sympy_A_t.cols)]) for a in
              range(-2, 2 + 1, 1)]  # Vectors v with n entries in form: (a*t, a*t, ..., a*t)

    omega_xt = [
        sympy_A_t.transpose() * sympy_P1.pinv() * sympy_b + v - sympy_A_t.transpose() * sympy_P1.pinv() *
        A_v(sympy_A_t, v, T) for v in v_list]
    omega_xt = [[simplify(el) for el in x] for x in omega_xt]

    epsilon_2 = sympy_b.transpose() * sympy_b - sympy_b.transpose() * sympy_P1 * sympy_P1.pinv() * sympy_b
    epsilon_2 = simplify(epsilon_2[0, 0])

    x_circumflex = [simplify(el) for el in (sympy_A_t.transpose() * sympy_P1.pinv() * sympy_b)]

    N = 10
    t_s = [(s + 1) * T / N for s in range(N)]
    uniqueness_matrix = Matrix(
        [[calc_matrix(sympy_A_t.transpose(), t_s[i]) * calc_matrix(sympy_A_t, t_s[j]) for j in range(N)] for i in
         range(N)])
    uniqueness_condition = uniqueness_matrix.det() > 0
    print(uniqueness_matrix.det())

    return {"omega": omega_xt,
            "precision": epsilon_2,
            "solution": x_circumflex,
            "uniqueness_condition": uniqueness_condition
            }


def A_v(A_t, v, T):
    temp_A_v = [[integrate(func, (Symbol('t'), 0, T)) for func in (A_t * v).row(i)] for i in range(A_t.rows)]
    sympy_A_v = Matrix(temp_A_v)

    return sympy_A_v


def calc_matrix(matrix, at):
    return Matrix([[el.subs(Symbol('t'), at) for el in matrix.row(i)] for i in range(matrix.rows)])
