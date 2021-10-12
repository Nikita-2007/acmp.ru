arr = list(map(int, input().split()))
if arr[2]*2 <= arr[0] and arr[2]*2 <= arr[1]:
    print("YES")
else:
    print("NO")