N = int(input())
arr = list(map(int, input().split()))
k = int(input())
s = 0
for i in range(N):
	s += min(arr[i], k)
print(s)
