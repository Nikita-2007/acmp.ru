arr = list(map(int, input().split()))
arr[0] = arr[0] // 2
arr[1] = arr[1] // 6
arr[2] = arr[2] // 1
arr.sort()
print(arr[0])