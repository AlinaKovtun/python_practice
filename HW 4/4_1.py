import math
import sys


op_list = ['+', '-', '*', '/', '%', '^', 'sqrt', 'sin', 'cos', 'tg']

 
def Calc(a, op):
    s = []
    if op == '+':
        try_b()
        print(a+b)
        s.append(a+b)
    elif op == '-':
        try_b()
        print(a-b)
        s.append(a-b)
    elif op == '*':
        try_b()
        print(a*b)
        s.append(a*b)
    elif op == '/':
        try_b()
        print(a//b)
        s.append(a//b)
    elif op == '%':
        try_b()
        print(a%b)
        s.append(a%b)
    elif op == '^':
        try_b()
        print(math.pow(b,a))
        s.append(math.pow(b,a))
    elif op == 'sqrt':
        print(math.sqrt(a))
        s.append(math.sqrt(a))
    elif op == 'sin':
        print(math.sin(a))
        s.append(math.sin(a))
    elif op == 'cos':
        print(math.cos(a))
        s.append(math.cos(a))
    elif op == 'tg':
        print(math.tan(a))
        s.append(math.tan(a))    

def try_a():
    try:
        global a
        a = int(input('a = '))
    except ValueError:
        print('Invalid input!')
        try_a()

def try_op():
    global op
    op = input('Operation (+  -  *  /  %  ^  sqrt  sin  cos  tg): ')
    if not op in (op_list):
            print('Invalid input!')
            try_op()
            
def try_b():
    try:
        global b
        b = int(input('b = '))
    except ValueError:
        print('Invalid input!')
        try_b()            
            
def repeat():
    rep = input('Press any key to continue, press "x" to exit.')
    if rep == 'x':
            return False
    else:
        return True
        
def input_data(): 
    if repeat():
        try_a() 
        try_op()
    elif not repeat():
        sys.exit()
    Calc(a, op)  
    input_data()

        
input_data()        



