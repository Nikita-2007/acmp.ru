n, s = input(), 0
for i in range(len(n)-4):
	if n[i:i+5] == '>>-->' or n[i:i+5] == '<--<<':
		s += 1
print(s)
