n = int(input())
arr = []
if (n >= 9):
	arr.append(n-8)
if ((n-1) % 8 != 0):
	arr.append(n-1)
if (n % 8 != 0):
	arr.append(n+1)
if (n <= 56):
	arr.append(n+8)
print(*arr)
