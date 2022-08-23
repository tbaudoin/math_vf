from collections import Counter
from sympy import factor, latex, expand
from sympy.abc import a, b, c, x, y
from sympy.parsing.sympy_parser import (parse_expr, _token_splittable,
                                        standard_transformations, implicit_multiplication, split_symbols_custom)

transformations = standard_transformations + (implicit_multiplication,)


def parse(expr):
    return parse_expr(expr, transformations=transformations)


def factorisation(expr):
    return factor(expr)


def developpement(expr):
    return expand(expr)


def make_op(math_expr, op):
    result = []
    try:
        for expr in math_expr:
            result.append(op(parse(expr)))
        # print the result
        print("== Succes ==")
        for expr in result:
            print(latex(expr, mode="inline"))
    except:
        print("an error occur")
    return result


# a list of math expressions
math_expr = ["3a-3b",
             "6abc+12ab",
             "24bc+36cd",
             "2ab-2ac",
             "16a+40b",
             "25x-15y",
             "4a+4c",
             "18a+24b",
             "55ab+11a",
             "12rst-2r"]
# the operation
op = factorisation
for e in math_expr:
    print(make_op(e,op))
