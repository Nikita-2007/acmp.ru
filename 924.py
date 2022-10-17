arr = []
t = 'Yes'
for i in range(4):
	arr.append(input())
for i in range(3):
	for j in range(3):
		if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1]:
			t = 'No'
			break
print(t)
