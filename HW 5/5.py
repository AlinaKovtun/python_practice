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
    print(nums)
            

    
input_numbers(2) 
input_numbers(5)
input_numbers()
        