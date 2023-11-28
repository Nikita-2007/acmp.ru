n, s, f = map(int, input().split())
s, f = s-1, f-1
arr = []
p = [1e10]*n
p[s] = 0
q = [s]
for i in range(n):
	arr.append(list(map(int, input().split())))
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] != -1 and arr[q[0]][i]+p[q[0]] < p[i]:
			q.append(i)
			p[i] = arr[q[0]][i]+p[q[0]]
	q.pop(0)
if p[f] == 1e10:
	print(-1)
else:
	print(p[f])
