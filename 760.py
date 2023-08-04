n, v, l = map(int, input().split())
arr = list(map(int, input().split()))
f = round(l/v*60, 2)
for i in range(1, n*2, 2):
	f += arr[i]
print(str(f).ljust(len(str(int(f)))+3, '0'))
