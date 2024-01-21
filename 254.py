n = int(input())
arr = list(map(int, input().split()))
f = list(arr)
for i in range(int(input())):
	a, b = map(int, input().split())
	for i in range(n):
		if arr[i] == a:
			f[i] = b
print(*f)
