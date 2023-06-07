n, m, k = map(int, input().split())
print(n*(min(k-1, m) + m // k))
