N = int(input())
arr_5 = list(map(int, input().split()))
arr_3 = arr_5.copy()
arr_3.reverse()
arr_1 = arr_5.copy()
arr_1.sort()

summ = [0, 0, 0]
for i in range(N):
    summ[0] += arr_5[i]
    summ[1] += arr_3[i]
    summ[2] += arr_1[i]
print(max(summ))
