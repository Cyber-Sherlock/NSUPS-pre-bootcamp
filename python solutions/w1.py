import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split(' '))
    if a <= b:
        a, b = b, a
    gcd = math.gcd(a,b)
    lcm = int(a*b/gcd)

    print(f"{gcd} {lcm}")