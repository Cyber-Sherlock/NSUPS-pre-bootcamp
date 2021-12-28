i = 1
while True:
    s = input()
    if s == '*':
        break
    if s == 'Hajj':
        print('Case {}: Hajj-e-Akbar'.format(i))
        i+=1
    elif s == 'Umrah':
        print('Case {}: Hajj-e-Asghar'.format(i))
        i+=1