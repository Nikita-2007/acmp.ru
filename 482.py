n = int(input())
arr = [1]
i = f = 1
while n > len(arr):
	for j in str(i):
		arr.append(j)
	if i > f:
		i = 1
		f += 1
	else:
		i += 1
print(arr[n-1])
