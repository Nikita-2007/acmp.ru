s, f = map(str, input().split())
s = list(s.lower())
f = list(f.lower())
s.sort()
f.sort()
if s == f:
	print('Yes')
else:
	print('No')
