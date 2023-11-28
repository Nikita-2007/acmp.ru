n, s = map(int, input().split())
arr = []
s -= 1
q = [s]
f = [0]*n
e = 0
for i in range(n):
	arr.append(list(map(int, input().split())))
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] == 1 and not f[i]:
			f[i] = 1
			e-=-1
			q.append(i)
	q.pop(0)
print(max(e-1, 0))
