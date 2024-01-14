w, h = map(int, input().split())
arr1 = []
arr2 = []
for i in range(h):
	arr1.append(list(map(int, input())))
for i in range(h):
	arr2.append(list(map(int, input())))
arr3 = list(map(int, input()))
f = [[0 for i in range(w)] for i in range(h)]
for i in range(h):
	for j in range(w):
		if not arr1[i][j] and not arr2[i][j]:
			f[i][j] = arr3[0]
		elif not arr1[i][j] and arr2[i][j]:
			f[i][j] = arr3[1]
		elif arr1[i][j] and not arr2[i][j]:
			f[i][j] = arr3[2]
		else:
			f[i][j] = arr3[3]
for i in range(h):
	print(''.join(list(map(str, f[i]))))
