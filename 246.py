n = int(input())
arr = list(map(int, input().split()))
s = 0
for i in range(n-1):
	if arr[i] - arr[i+1] != -1:
		s += 1
print(s)
