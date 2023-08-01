import random

animal =['dog','cat','mankey','lion','giraffe','chicken','cheetah','tiger','lizard']
color =['black','white','blue','red','yellow','green','purple','gray','golden','brown']
car =['ford','benz','bmw','ferrari','toyota','porsche','lamborghini','maserati','astonmartin','renault']
soccer_player =['ronaldo','messi','zlatan','mbappe','buffon','neuer','aguero','neymar','holland','pique']
country =['iran','usa','japan','itali','spain','france','germany','brazil','australia','egypt']

def choose_word() :
    while True:
        op = input('animal\tcolor\tcar\tsoccer_player\tcountry: ')
        if op == 'animal' :
            word = random.choice(animal)
            break
        elif op == 'color' :
            word = random.choice(color)
            break

        elif op == 'car' :
            word = random.choice(car)
            break

        elif op == 'soccer_player' :
            word = random.choice(soccer_player)
            break
        else :
            word = random.choice(country)
            break
    return word
def heart(word):
    chance = (len(word) * 1.5) // 1
    show_w =[]
    for i in range(len(word)):
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
        if user_char in word:
            for j in word:
                if user_char == j:
                    show_w[word.index(j,idx)]=user_char
                idx += 1
        else:
            if not chance == 1 :
                print('try again')
            chance -= 1
while True :
    word = choose_word()
    heart(word)
    try_again = input("do you want to try agian?(y, n)\t")
    if try_again != "y":
        break
    