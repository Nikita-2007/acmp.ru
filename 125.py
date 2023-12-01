n = int(input())
arr = []
F = []
s = 0
for i in range(n):
	arr.append(list(map(int, input().split())))
input()
F = list(map(int, input().split()))
for i in range(n):
	for j in range(1, n-i):
		if arr[i][n-j] == 1 and F[i] != F[n-j]:
			s += 1
print(s)
