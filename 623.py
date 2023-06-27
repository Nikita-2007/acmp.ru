n = int(input())
a = b = c =1
for i in range(n-1):
	a, b = (a+b)%10, a
print(a)
