n, m, k = map(int, input().split())
arr = []
mtx = [[0]*m for i in range(n)]
for i in range(k):
	arr.append(list(map(int, input().split())))
for i in arr:
	if i[0] > 1 and i[1] > 1: mtx[i[0]-2][i[1]-2] += 1
	if i[0] > 1: mtx[i[0]-2][i[1]-1] += 1
	if i[0] > 1 and i[1] < m: mtx[i[0]-2][i[1]] += 1
	if i[1] > 1: mtx[i[0]-1][i[1]-2] += 1
	if i[1] < m: mtx[i[0]-1][i[1]] += 1
	if i[0] < n and i[1] > 1: mtx[i[0]][i[1]-2] += 1
	if i[0] < n: mtx[i[0]][i[1]-1] += 1
	if i[0] < n and i[1] < m: mtx[i[0]][i[1]] += 1
for i in arr:
	mtx[i[0]-1][i[1]-1] = '*'
for i in range(n):
	for j in range(m):
		if mtx[i][j] == 0:
			mtx[i][j] = '.'
		elif mtx[i][j] != '*':
			mtx[i][j] = str(mtx[i][j])
for i in range(n):
	print(''.join(mtx[i]))
