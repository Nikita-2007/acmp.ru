n, m = map(int, input().split())
s = 0
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(m):
	if arr[i] > 0:
		s += arr[i]
	else:
		break
print(s)
