x = int(input())
if x < -5:
    print("x принадлежит интервалу (-inf; -5)")
elif x <= 5:
    print("x принадлежит интервалу [-5; 5]")
else:
    print("x принадлежит интервалу (5; +inf)")
