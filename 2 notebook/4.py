import numpy as np

A = np.array([1] * 25).reshape(5,5)
for i in range(5):
    for j in range(5):
        if (i == 0 or j == 0 or i == 4 or j == 4):
            A[i][j] = 0

print(A)