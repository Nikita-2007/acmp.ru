A, B = map(int, input().split())
while A != 0 and B != 0:
    if A > B:
        A %= B
    else:
        B %= A
print(A + B)
