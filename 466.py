n, m = map(int, input().split())
arr1 = []
arr2 = []
t = False
for i in range(n):
	arr1.append(list(input()))
for i in range(n):
	arr2 = list(map(int, input().split()))
	for j in arr1[i]:
		if j == 'R' and (arr2[i] == 0 or arr2[i] == 1 or arr2[i] == 2 or arr2[i] == 3):
			t = True
			break
		if j == 'G' and (arr2[i] == 0 or arr2[i] == 1 or arr2[i] == 4 or arr2[i] == 5):
			t = True
			break
		if j == 'B' and (arr2[i] == 6 or arr2[i] == 4 or arr2[i] == 2 or arr2[i] == 0):
			t = True
			break
	if t:
		break
if t:
	print('NO')
else:
	print('YES')
