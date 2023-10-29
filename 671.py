n = int(input())
s = len(str(n))-1
r = 0
for i in range(1, s+1):
	r += 2**i
for i in range(2**(s+1)):
	if int(''.join(['4' if x=='0' else '7' for x in list(('{:0'+str(s+1)+'}').format(int(str(bin(i))[2:])))])) <= n:
		r += 1
	else:
		break
print(r)
