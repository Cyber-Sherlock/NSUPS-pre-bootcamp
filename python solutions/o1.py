l = list(map(int, input().split(' ')))
d = {}
for i in l:
    if str(i) in d.keys():
        continue
    c = l.count(i)
    d[str(i)] = c

for k, v in d.items():
    print(k, v)
    