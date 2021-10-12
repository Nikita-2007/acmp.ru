A1, A2, A3, B1, B2, B3 = map(int, input().split())
arrA = [A1, A2, A3]
arrB = [B1, B2, B3]
arrA.sort()
arrB.sort()
print(arrA[0]*arrB[0]+arrA[1]*arrB[1]+arrA[2]*arrB[2])