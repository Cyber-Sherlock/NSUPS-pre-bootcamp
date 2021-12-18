t = int(input())
l = []
for _ in range(0, t):
    tl = list(map(int, input().split(' ')))
    tl.sort()
    l.append(tl[1])
l = [str(x) for x in l]
print('\n'.join(l))