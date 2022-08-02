N, M, Y, X = map(int, input().split())
print(M*Y-(M+1)+X) if Y % 2 == 1 else print(M*Y-X)
