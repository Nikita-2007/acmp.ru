n = int(input())
maxi = 0
t = 1
arrf = list(map(int, input().split()))
arrn = list(map(int, input().split()))
for i in range(n):
	if maxi < arrf[i]/100*arrn[i]:
		maxi = arrf[i]/100*arrn[i]
		t = i+1
print(t)
