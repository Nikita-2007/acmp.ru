s = ''
n = input()
arr = [1, 1]
for i in range(len(n)):
	if arr[i]+arr[i+1] < len(n)+1:
		arr.append(arr[i]+arr[i+1])
	else:
		arr.pop(1)
		break
for i in range(len(arr)):
	s += n[arr[i]-1]
print(''.join(s))
