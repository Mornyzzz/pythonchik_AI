import numpy as np


print("Введите числа:")
x = int(input())
y = int(input())
print("Введите знак операции (+, -, *, /, exp, sin, cos, pow):")
s = input()
print("Ответ:")

if s == '+':
    print(x + y)
if s == '-':
    print(x - y)
if s == '*':
    print(x * y)
if s == '/':
    if y == 0:
        print("Деление на ноль")
    else:
        print(x / y)
if s == 'exp':
    print(np.exp(1) ** (x + y))
if s == 'sin':
    print(np.sin(x + y))
if s == 'cos':
    print(np.cos(x + y))
if s == 'pow':
    print(x ** y)



