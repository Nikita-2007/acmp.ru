n = int(input())
arr = list(map(int, input().split()))
s = 0
f = 1
maxi, mini = max(arr), min(arr)
l = min(arr.index(mini), arr.index(maxi))
r = max(arr.index(mini), arr.index(maxi))
for i in arr:
	if i > 0:
		s += i
for i in arr[l+1:r]:
	f *= i
print(s, f)
