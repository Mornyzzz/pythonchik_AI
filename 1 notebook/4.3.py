import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import simps
from numpy import trapz


def func(n):
    return abs(np.cos(n * np.exp(1) ** (np.cos(n) + np.log(n + 1))))


x = np.arange(0.0, 11.0, 1)
y = func(x)
print(trapz(y))
plt.plot(x, y, c="b")
plt.fill_between(x, y)
#plt.set_facecolor('seashell')
plt.grid()
plt.show()





