n, k = map(str, input().split())
n, r = int(n), 1
while n > 1:
	r *= n
	n -= len(k)
print(r)
