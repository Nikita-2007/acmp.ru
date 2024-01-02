p, q = map(int, input().split())
f = 0
for i in range(p, q+1):
	x = i
	while x != 2:
		if x % 2 == 0:
			x //= 2
		else:
			x = x*3+1
		f += 1
print(f)
