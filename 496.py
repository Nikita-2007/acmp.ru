n = int(input())
maxi = 0
arr = list(map(int, input().split()))
for i in range(n-2):
	maxi = max(arr[i] + arr[i+1] + arr[i+2], maxi)
print(max(maxi, arr[0] + arr[1] + arr[n-1], arr[0] + arr[n-1] + arr[n-2]))
