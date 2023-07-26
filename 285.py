n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(n):
	arr[i] -= 1
if arr[0] > m-1:
	print('no')
elif sum(arr) >= m-1:
	print('yes')
else:
	print('no')
