n = int(input())
s = 0
for i in range(1, n):
	a = i
	b = n
	while a!=0 and b!=0:
		if a>b:
			a=a%b
		else:
			b=b%a
	if a+b == 1:
		s += 1
print(s)
