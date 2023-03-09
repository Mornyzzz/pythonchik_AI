import numpy as np
import pandas as pd

a = pd.Series([5,7])
b = pd.Series([10,4])

e = np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

print(e)