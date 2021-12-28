tc = int(input())
rs =[]
for i in range(tc):
    x = int(input())
    sum = 0
    while x != 0:
        sum+=(x%10)
        x = int(x/10)
    rs.append(str(sum))
print('\n'.join(rs))