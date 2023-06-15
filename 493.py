n, m = map(int, input().split())
arr = []
s = 0
for i in range(n):
	arr.append(list(map(str, input())))
for i in range(n):
	for j in range(m):
		if arr[i][j] == '*':
			if arr[i][min(j+1, m-1)] == '.':
				arr[i][min(j+1, m-1)] = 1
			if arr[i][max(j-1, 0)] == '.':
				arr[i][max(j-1, 0)] = 1
			if arr[min(n-1, i+1)][j] == '.':
				arr[min(n-1, i+1)][j] = 1
			if arr[max(0, i-1)][j] == '.':
				arr[max(0, i-1)][j] = 1
for i in range(n):
	s += arr[i].count('.')
print(s)
