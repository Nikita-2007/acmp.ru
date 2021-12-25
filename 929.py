N = int(input())
a = (N - (N // 6 * 6))
if a == 0:
    a += 7
print(7 - a + (N // 6), N*6)
