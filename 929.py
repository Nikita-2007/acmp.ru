N = int(input())
a = (N - (N // 6 * 6))
if a == 1:
    a = 6
elif a == 2:
    a = 5
elif a == 3:
    a = 4
elif a == 4:
    a = 3
elif a == 5:
    a = 2
elif a == 6:
    a = 1
print(a + (N // 6), N*6)
