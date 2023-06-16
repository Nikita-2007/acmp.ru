n1,p1 = map(int,input().split())
n2,p2 = map(int,input().split())
s1 = s2 = 0
while n1 != 0:
	s1 += n1%p1
	n1 = n1//p1
while n2 != 0:
	s2 += n2%p2
	n2 = n2//p2
print(s1) if s1 == s2 else print(0)
