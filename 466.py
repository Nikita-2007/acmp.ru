n, m = map(int, input().split())
arr1 = []
arr2 = []
t = False
for i in range(n):
	arr1.append(list(input()))
for i in range(n):
	arr2 = list(map(int, input().split()))
	for j in range(m):
		if arr1[i][j] == 'R' and (arr2[j] == 0 or arr2[j] == 1 or arr2[j] == 2 or arr2[j] == 3):
			t = True
			break
		if arr1[i][j] == 'G' and (arr2[j] == 0 or arr2[j] == 1 or arr2[j] == 4 or arr2[j] == 5):
			t = True
			break
		if arr1[i][j] == 'B' and (arr2[j] == 6 or arr2[j] == 4 or arr2[j] == 2 or arr2[j] == 0):
			t = True
			break
	if t:
		break
if t:
	print('NO')
else:
	print('YES')
