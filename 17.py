n = int(input())-1
arr = list(map(int, input().split()))
el = []
t = False
f = -1
for i in range(1, n+1):
	if n%i == 0:
		sek = n//i
		t = True
		for j in range(i):
			if arr[j*sek:(j+1)*sek] != arr[0:sek]:
				t = False
				break
		if t:
			f = sek
print(f)
