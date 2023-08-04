n, x, y, l = map(int, input().split())
f = 1
for i in range(n):
	x1, y1 = map(int, input().split())
	if ((abs(x-x1)**2)+(abs(y-y1)**2))**0.5 <= l:
		print(i+1)
		f = 0
		break
if f:
	print('Yes')
