def isprime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
x =int(input('Enter your number: '))
y = isprime(x)
print(y)