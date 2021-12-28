l =[]
while True:
    try:
        x = int(input())
        l.append(x)
        l.sort()
        if len(l)%2 == 0:
            i = int(len(l)/2) - 1
            m = int((l[i]+l[i+1])/2)
            print(m)
        else:
            m = l[int((len(l)+1)/2) -1]
            print(m)
    except EOFError:
        break