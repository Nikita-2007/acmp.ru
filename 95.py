n = input()
l = 0
while len(n) > 1:
	s = 0
	for i in n:
		s += int(i)
	n = str(s)
	l += 1
print(n, l)
