e = '2.71828182845904523536028750'
n = int(input())
if n == 0:
	print(3)
else:
	print(e[:n+1]+str(int(e[n+1])+1)) if e[n+2] > '4' else print(e[:n+2])
