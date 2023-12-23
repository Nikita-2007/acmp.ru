n = str(bin(int(input())))[2:]
maxi = 0
for i in range(len(n)):
	n = n[-1] + n[:len(n)-1]
	maxi = max(maxi, int('0b'+n, 2))
print(maxi)
