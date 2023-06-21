n = int(input())
arr = []
arr2 = []
s = 0
for i in range(n):
	arr.append(list(map(str, input())))
	arr2.append(['1']*n)
	s += arr[i].count('C')
s //= 2
for i in range(n):
	for j in range(n):
		arr2[i][j] = '2'
		if arr[i][j] == 'C':
			s -= 1
		if s == 0:
			break
	if s == 0:
		break
for i in range(n):
	print(''.join(arr2[i]))
