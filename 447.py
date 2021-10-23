N = int(input())
x = 1
for i in range(1, N+1):
    x *= i
x = str(x)
while True:
    if x[-1] == '0':
        x = x[:-1]
    else:
        break
print(x[-1])
