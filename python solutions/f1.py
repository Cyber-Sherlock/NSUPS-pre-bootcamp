n = int(input())
r =[]
for i in range(n):
    x = int(input())
    sum = 0
    while x != 0:
        sum+=(x%10)
        x = int(x/10)
    r.append(str(sum))
print('\n'.join(r))