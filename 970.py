arr = list(map(int, input().split()))
if ((arr[0] + arr[1]) == arr[2]) or ((arr[0] + arr[2]) == arr[1]) or ((arr[2] + arr[1]) == arr[0]):
    print("YES")
else:
    print("NO")
