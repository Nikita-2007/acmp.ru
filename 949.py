n, x, y = map(int, input().split())
for i in range(n-1): x, y = y-x, x
print(x, y)
