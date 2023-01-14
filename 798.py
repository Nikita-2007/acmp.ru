n, m, i, j, c = map(int, input().split())
if not (n*m) & 1:
	print('equal')
elif (i+j) & 1:
	print('white') if c == 0 else print('black')
else:
	print('white') if c == 1 else print('black')
 
