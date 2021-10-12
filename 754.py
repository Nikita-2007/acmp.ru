arr = list(map(int, input().split()))
if (arr[0] < 94) or (arr[1] < 94) or (arr[2] < 94) or (arr[0] > 727) or (arr[1] > 727) or (arr[2] > 727):
    print("Error")
else:
    arr.sort()
    print(arr[2])