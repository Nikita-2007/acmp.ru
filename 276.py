n, m = map(int, input().split())
x = n//m
y = n-(m*x)
arr = []
for i in range(m):
	arr.append(x)
for i in range(y):
	arr[m-i-1] += 1
print(*arr)
