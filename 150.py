n, s = map(int, input().split())
arr = []
q = [s-1]
f = [1]*n
e = 0
for i in range(n):
	arr.append(list(map(int, input().split())))
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] and f[i]:
			f[i] = 0
			e-=-1
			q.append(i)
	q.pop(0)
print(max(e-1, 0))
