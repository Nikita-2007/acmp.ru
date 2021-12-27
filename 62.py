N = input()
x = N[0:1]
x = True if x == 'A' or x == 'C' or x =='E' or x == 'G' else False
if int(N[1:2]) % 2 == 0 and x: print('WHITE')
elif int(N[1:2]) % 2 == 1 and not x: print('WHITE')
else: print('BLACK')
