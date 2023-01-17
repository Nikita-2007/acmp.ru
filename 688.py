x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())-
n = int(input())
for i in range(n):
	x3, y3 = map(int, input().split())
	if (abs(x1-x3)**2 + abs(y1-y3)**2)**0.5 <= ((abs(x2-x3)**2 + abs(y2-y3)**2)**0.5)/2:
		print(i+1)
		break
	if i+1 == n:
		print('NO')
