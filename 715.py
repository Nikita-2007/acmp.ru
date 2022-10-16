x, y = map(int, input().split())
arr = []
arr2 = []
r = 0
for i in range(x):
	arr.append(input())
input()
for i in range(x):
	arr2.append(input())

for i in range(x):
	for j in range(y):
		if arr[i][j:j+1] == arr2[i][j:j+1]:
			r += 1

print(r)
