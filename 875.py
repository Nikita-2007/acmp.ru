n, m, k = map(int, input().split())
arr = []
for i in range(n):
	s = input()
	for j in range(m):
		if s[j] == '*':
			arr.append([i, j])

for _ in range(k):
	mtx = [[0]*m for i in range(n)]
	for i in arr:
		mtx[i[0]][i[1]] += 10
		mtx[(i[0]-1+n)%n][(i[1]-1+m)%m] += 1
		mtx[(i[0]-1+n)%n][i[1]] += 1
		mtx[(i[0]-1+n)%n][(i[1]+1+m)%m] += 1
		mtx[i[0]][(i[1]-1+m)%m] += 1
		mtx[i[0]][(i[1]+1+m)%m] += 1
		mtx[(i[0]+1+n)%n][(i[1]-1+m)%m] += 1
		mtx[(i[0]+1+n)%n][i[1]] += 1
		mtx[(i[0]+1+n)%n][(i[1]+1+m)%m] += 1
	arr = []
	for i in range(n):
		for j in range(m):
			if mtx[i][j] == 3 or (mtx[i][j] > 11  and mtx[i][j] < 14):
				arr.append([i, j])
mtx = [['.']*m for i in range(n)]
for i in arr:
	mtx[i[0]][i[1]] = '*'
for i in range(n):
	print(''.join(mtx[i]))
