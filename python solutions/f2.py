p = int(input())
l = list(map(int, input().split(' ')))
r = 0
i = 1
while True:
    if i == 8:
        i = 1
    pr = l[i-1]
    r+=pr
    if r >= p:
        break
    i+=1

print(i)