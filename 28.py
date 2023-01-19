x1, y1, x2, y2 = map(int, input().split())
xa, ya = map(int, input().split())
if x1 == x2:
	print(-xa+(x1*2), ya)
else:
	print(xa, -ya+(y1*2))
