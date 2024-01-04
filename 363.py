n = input()
m = input()
f = 0
if len(m) > len(n):
	n, m = m, n
n = int(n)
arr = [n*i for i in range(10)]
for i in range(len(m)-1, -1, -1):
	f += arr[int(m[-i-1])]*10**i
print(f)
