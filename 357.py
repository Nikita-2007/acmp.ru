s = t = 0
for i in input():
	s = s+int(i) if not t else s-int(i)
	t = not t
print('YES') if s % 11 == 0 else print('NO')
