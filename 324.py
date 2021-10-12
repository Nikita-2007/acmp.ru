N = int(input())
arr = []
for i in range(4):
    arr.append(N % 10)
    N = N // 10
if arr[0] == arr[3] and arr[1] == arr[2]:
    print('YES')
else:
    print('NO')