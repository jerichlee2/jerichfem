import numpy as np
from sympy import *
import matplotlib.pyplot as plt

x = symbols('x')

def create_symbols(n, prefix='x'):
    symbols_tuple = symbols(f'{prefix}0:{n}')
    #f string allows u to swap in stuff
    #0:{n} enumerates from 0 to n-1
    return list(symbols_tuple)

def lagrange(k):
    vars = create_symbols(k)
    list_of_vars = []
    for i in range(k):
        list_of_vars.append(1)
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            else:
                list_of_vars[i] = list_of_vars[i]*(x-vars[j])/(vars[i]-vars[j])
       
    return list_of_vars

def lagrange_poly(list_of_vars, y_set):
    eqn = 0
    if len(y_set) != len(list_of_vars):
        raise Exception("sizes of sets are different") 
    for i in range(len(list_of_vars)):
        eqn += list_of_vars[i]*y_set[i]

    return eqn



     


            
        



        