n = int(input())
l = list(map(int, input().split(' ')))
c = 0
t = []
f = False
for i in range(1, n+1):
    if l[i-1] == i:
        continue
    else:
        c +=1
        if c > 2:
            print('NO')
            f = True
            break
        t.append(l[i-1])

if not f:
    print('YES')