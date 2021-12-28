q = int(input())
l = []
for _ in range(q):
    y, x = map(int, input().split(' '))
    if y == 1:
        if l.count(x) > 0:
            continue
        l.append(x)
        continue
    elif y == 2:
        if l.count(x) > 0:
            l.remove(x)
            continue
        else:
            continue
    elif y == 3:
        if l.count(x) > 0:
            print("Yes")
        else:
            print("No")
        continue
