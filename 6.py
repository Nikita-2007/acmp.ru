s = input()
if len(s) != 5 or s[2] != '-' or s[0] in 'ABCDEFGH' == 0 or s[3] in 'ABCDEFGH' == 0 or s[1].isdigit() == 0 or s[4].isdigit() == 0 or int(s[1]) > 8 or int(s[4]) > 8 or int(s[1]) < 1 or int(s[4]) < 1 or (s[3] == s[0] and s[1] == s[4]):
	print('ERROR')
else:
	x1, x2, y1, y2 = ord(s[0])-64, ord(s[3])-64, int(s[1]), int(s[4])
	if (abs(x1-x2) == 1 and abs(y1-y2) == 2) or (abs(x1-x2) == 2 and abs(y1-y2) == 1):
		print('YES')
	else:
		print('NO')
