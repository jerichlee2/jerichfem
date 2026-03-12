import re
import numpy as np
import sympy as sp
from scipy import integrate
import matplotlib.pyplot as plt

x = sp.symbols('x')


E = 8 #Pa
L = 4 #m
A = 2*x+2 
b = 8 #N/m

P = 24 #N
# We want to solve for the displacement u, strain du/dx, and stress

