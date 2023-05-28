team = input()
arr = []
for i in range(3):
	arr.append(input())
arr.sort()
print(team+": "+', '.join(arr))
