arr = []
arrN = []
n = 0
for i in range(int(input())):
	for j in range(int(input())):
		f, s = map(str, input().split())
		f = float(f)
		for k in range(len(arr)):
			if f > arr[k]:
				n = k
				break
			elif f == arr[k]:
				for m in range(arr.count(arr[k])):
					if str(str(f)+' '+s).swapcase() < arrN[k+m].swapcase():
						n = k+m
						#print(m, arrN, str(str(f)+' '+s).swapcase(), arrN[k+m].swapcase())
						break
					else:
						n = k+1+m
			else:
				n = len(arr)
		arrN.insert(n, str(str(f)+' '+s))
		arr.insert(n, f)
print(len(arr))
for i in range(len(arr)):
	print(arrN[i])
