n, m = map(int, input().split())
r = g = b = c = 0
for i in range(1, n+1):
	for j in range(1, m+1):
		f = i*j
		if f%5 == 0:
			b += 1
		elif f%3 == 0:
			g += 1
		elif f%2 == 0:
			r += 1
		else:
			c += 1
print('RED :', r)
print('GREEN :', g)
print('BLUE :', b)
print('BLACK :', c)
