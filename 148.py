A, B = map(int, input().split())
while A != B:
    if A > B:
        A -= B
    else:
        B -= A        
print(A)
