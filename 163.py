s = input()
if s[0] == 'x':
	print(int(s[4])-int(s[1:3]))
elif s[4] == 'x':
	print(int(s[0])+int(s[1:3]))
else:
	print(int(s[0])-int(s[4])) if s[1]=='-' else print(int(s[4])-int(s[0]))
