N = input()
print('BLACK') if (ord(N[0:1]) + int(N[1:2])) % 2 == 0 else print('WHITE')
