N, s = int(input()), 0
for i in range(1, N+1):
    if N % i == 0:
        s += i
print(s)
