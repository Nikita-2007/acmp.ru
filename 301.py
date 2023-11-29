s, k = map(int, input().split())
mini = '1'+'0'*(k-1)
maxi = ('9'*(s//9)+str(s%9)+'0'*k)[:k]
for i in range(k):
	if s-sum(list(map(int, list(mini)))) >= 9:
		mini = mini[:k-i-1] + '9' + mini[k-i:]
	else:
		mini = mini[:k-i-1] + str(s-sum(list(map(int, list(mini))))) + mini[k-i:]
		break
if s-sum(list(map(int, list(mini)))) != 0:
	mini = str(int(mini[0])+1) + mini[1:]
print(maxi, mini)
