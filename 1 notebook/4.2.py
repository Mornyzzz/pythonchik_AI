import numpy as np
from matplotlib import pyplot as plt


def func(x):
    return np.sqrt(1 + np.exp(1) ** np.sqrt(x) + np.cos(x ** 2)) / abs(1 - np.sin(x) ** 3) + np.log(abs(2 * x))


count = 10
arr = np.arange(1, count + 1)
slice = arr[:int(count / 2)]

plt.plot(arr, func(arr))
plt.grid()
plt.show()

plt.scatter(slice, func(slice))
plt.grid()
plt.show()

