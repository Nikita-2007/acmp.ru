n, i, j = map(int, input().split())
print(min(abs(j-i)-1, n-max(i, j)+min(i, j)-1))
