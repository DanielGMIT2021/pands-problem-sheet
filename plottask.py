# displays a plot of the functions 
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

# Author: Daniel Gonzalez

import numpy as np
import matplotlib.pyplot as plt

# Variables:
x = np.arange(4)
g = x**2
h = x**3

# Characteristics of plots: 
plt.plot(x,marker='o',color="blue", label="base value")
plt.plot(g, marker='o', color="orange", label="X squared", linestyle='dashed', linewidth=3)
plt.plot(h, marker='o', color="red", label="X Cubed", linewidth=3)

# Decoration of plots:
plt.title(label="X and Relations",backgroundcolor='grey', loc="center", pad=10, fontsize=15, fontstyle='italic')
plt.xlabel("X", fontstyle='italic', fontsize=13, backgroundcolor='grey')
plt.ylabel("X Relations", fontstyle='italic', fontsize=13, backgroundcolor='grey')

ax = plt.axes()
ax.set_facecolor("black")

plt.legend()
plt.show()