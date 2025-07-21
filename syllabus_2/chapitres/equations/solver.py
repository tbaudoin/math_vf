from sympy.abc import x
from sympy import solve
from sympy.parsing.mathematica import parse_mathematica
from sympy import latex
from pyperclip import copy

equations = [
    "\dfrac{1}{2}+3x -(\dfrac{4}{3})",
    "55x-15 -(75x+18)",
    "2x+\dfrac{7}{3} -(1/4)",
    "4x+3 -(2x-7)",
    "x-1 -(3x+9)",
    "2x+8\cdot 5-5 -(7\cdot 3x)",
    "-14+5x\cdot 2 -(x+5)",
    "\dfrac{2x}{3}-\dfrac{5x}{4}+5 -(-6x+\dfrac{4}{3})",
    "12x+4 -(88x-16)",
    "-8-8x+2 -(-6x+x)",
    "19+3x-5x+1 -(11x)",
    "\dfrac{-5}{2}+\dfrac{2x}{3}+x -(\dfrac{4}{3})",
    "-7x+\dfrac{21}{3} -(-43+2x)",
    "\dfrac{6x}{7}+0,2 -(-x-\dfrac{3}{21})",
    " 2x+\dfrac{7}{3} -(\dfrac{1}{4})",
    "9-2x -(7x+1)",
    "-125x-25x -(80-10x )",
    "\dfrac{-8x}{15}+\dfrac{2}{5} -(0,25x+7)",
    "-36+56-2x -(18x)",
    "-18+45x+2x -(50x)",
    "-14+5x\cdot 2 -(x+5)"
    ]

# résolution des équations
solutions = [solve(parse_mathematica(s))[0] for s in equations]

# formatage en latex
latex_solutions = [
    r"\item " + latex(sol, mode='inline', fold_short_frac=False)for sol in solutions]

copy("\n".join(latex_solutions))
print("Content was copied in clipboard")
