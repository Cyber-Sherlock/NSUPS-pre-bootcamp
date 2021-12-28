n = int(input())
o = []
for _ in range(n):
    x = int(input())
    l = list(map(int, input().split(' ')))
    l.sort()
    sum = l[0]+l[1]
    o.append(sum)
for i in o:
    print(i)