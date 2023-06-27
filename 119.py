n = int(input())
arr = []
for i in range(n):
	a, b, c = map(int, input().split())
	arr.append((a*3600)+(b*60)+c)
arr.sort()
for i in range(n):
	a = arr[i]//3600
	b = (arr[i]-a*3600)//60
	c = arr[i]-(a*3600)-(b*60)
	print(a, b, c)
