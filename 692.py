N = int(input())
x = 1
while True:
    if N == x:
       print('YES')
       break
    elif N > x:
        x = x*2
    else:
        print('NO')
        break