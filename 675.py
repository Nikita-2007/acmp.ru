n, m = map(int, input().split())
mini = 1e10
for i in range(n):
	mini = min(mini, input().count('.'))
print(mini)
