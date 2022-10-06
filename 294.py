k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
print((k1-(k1-(k1//100*l1)))*m1 + (k2-(k2-(k2//100*l2)))*m2 + ((k1-(k1//100*l1))-(k2-(k2//100*l2))) * m1) if (k1-(k1//100*l1)) > (k2-(k2//100*l2)) else print((k1-(k1-(k1//100*l1)))*m1 + (k2-(k2-(k2//100*l2)))*m2 + ((k2-(k2//100*l2))-(k1-(k1//100*l1))) * m2)
