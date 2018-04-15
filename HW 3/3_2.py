#fionacci
def fibonacci():
    n = int(input('Enter n: '))
    prev1 = 0 
    prev2 = 1
    fib = 1
    while fib <= n:
        fib = prev1 + prev2
        print(fib, end = ' ')
        prev1 = prev2
        prev2 = fib
    
fibonacci()    