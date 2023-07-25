import random

animal =['dog','cat','mankey','lion','giraffe','chicken','cheetah','tiger','lizard']
color =['black','white','blue','red','yellow','green','purple','gray','golden','brown']
car =['ford','benz','bmw','ferrari','toyota','porsche','lamborghini','maserati','astonmartin','renault']
soccer_player =['ronaldo','messi','zlatan','mbappe','buffon','neuer','aguero','neymar','holland','pique']
country =['iran','usa','japan','itali','spain','france','germany','brazil','australia','egypt']

w1 = random.choice(animal)
w2 = random.choice(color)
w3 = random.choice(car)
w4 = random.choice(soccer_player)
w5 = random.choice(country)

show_w = []

op =int(input('1_animal\t2_color\t3_car\t4_socer player\t5_country:Choose one to play: '))
if op == 1:
    chance = (len(w1) * 1.5) // 1
    for i in range(len(w1)):
        show_w.append('_')
    while not chance == 0 :
        print(' '.join(show_w))
        print('*' * int(chance))
        if not('_' in show_w):
            print('You win!')
            break

        user_char = input('Enter charter : ')
        idx = 0
        user_char = user_char.lower()
        if user_char in w1:
            for j in w1:
                if user_char == j:
                    show_w[w1.index(j,idx)]=user_char
                idx += 1

        else:
            if not chance == 1 :
                print('try again')
            chance -= 1

    if chance == 0 :
        print('Game over')

elif op == 2 :
    chance = (len(w2) * 1.5) // 1
    for i in range(len(w2)):
        show_w.append('_')
    while not chance == 0 :
        print(' '.join(show_w))
        print('*' * int(chance))
        if not('_' in show_w):
            print('You win!')
            break

        user_char = input('Enter charter : ')
        idx = 0
        user_char = user_char.lower()
        if user_char in w2:
            for j in w2:
                if user_char == j:
                    show_w[w2.index(j,idx)]=user_char
                idx += 1

        else:
            print('try again')
            chance -= 1

    if chance == 0 :
        print('Game over')

elif op == 3 :
    chance = (len(w3) * 1.5) // 1
    for i in range(len(w3)):
        show_w.append('_')
    while not chance == 0 :
        print(' '.join(show_w))
        print('*' * int(chance))
        if not('_' in show_w):
            print('You win!')
            break

        user_char = input('Enter charter : ')
        idx = 0
        user_char = user_char.lower()
        if user_char in w3:
            for j in w3:
                if user_char == j:
                    show_w[w3.index(j,idx)]=user_char
                idx += 1

        else:
            print('try again')
            chance -= 1

    if chance == 0 :
        print('Game over')

elif op == 4 :
    chance = (len(w4) * 1.5) // 1
    for i in range(len(w4)):
        show_w.append('_')
    while not chance == 0 :
        print(' '.join(show_w))
        print('*' * int(chance))
        if not('_' in show_w):
            print('You win!')
            break

        user_char = input('Enter charter : ')
        idx = 0
        user_char = user_char.lower()
        if user_char in w4:
            for j in w4:
                if user_char == j:
                    show_w[w4.index(j,idx)]=user_char
                idx += 1

        else:
            print('try again')
            chance -= 1

    if chance == 0 :
        print('Game over')

elif op == 5 :
    chance = (len(w5) * 1.5) // 1
    for i in range(len(w5)):
        show_w.append('_')
    while not chance == 0 :
        print(' '.join(show_w))
        print('*' * int(chance))
        if not('_' in show_w):
            print('You win!')
            break

        user_char = input('Enter charter : ')
        idx = 0
        user_char = user_char.lower()
        if user_char in w5:
            for j in w5:
                if user_char == j:
                    show_w[w5.index(j,idx)]=user_char
                idx += 1

        else:
            print('try again')
            chance -= 1

    if chance == 0 :
        print('Game over')
