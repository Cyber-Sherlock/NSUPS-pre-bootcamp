n = int(input())
l = list(map(int, input().split(' ')))
l2 = [x%2 for x in l]
ec = l2.count(0)
if ec > 1:
    print(l2.index(1) + 1 )
else:
    print(l2.index(0) + 1)