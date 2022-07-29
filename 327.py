def test(S): return sum(map(int, str(S%1000))) == sum(map(int, str(S//1000)))
for i in range(int(input())):
	S = int(input())
	print('Yes') if test(S+1) or test(S-1) else print('No')
