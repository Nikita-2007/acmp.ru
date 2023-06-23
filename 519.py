n = list(input())
n.sort()
s = n.copy()
s = n.copy()
n[n.count('0')], n[0] = n[0], n[n.count('0')]
print(''.join(n),''.join(s[::-1]))
