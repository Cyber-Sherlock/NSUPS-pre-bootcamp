t = int(input())
for _ in range(t):
    n = int(input())
    colors = input()
    red = colors.count('R')
    green = colors.count('G')
    blue = colors.count('B')
    m = max(red, green, blue)
    print(n - m)