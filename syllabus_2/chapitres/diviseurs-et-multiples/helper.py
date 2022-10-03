from sympy.ntheory import factorint
from pyperclip import copy
from sympy import gcd, lcm

exos=[(40, 16),
(75, 90),
(90, 48),
(80, 84),
(44, 55),
(150, 300),
(2, 3),
(12, 15),
(50, 75),
(16, 12),
(14, 10),
(60, 35)]
for t in exos:
    print(lcm(t))
