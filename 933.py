A, B, C, T = map(int, input().split())
if T <= A:
    print(T*B)
else:
    print(A*B +(T-A)*C)
