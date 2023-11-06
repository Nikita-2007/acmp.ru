n, f = map(str, input().split())
b = c = 0
for i in range(4):
	if f[i] == n[i]:
		b += 1
	elif f[i] in n:
		c += 1
print(b, c)
