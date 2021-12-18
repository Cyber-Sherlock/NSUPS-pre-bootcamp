n = int(input())
 
nsl = [s for s in str(n)]
 
fc = nsl.count('4')
sc = nsl.count('7')
 
lc = fc + sc 
 
if lc == 4 or lc == 7:
    print("YES")
 
else:
    print("NO")