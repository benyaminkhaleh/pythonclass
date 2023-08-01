import random

def winer(x , computer) :
    if computer == x:
        return f"computer is {computer}"," win!"
    elif computer > x:
        return f"computer is {computer}","go dawn !"
    else:
        return f"computer is {computer}","go up !"

def game(x) :
    x =int(input('Enter your number'))
    ma = 100
    mi = 0
    computer =random.randint(mi , ma)
    while True :
        w = winer(x , computer)
        if computer == x :
            print(w)
            break
        elif computer > x: 
            print(f"computer number is:{x}", w)
            ma = x
            computer = random.randint(mi , ma - 1)
        else :
            print(f"computer number is:{x}", w)
            ma = x
            computer = random.randint(mi - 1 , ma )

while True :
    start_game = winer
    game(start_game)
    try_again = input("do you want to try again?(y, n):\t") # try again
    if try_again == "n":
        break
print("good bye!")