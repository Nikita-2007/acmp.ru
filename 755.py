arr = list(map(int, input().split()))
if arr[0] + arr[1] < arr[2]:
    print("Impossible")
else:
    print(arr[0] + arr[1] - arr[2])
