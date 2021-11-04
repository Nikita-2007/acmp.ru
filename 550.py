N = int(input())
if N % 400 == 0:
    print('12/09/' + str(f'{N:04}'))
elif N % 4 == 0 and N % 100 != 0:
    print('12/09/' + str(f'{N:04}'))
else:
    print('13/09/' + str(f'{N:04}'))
