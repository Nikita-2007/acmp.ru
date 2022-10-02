normsim = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
normnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(int(input())):
	s = input()
	if  len(s) == 6 and s[0] in normsim and s[4] in normsim and s[5] in normsim and s[1] in normnum and s[2] in normnum and s[3] in normnum:
		print('Yes')
	else:
		print('No')
