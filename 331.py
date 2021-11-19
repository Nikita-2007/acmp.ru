H, M = map(int, input().split(':'))
H2, M2 = map(int, input().split())
print(str(f'{((H+H2) + (M+M2) // 60) % 24:02}') + ':' + str(f'{(M+M2) % 60:02}'))
