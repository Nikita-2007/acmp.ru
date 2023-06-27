n = input()
s = ''
i = 1
while s.find(n) < 0:
	s += str(i)
	i += 1
print(s.find(n)+1)
