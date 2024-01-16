s = input()
arr = []
f = 1
for i in set(s):
	arr.append(s.count(i))
for i in range(1, len(s)+1):
	f *= i
print(f)
