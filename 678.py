N, arr = input(), [0] * 3
arr[0] = 1
for i in N:
    if i == 'A': arr[0], arr[1] = arr[1], arr[0]
    elif i == 'B': arr[2], arr[1] = arr[1], arr[2]
    else: arr[0], arr[2] = arr[2], arr[0]
print(arr.index(1)+1)
