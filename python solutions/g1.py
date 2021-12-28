n = int(input())
import math
for _ in range(n):
    l = float(input())
    w = (l*6)/10
    r = (l/5.0)
    ta = l*w
    pi = math.acos(-1)
    ca = pi*r*r
    print("{} {}".format(round(ca,2), round((ta-ca),2)))