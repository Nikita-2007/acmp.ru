n, m, k = map(int, input().split())
f = 0
if n < m and n <= k:
	print('NO')
else:
	while m > 0:
		f += 1
		m -= n
		if m <= 0:
			break
		m += k
	print(f)
