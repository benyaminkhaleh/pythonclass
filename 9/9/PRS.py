import random
import pyfiglet

pf = pyfiglet.figlet_format("rock  paper  scissors", font="charact2") # 5lineoblique, 3-d, slant, banner3-D
print(pf)

a = int(input("1 = 1player, 2 = 2player : "))
c = int(input("1 or 3 or 5 : "))
computer= 0
user1= 0
user2 = 0
RPS = ["rock","paper","scissors"]

if a == 1:
    while True:
        if computer == c or user1 == c:
            break

        computer = random.choice(RPS)
        user = input("1_rock\t2_paper\t3_scissors\tChose one : ")
        print(f"computer : {computer} and user : {user} \n")

        if user == "rock":
            a = {"scissors" : "user", "paper" : "computer", "rock" : "draw"}
            for i in a:
                if computer == i:
                    b = a.get(i)
                
        elif user == "paper":
            a = {"scissors" : "computer", "paper" : "draw", "rock" : "user"}
            for i in a:
                if computer == i :
                    b = a.get(i)

        elif user == "scissors":
            a = {"scissors" : "draw", "paper" : "user", "rock" : "computer"}
            for i in a:
                if computer == i:
                    b = a.get(i)

        if b == "user":
            user1 += 1
            print("user win!!")
        elif b == "computer":
            computer_c += 1
            print("computer win")
        else:
            print("draw")

        print(f"user : {user_c} and computer : {computer_c}")

elif a == 2:
    while True:
        if user2 == c or user1 == c:
            break

        user = input("user : rock or paper or scissors \t")
        user2 = input("user2 : rock or paper or scissors \t")
        print(f"user2 : {user2} and user : {user1} \n")
        
        if user == "rock":
            a = {"scissors" : "user", "paper" : "user2", "rock" : "draw"}
            for i in a:
                if user2 == i :
                    b = a.get(i)
                
        elif user == "paper":
            a = {"scissors" : "user2", "paper" : "draw", "rock" : "user"}
            for i in a:
                if user2 == i :
                    b = a.get(i)

        elif user == "scissors":
            a = {"scissors" : "draw", "paper" : "user", "rock" : "user2"}
            for i in a:
                if user2 == i  :
                    b = a.get(i)

        if b == "user":
            user1 += 1
            print("user win!!")
        elif b == "user2":
            user2 += 1
            print("user2 win")
        else:
            print("draw")

        print(f"user : {user_c} and user2 : {computer_c}")