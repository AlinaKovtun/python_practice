def Calc():
    s = []
    a = int(input())
    op = input()
    if op == '+':
        b = int(input())
        print(a+b)
        s.append(a+b)
    elif op == '-':
        b = int(input())
        print(a-b)
        s.append(a-b)
    elif op == '*':
        b = int(input())
        print(a*b)
        s.append(a*b)
    elif op == '/':
        b = int(input())
        print(a//b)
        s.append(a//b)
    elif op == '%':
        b = int(input())
        print(a%b)
        s.append(a%b)
    else:
        print('Invalid input')
        Calc()

        
Calc()   
repeat = input('Do you want to repeat? (1 - yes, 2 - no)')
if repeat == '1':
    Calc()

