N = int(input())
print(N*(N+1)*(N+2)//2 )

#1. Тупой перебор
#for i in range(N+1):
#    for j in range(i, N+1):
#        S += i+j
#2. Перебор с алгоритмом
#for i in range(N+1):
#    S += i * (N-i+1) + ((i+N) * (N-i+1)//2)
#3.Формула
#print(N*(N+1)*(N+2)//2)
