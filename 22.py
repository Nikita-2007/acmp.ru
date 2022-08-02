n, k = int(input()), ''
while n > 0:
    k = str(n % 2) + k
    n = n // 2
print(k.count('1'))
