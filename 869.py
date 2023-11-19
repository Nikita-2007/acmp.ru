n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
f = 0
l = 0
r = n-1
while l <= r:
	if l == r:
		f += 1
		break
	if arr[l] + arr[r] <= d:
		l += 1
	r -= 1
	f += 1
print(f)
