x =int(input('Enter your number: '))
for i in range(1,x + 1):
    for j in range(1, i + 1):
        print(j,end="")
    print()



for i in range(x, 0, -1):
    for j in range(1, i + 1):
        print(j,end="")
    print()

