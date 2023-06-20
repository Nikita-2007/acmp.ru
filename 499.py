k, w = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
if a1+a2+a3<=w and b1+b2+b3>=k:
	print('YES')
elif a1+a2<=w and b1+b2>=k:
	print('YES')
elif a1+a3<=w and b1+b3>=k:
	print('YES')
elif a2+a3<=w and b2+b3>=k:
	print('YES')
elif a1<=w and b1>=k:
	print('YES')
elif a2<=w and b2>=k:
	print('YES')
elif a3<=w and b3>=k:
	print('YES')
else:
	print('NO')
