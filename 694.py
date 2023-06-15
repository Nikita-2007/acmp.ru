l, r = 32, 0
for i in range(int(input())):
	t1, t2 = map(int, input().split())
	l = min(t2, l)
	r = max(t1, r)
print('NO') if r > l else print('YES')
