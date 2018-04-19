#5.1 Прочитати два числа та: 
#    • вивести значення бiльшого iз них; 
#    • вивести словами, чи перше було бiльше, чи друге, чи вони рiвнi.
#5.2 Вивести бiльше iз введених 5 чисел.
#5.3 Читати з клавiатури числа, поки не ввели лiтеру ‘x’. Вивести: 
#    • найбiльше, 
#    • найменше, 
#    • суму, 
#    • кiлькiсть парних, 
#    • кiлькiсть додатних.
#P.S. Програма повинна коректно працювати,  навіть коли введено лише вiд’ємнi числа. При запуску аплікації має бути вибір яку з 3 операцій ми хочемо виконати (5.1, 5.2, 5.3).

def input_numbers(n = None):
    nums = list()
    if n != None:
        count = 0
        while count < n:
            nums.append(int(input()))
            count += 1
    else:
        
        while True:
            a = input()
            if a == 'x':
                break
            nums.append(int(a)) 
    return nums        
    

def select_operation():
    op = int(input("Choose which operation do you want to execute (1,2,3): "))
    return op


def first_op():
    nums_list = input_numbers(2)
    nums_list_g = sorted(nums_list, reverse = True)
    print('The greater number is', nums_list_g[0])
    if nums_list == nums_list_g:
        print('The first number is greater.')
    else:
        print('The second number is greater.')


def second_op():
    nums_list = input_numbers(5)
    nums_list_g = sorted(nums_list, reverse = True)
    print('The greater number is', nums_list_g[0])
    

def third_op():
    nums_list = input_numbers()
    nums_list_g = sorted(nums_list, reverse = True)
    print('The greater number is', nums_list_g[0])
    nums_list_s = sorted(nums_list)
    print('The smaller number is', nums_list_s[0])
    
    count_even = 0
    for i in nums_list:
        if i % 2 == 0:
            count_even += 1
    print('Number of even numbers', count_even)   
    
    count_positive = 0
    for i in nums_list:
        if i > 0:
            count_positive += 1
    print('Number of positive numbers', count_positive) 


def execute_op():
    operation = select_operation()
    if operation == 1:
        first_op()
    elif operation == 2:
        second_op()
    elif operation == 3:
        third_op()
    else:
        print('Invalid input. Try again')
        execute_op()


execute_op()      