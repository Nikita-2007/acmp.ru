N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    if arr[i] <= 437:
       print('Crash', i+1)
       N = 0
       break
if N:
   print('No crash')
