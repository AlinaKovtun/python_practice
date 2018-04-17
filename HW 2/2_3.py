a = int(input('Enter 2 numbers\n1: '))
b = int(input('2: '))

print('\nAscending: ')
if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
elif b < a:
    for i in range(b, a+1):
        print(i, end=' ')
        
print('\nDescending: ')    
if a < b:
    for i in range(b,a-1,-1):
        print(i, end=' ')
elif b < a:
    for i in range(a,b-1,-1):
        print(i, end=' ')