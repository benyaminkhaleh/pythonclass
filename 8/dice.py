import random
number = 0
number_list = []
n = 0
while not number == 6:
    number_list.append(number)
    number =random.randint(1,6)
    n += 1
    if number == 6:
        print(f"you got 6 and you won {n} round")
    else:
        print(f'try again, You got:', number)
print('The sum of all the numbers you got =', sum(number_list) + 6)