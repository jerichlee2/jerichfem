import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import lagrange_interpolation
import random

x = symbols('x')

terms = lagrange_interpolation.lagrange(5)

start = 1
end = 50
amount = 5
prefix = 'x'
numbers = random.sample(range(start, end+1),amount)
subs_dict = {}

for i in range(amount):
    subs_dict[f'{prefix}{i}'] = numbers[i] 

polynomial = lagrange_interpolation.lagrange_poly(terms, numbers)

subbed_polynomial = polynomial.subs(subs_dict)
poly = lambdify(x, subbed_polynomial, "numpy")

x_values = np.linspace(0,5)
print((poly(x)))

plt.scatter(range(len(numbers)), numbers)
plt.plot(x_values, poly(x_values))
plt.title("Random sample lagrange interpolation plot")
plt.xlabel("Index")
plt.ylabel("value")
plt.show()

