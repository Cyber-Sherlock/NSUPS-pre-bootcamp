n = int(input())
for _ in range(n):
    l = float(input())
    w = (l/10.0)*6
    r = (l/5.0)
    ta = l*w
    ca = 3.142*r*r
    print(f"{ca:.2f} {(ta-ca):.2f}")