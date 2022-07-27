n = int(input())
arr = list(map(int, input().split()))
arr2= []
m = int(input())
for i in range(m):
  l, r = map(int, input().split())
  for j in range(l, r+1):
    arr2.append(arr[j-1])
  print(*arr2)
  arr2 = []
