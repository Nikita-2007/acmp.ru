n = input()
arr = ['00:00', '01:10', '02:20', '03:30', '04:40', '05:50', '10:01', '11:11', '12:21', '13:31', '14:41', '15:51', '20:02', '21:12', '22:22', '23:32', '00:00']
if n in arr:
	print(arr[arr.index(n)+1])
else:
	for i in range(16):
		if n < arr[i]:
			print(arr[i])
			break
		elif i == 15:
			print('00:00')
