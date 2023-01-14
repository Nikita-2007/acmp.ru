s=r=l=1
for i in input():
 s+=int(i)%2*2-1
 l, r=max(l, s), min(r, s)
print(l-r+1)
