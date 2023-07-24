if int(input())-1:
	print(min(map(int, input().split())))
else:
	n, a, b, c = map(int, input().split())
	arr = [a, b, c]
	print(max(sum(arr)-n*2), 0)
