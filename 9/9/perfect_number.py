number = abs(int(input('Enteer your number : ')))
n = []
for i in range (1 , number) :
    if (number % i ) == 0 :
        n.append(i)

if sum(n) == number :
    print('Your number is perfect')
else :
    print('Your number is not perfect')