n = int(input())
s = 3000
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			s = min(s, arr[i][j]+arr[j][k]+arr[k][i])
print(s)
