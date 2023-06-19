n = int(input())
arr = list(map(int, input().split()))
s = 3
f = 0
for i in arr:
	if i == 1:
		f += s
		s += 1
	else:
		s = max(3, s-3)
print(f)
