N = int(input())
r = maxi = 0;
arr = list(map(int, input().split()))
for i in range(N):
	if arr[i] >= 1:
		r += 1
	else:
		maxi = max(r, maxi)
		r = 0
	maxi = max(r, maxi)
print(maxi)
