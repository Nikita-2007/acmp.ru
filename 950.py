arr, n = [], 0
for i in input():
	if i == '0':
		n += 1
	else:
		arr.append('abcdefghijklmnopqrstuvwxyz'[n])
		n = 0
print(''.join(arr))
