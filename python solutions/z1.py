t = int(input())
for _ in range(t):
    a,b, c = map(int, input().split(' '))
    s = a+b+c
    if s == 180:
        print("YES")
    else:
        print("NO")