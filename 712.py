w, h, n = map(int, input().split())
maxi = max(w, h)
mini = min(w, h) * n
while (maxi < mini):
    mid = (maxi + mini) // 2;
    if (n <= (mid // w) * (mid // h)):
        mini = mid
    else:
        maxi = mid + 1
print(maxi)
