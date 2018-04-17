a = int(input('Enter the first numer: '))
b = int(input('Enter the second numer: '))
if a == b:
    print(a, '=', b)
elif a > b:
    print(a, '>', b)
    print(a, 'is bigger')
else:
    print(a, '<', b)
    print(b, 'is bigger')