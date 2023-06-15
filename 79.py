a, b = map(int, input().split())
s = a
for i in range(b-1):
	a = int(str(a*s)[-1])
print(str(a)[-1])
