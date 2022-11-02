x = 0
for i in range(int(input())):
	x += sum(map(int, input().split()))
print(x//2)
