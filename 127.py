n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
	for j in range(n):
		if arr[i][j] == 0:
			arr[i][j] = n**n
s, f = map(int, input().split())
s, f = s-1, f-1
q = [s]
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] == 1 and arr[s][i] > arr[s][q[0]]+1:
			q.append(i)
			arr[s][i] = arr[i][s] = arr[s][q[0]]+1
	q.pop(0)
if arr[s][f] < n*n:
	print(arr[s][f])
else:
	print(-1)
print(arr)
