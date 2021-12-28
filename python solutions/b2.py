t = int(input())
l = list(map(int, input().split(' ')))
if t == 1 and l[0] == 0:
    print(1)
elif t == 1 and l[0] != 0:
    print(0)
else:
    mx = max(l)
    if mx == 0:
        print(0)
    else:
        l.sort()
        res = 0
        for i in l:
            res+=mx-i
        print(res)