n = int(input())
s = 0

def f(t):
	res = 1
	for i in range(1, t+1):
		res *= i
	return res

for i in range(2, n+1):
	s += f(n) // (f(i) * f(n-i))
print(s)
