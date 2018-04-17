a = int(input('Enter 2 numbers\n1: '))
b = int(input('2: '))

if (a > b):
    t = b
    b = a
    a = t

num = a
while (num <= b):
    if (num % 2 == 0):
        print(num)
    num += 1    