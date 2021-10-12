N = int(input())
g = 0
r = 0
for i in range(N):
    x = input()
    if x == '0':
        g += 1
    else:
        r += 1 
if r > g:
    print(g)
elif g > r:
    print(r)
else:
    print(g)