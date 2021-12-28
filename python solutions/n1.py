a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))
x, y = abs(c - a), abs(d - b)
if x >= y:
    print(x)
else:
    print(y)
    