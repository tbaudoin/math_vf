from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication, convert_xor)
from sympy.abc import x,y,z
from sympy import factor
from sympy import latex
transformations = standard_transformations + (implicit_multiplication, convert_xor)

expressions = ["5xy^2 + 10x^3y"]

with open("solution.txt", "w") as f:
    for e in expressions:
        expr = parse_expr(e, transformations=transformations)
        print(expr)
        expr = factor(expr)
        print(expr)
        print(latex(expr, mode="inline"))
    