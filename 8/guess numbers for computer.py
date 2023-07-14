import random
x =int(input('Enter your number: '))

max = 100
min = 0
computer = random.randint(min,max)
while True:
    if computer == x:
        print(f"computer is {computer}"," win!")
        break
    elif computer > x:
        print(f"computer is {computer}","go dawn !")
        max = x
        computer = random.randint(min,max)
    else:
        print(f"computer is {computer}","go up !")
        min = x
        computer = random.randint(min,max)
        
        



