X,Y,Z = map(int, input().split())
if max(X, Y, Z) < X+Y+Z-max(X,Y,Z):
    print('YES')
else:
    print('NO')
