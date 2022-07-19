maxi = n = -1;
for i in range(int(input())):
	v, s = map(int, input().split())
	if s == 1:
		if maxi < v:
			maxi = v
			n = i+1
print(n)
