n = input()
m = input()
if len(m) > len(n):
	n, m = m, n
f = 0
for i in range(len(m)):
	for j in range(len(n)):
		f += int(m[-(i+1)])*int(n[-(j+1)])*10**(i+j)
print(f)
