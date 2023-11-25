n = int(input())
q = []
arr = []
d = []
for i in range(n):
	arr.append(list(map(int, input().split())))
	d.append(n**n)
s, f = map(int, input().split())
s, f = s-1, f-1
q.append(s)
d[s] = 0
while len(q) > 0:
	t = q[0] #Номаер проверяемой вершиныы
	q.pop(0) #Убираем из очереди
	for i in range(n):
		if arr[t][i] > 0 and d[i] > d[t]+1:
			q.append(i)
			d[i] = d[t]+1 #Добовляем растояние(может быть не только 1)
if d[f] < n*n:
	print(d[f])
else:
	print(-1)
