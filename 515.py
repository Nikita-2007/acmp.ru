arr = [[0, 0]]
s = 0
for i in range(int(input())):
	arr.append(list(map(int, input().split())))
	s += round((abs(arr[i][0]-arr[i+1][0])**2+abs(arr[i][1]-arr[i+1][1])**2)**0.5, 3)
print(round(s+(abs(arr[len(arr)-1][0])**2+abs(arr[len(arr)-1][1])**2)**0.5, 3))
