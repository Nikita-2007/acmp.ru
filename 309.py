n = int(input())
f = 0
for i in range(n):
	if i + int(str(i)[::-1]) == n:
		f += 1
print(f)
