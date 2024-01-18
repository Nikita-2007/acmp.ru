n, m = map(int, input().split())
t = list(map(int, input().split()))
arr = [[0 for i in range(m)] for j in range(n)]
f = 0
q = []
for i in range(t.pop(0)):
	arr[t[i*2]-1][t[i*2+1]-1] = 1
	q.append([t[i*2]-1, t[i*2+1]-1])
while len(q)>0:
	t = []
	s = 1
	for i in q:
		if i[0] > 0 and arr[i[0]-1][i[1]] == 0:
			arr[i[0]-1][i[1]] = 1
			t.append([i[0]-1, i[1]])
			s = 0
		if i[0] < n-1 and arr[i[0]+1][i[1]] == 0:
			arr[i[0]+1][i[1]] = 1
			t.append([i[0]+1, i[1]])
			s = 0
		if i[1] > 0 and arr[i[0]][i[1]-1] == 0:
			arr[i[0]][i[1]-1] = 1
			t.append([i[0], i[1]-1])
			s = 0
		if i[1] < m-1 and arr[i[0]][i[1]+1] == 0:
			arr[i[0]][i[1]+1] = 1
			t.append([i[0], i[1]+1])
			s = 0
	if s: break
	q = t
	f += 1
print(f)
