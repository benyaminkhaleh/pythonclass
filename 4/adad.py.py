x=int(input('Enter your number: '))

if x%2==0 and x>=6:
    print('A')
elif x%2==0 and x<=4:
    print('B')
elif x<0:
    print('D')
else:
    print('C')
