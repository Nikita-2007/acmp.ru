arr = [0]*5
for i in range(5):
	x, y = map(int, input().split())
	mini = 0
	for j in range(5):
		if ((x-25*j)**2+y**2)**0.5 <= 10:
			arr[j] = 1
print(sum(arr))
