import numpy as np
from matplotlib import pyplot as plt

apple = [133, 123, 123, 132, 125, 136, 146, 152, 141, 149, 167, 178]
microsoft = [235, 236, 239, 253, 251, 270, 286, 303, 282, 331, 335, 335]
google = [92, 102, 104, 118, 119, 122, 135, 145, 134, 148, 144, 145]
months = np.arange(1, 13)

plt.xlabel("Месяц")
plt.ylabel("Цена акции, $")

plt.plot(months, microsoft, c="r", linewidth=3, label="Microsoft")
plt.plot(months, apple, c="g", linewidth=3, label="Apple")
plt.plot(months, google, c="b", linewidth=3, label="Google")
plt.grid()
plt.legend()
plt.show()




