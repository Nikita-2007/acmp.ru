n = int(input())
f = 'Correct'
arrR = []
for i in range(n*n):
	arrR.append(list(map(int, input().split())))
arrC = list(zip(*arrR))
for i in range(n*n):
	arrC[i] = list(arrC[i])

for i in range(n*n):
	for j in range(1, n*n+1):
		if j not in arrR[i] or j not in arrC[i]:
			f = 'Incorrect'
			break
	if f == 'Incorrect':
		break

if f == 'Correct':
	for k1 in range(0, n*n, n):
		for k2 in range(0, n*n, n):
			t = []
			for i in range(n):
				for j in range(n):
					t.append(arrR[i+k1][j+k2])
			for j in range(1, n*n+1):
				if j not in t:
					f = 'Incorrect'
					break
			if f == 'Incorrect':
				break
		if f == 'Incorrect':
			break
print(f)
