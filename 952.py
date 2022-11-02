n, m = map(int, input().split())
print('Impossible') if n <= 0 and m != 0 else print(n + max(m-n, 0), n + max(m-1, 0)) 
