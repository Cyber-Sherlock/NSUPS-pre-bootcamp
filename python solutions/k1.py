a, b = map(int, input().split(' '))
x = (a+b)/2
y = (x*10)%10
if y == 0:
    print(int(x))
else:
    print('IMPOSSIBLE')