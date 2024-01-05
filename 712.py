w, h, n = map(int, input().split())
f = w*n
mini = f
for i in range(1, n):
	x = f // i
	if x < h*i:
		break
	s = (int(x**0.5)+1)**2
	mini = min(mini, f)
print(f)
