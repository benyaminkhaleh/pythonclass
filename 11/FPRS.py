import random
import pyfiglet

pf = pyfiglet.figlet_format("rock  paper  scissors", font="charact2") # 5lineoblique, 3-d, slant, banner3-D
print(pf)

a = int(input('1_one player\t2_two player\tHow many people do you want?: '))
b = int(input('How many rounds do you want?(1 or 3 or 5): '))
rps = ['rock' , 'paper' , 'scissor']
player1 = 0
player2 = 0
computer = 0
if a == 1 :
    def check_game1(p1) :
        while True :
            p1=int(input('1_rock\t2_paper\t3_scissor\tEnter your number: '))
            c =random.choice(rps)
            if p1 == 1 :
                if c == 'rock' :
                    print("draw")
                elif c == 'paper' :
                    print("computer win rounds")
                    computer += 1
                else :
                    print("player1 win rounds")
                    player1 += 1
            elif p1 == 2 :
                if c == 'paper' :
                    print("draw")
                elif c == 'rock' :
                    print("player1 win rounds")
                    player1 += 1
                else :
                    print("computr win rounds")
                    computer += 1
            else :
                if c == 'scissor' :
                    print("draw")
                elif c == 'paper' :
                    print("player1 win rounds")
                    player1 += 1
                else :
                    print("computr win rounds")
                    computer += 1
            if player1 == b or computer == b :
                if player1 == b :
                    winer =print('player1 winer')
                    return Winer 
                else :
                    winer = print('computer winer')    
                    return Winer 
            
if a == 2 :
    def check_game2(p1 , p2) :
        p1=int(input('1_rock\t2_paper\t3_scissor\tEnter your number: '))
        p2=int(input('1_rock\t2_paper\t3_scissor\tEnter your number: '))
        if p1 == 1 :
            if p2 == 'rock' :
                print("draw")
            elif p2 == 'paper' :
                print("player2 win rounds")
                player2 += 1
            else :
                print("player1 win rounds")
                player1 += 1
        elif p1 == 2 :
            if p2 == 'paper' :
                print("draw")
            elif p2 == 'rock' :
                print("player1 win rounds")
                player1 += 1
            else :
                print("player2 win rounds")
                player2 += 1
        else :
            if p2 == 'scissor' :
                print("draw")
            elif p2 == 'paper' :
                print("player1 win rounds")
                player1 += 1
            else :
                print("player2 win rounds")
                player2 += 1
        if player1 == b or player2 == b :
            if player1 == b :
                winer = player1
                return winer
            else :
                winer = player2
                return winer

if a == 1 :
    x = check_game1(winer)
else :
    x = check_game2(winer)
print(x)


