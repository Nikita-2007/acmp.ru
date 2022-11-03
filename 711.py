n, m = map(int, input().split())
mini = 999999
for i in range(n):
	name = input()
	kr = sum(map(int, input().split()))
	if kr < mini:
		rez = name
		mini = min(mini, kr)
print(rez)
