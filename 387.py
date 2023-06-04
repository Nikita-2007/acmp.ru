t = 0
for i in range(int(input())):
	r, a = map(str, input().split('->'))
	if r == a[0]:
		t += 1
print(t)
