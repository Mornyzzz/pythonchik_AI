x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = x[0:9:2][::-1]
for i in range(5):
    x[i * 2] = b[i]
print(x)
