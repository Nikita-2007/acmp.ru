n, v, k = map(int, input().split())
f = 0
s = 'YES' if n*k < v+k else 'NO'
for i in range(n):
	f += v
	v -= k
	if v <= 0:
		break
print(s, f)
