N = int(input())
arr = list(map(int, input().split()))
arrA, arrB = [], []
for i in arr:
	if i % 2 == 1:
		arrA.append(i)
	else:
		arrB.append(i)
print(*arrA)
print(*arrB)
if len(arrA) <= len(arrB):
	print('YES')
else:
	print('NO')
