n = int(input())
f = s = h = 0
arr = list(map(int, input().split()))
for i in range(101):
		if s <= arr.count(i):
			f = s
			s = arr.count(i)
			h = i
if s == f:
	print(0)
else:
	print(h)
