n = input()
if n == '6174':
	print(6174, "\n"+'0')
else:
	n = ''.join(sorted(n))
	x = n[::-1]
	for i in range(1, 8):
		if int(x) - int(n) == 6174:
			print(6174, "\n"+str(i))
			break
		n = str(int(x) - int(n)).zfill(4)
		n = ''.join(sorted(n))
		x = str(n)[::-1]
