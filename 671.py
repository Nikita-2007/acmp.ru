n = input()
arr = []
s = -1

def f(p, r):
	if not r:
		return 2**(len(n)-p)
	if p == len(n):
		return 1
	t = 0
	if arr[p] > 4:
		t += f(p+1, 0)
	if arr[p] > 7:
		t += f(p+1, 0)
	if arr[p] == 4 or arr[0] == 7:
		t += f(p+1, 1)
	return t

for i in range(len(n)):
	arr.append(int(n[i]))
	s += 2**i

print(s+f(0, 1))
