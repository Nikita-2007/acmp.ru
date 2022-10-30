a, b, c, d = map(int, input().split())
arr = []
for i in range(-101, 101):
	if a*i*i*i+b*i*i+c*i+d == 0:
		arr.append(i)
arr.sort()
print(*arr)
