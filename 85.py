n, m = map(int,input().split())
while(m):
	n, m = m, n % m 
print('1'*n)
