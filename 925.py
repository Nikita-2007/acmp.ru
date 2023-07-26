if int(input())-1:
	print(min(map(int, input().split())))
else:
	n, a, b, c = map(int, input().split())
	print(max(sum([a, b, c])-n*2, 0))
