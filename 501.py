n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))
x1, y1, x2, y2 = map(int, input().split())
f = 0
for i in arr:
	xt1 = max(min(i[0], i[2]), min(x1, x2))
	yt1 = max(min(i[1], i[3]), min(y1, y2))
	xt2 = min(max(i[0], i[2]), max(x1, x2))
	yt2 = min(max(i[1], i[3]), max(y1, y2))
	f += max(yt2-yt1, 0)*max(xt2-xt1, 0)
print(f)
