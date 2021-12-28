n, k, l, c, d, p, nl, np  = map(int, input().split(' '))
tv = k*l
ts = c*d
l = [int(tv/nl), ts, int(p/np)]
m = min(l)
r = int(m/n)
print(r)