import numpy as np
from matplotlib import pyplot as plt

data = np.random.random(1000)
q = np.arange(1000)
x = np.median(data)
y = np.average(data)
print(x, y)
plt.grid()
plt.scatter(q, data)
plt.show()

