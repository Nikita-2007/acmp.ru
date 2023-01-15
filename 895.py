t = 1
arr = []
for i in range(3):
	arr.append(list(input()))
for i in range(3):
	if arr[i][0] == arr[i][1] == arr[i][2] or arr[0][i] == arr[1][i] == arr[2][i]:
		if arr[i][i] == 'X':
			print('Win')
			break
		elif arr[i][i] == 'O':
			print('Lose')
			break
if arr[0][0] == arr[1][1] == arr[2][2] or arr[0][2] == arr[1][1] == arr[2][0]:
	if arr[1][1] == 'X':
		print('Win')
	elif arr[1][1] == 'O':
		print('Lose')
	else:
		t = 0
		print('Draw')
elif t:
	print('Draw')
