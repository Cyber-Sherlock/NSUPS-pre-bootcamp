ls = []
while True:
    try:
        l = input()
        ls.append(l)
    except EOFError:
        break
k = ' '.join(ls)
punc = ['.', ',', '"', ":", "'", "!"]
for i in punc:
    k.replace(i, "")
k = k.lower()
words = k.split(' ')
words.sort()
for i in words:
    print(i)