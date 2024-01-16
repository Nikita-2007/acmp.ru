n = int(input())
arr = list(map(int, input().split()))
a = b = c = 0
for i in range(n):
	c += b*arr[i]
	b += a*arr[i]
	a += arr[i]
print(c)



'''
#1
for i in range(n-2):
	for j in range(i+1, n-1):
		for k in range(j+1, n):
			f += arr[i]*arr[j]*arr[k]
			
#2
for i in range(n-2):
	for j in range(i+1, n-1):
		t = arr[i]*arr[j]
		for k in range(j+1, n):
			f += t*arr[k]
'''
