t = int(input())
for i in range(1,t+1):
    a, b , c = map(int, input().split(' '))
    if (a+b) > c and (a+c) > b and (b+c) > a:
        if a == b and a == c:
            print('Case {}: Equilateral'.format(i))
        elif a != b and a != c and b != c:
            print('Case {}: Scalene'.format(i))
        else:
            print('Case {}: Isosceles'.format(i))
    else:
        print('Case {}: Invalid'.format(i))