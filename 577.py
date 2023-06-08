n, m = map(int, input().split())
arr = [0]*10
for i in range(1, n+1):
	for j in range(1, m+1):
		x = i*j
		if i > j:
			while x > 0:
				r = x % 10
				x = x // 10
				arr[r] += 2
		elif i == j:
			while x > 0:
				r = x % 10
				x = x // 10
				arr[r] += 1
for i in arr:
	print(i)
