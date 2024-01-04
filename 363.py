n = input()
m = input()
l = (len(n)+len(m))
f = [0]*l
if len(m) > len(n):
	n, m = m, n
arr = [[i*j for i in range(10)] for j in range(10)]

for i in range(len(m)-1, -1 , -1):
	for j in range(len(n)-1, -1, -1):
		f[i+j+1] += arr[int(m[i])][int(n[j])]
for i in range(l-1, -1, -1):
	f[i-1] += f[i]//10
	f[i] %= 10

print(int(''.join(map(str, f))))
