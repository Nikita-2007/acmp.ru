n = int(input())
arr = list(map(int, input().split()))
arr2 = [0, 0]
for i in range(n):
	if arr[0] >= arr[-1]:
		arr2[i%2] += arr[0]
		arr.pop(0)
	else:
		arr2[i%2] += arr[-1]
		arr.pop(-1)
print(str(arr2[0])+':'+str(arr2[1]))
