n, s = map(int, input().split())
t = 0
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
	if s >= arr[i]:
		s -= arr[i]
		t += 1
	else:
		break
print(t)
