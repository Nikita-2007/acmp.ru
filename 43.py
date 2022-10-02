s = maxi = 0
for i in input():
	if i == '0':
		s+=1
		maxi = max(s, maxi)
	else:
		s = 0
print(maxi)
