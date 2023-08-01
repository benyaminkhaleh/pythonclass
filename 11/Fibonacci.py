def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
       
n = int(input('Enter your number:  '))
print(fibonacci(n)) 