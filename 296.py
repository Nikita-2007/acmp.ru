n = int(input())
for i in range(5):
	if n % 5 == 0:
		print(n//5, i)
		break
	else:
		n -= 3
