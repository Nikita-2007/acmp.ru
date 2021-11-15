for i in range(int(input())):
    n, m = map(int, input().split())
    print(19*m + (n + 239)*(n + 366) // 2)
