K = int(input())
A, B, C = 'G', 'C', 'V'
for i in range(K % 3):
    A, B, C = C, A, B
print(A + B + C)
 
