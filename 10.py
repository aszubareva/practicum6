x1a, y1a = map(float, input().split())
x2a, y2a = map(float, input().split())
x1b, y1b = map(float, input().split())
x2b, y2b = map(float, input().split())

x1a, x2a = min(x1a, x2a), max(x1a, x2a)
y1a, y2a = max(y1a, y2a), min(y1a, y2a)
x1b, x2b = min(x1b, x2b), max(x1b, x2b)
y1b, y2b = max(y1b, y2b), min(y1b, y2b)

if x2a < x1b or x2b < x1a or y2a > y1b or y2b > y1a:
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif (x1a > x1b and x2a < x2b and y1a < y1b and y2a > y2b) or (x1b > x1a and x2b < x2a and y1b < y1a and y2b > y2a):
    print("Один прямоугольник лежит внутри другого, не касаясь")
elif x1a == x2b or x2a == x1b or y1a == y2b or y1b == y2a:
    print("Прямоугольники имеют касание")
else:
    print("Прямоугольники имеют пересечение")
