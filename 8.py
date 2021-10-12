arr = list(map(int, input().split()))
arr[0] = arr[0] * arr[1]
if arr[0] == arr[2]:
    print("YES")
else:
    print("NO")
