n = int(input())
arr = []
r = []
for i in range(n):
	t = list(map(int, input().split()))
	if t[0] == 1:
		arr.insert(0, t[1])
	elif t[0] == 2:
		arr.append(t[1])
	elif t[0] == 3:
		r.append(arr[0])
		arr.pop(0)
	elif t[0] == 4:
		r.append(arr[len(arr)-1])
		arr.pop(len(arr)-1)
print(*r)
