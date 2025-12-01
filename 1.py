a, b = map(int, input().split('x'))
d = pow(a**2+b**2, 0.5)
if d <= 13:
    print("да")
else:
    print("нет")