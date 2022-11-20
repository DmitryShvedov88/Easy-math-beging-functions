import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.Symbol('x')
function_x = sp.sympify('x')
function_y = sp.sympify('x**2+x-10')
interval = np.arange(-10, 10, 0.1)
x_values = [function_x.subs(x, value) for value in interval]
y_values = [function_y.subs(x, value) for value in interval]
plt.figure(figsize=(10, 10))
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

