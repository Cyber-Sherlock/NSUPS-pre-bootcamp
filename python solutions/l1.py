t = int(input())
for _ in range(t):
    x = int(input())
    c = 0
    f = False
    while x != 1:
        if x % 2 == 0:
            x = int(x/2)
            c+=1
        elif x % 5 == 0:
            x = int(x/5)*4
            c+=1
        elif x % 3 == 0:
            x = int(x/3)*2
            c+=1
        else:
            print(-1)
            f = True
            break
    if not f:
        print(c)