s = 0
n = int(input())
if n >= 0:
	for i in range(1, n+1):
		s += i
	if s == 0:
		s = 1
	elif s == 1:
		s = 0
else:
	for i in range(1, -n+1):
		s -= i
	s += 1
print(s)
