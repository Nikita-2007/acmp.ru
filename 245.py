n = int(input())
arr = [int(input()) for i in range(n)]
if n < 3:
	print(sum(arr))
else:
	arr.sort()
	l = n-3
	r = n-1
	t = f = arr[-1]+arr[-2]
	while l >= 0:
		while arr[l]+arr[l+1] < arr[r]:
			t -= arr[r]
			r -= 1
		t += arr[l]
		l -= 1
		f = max(f, t)
	print(f)
