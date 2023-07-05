u=('Benyamin')
p=('1b3e8n5i')

x=input('Enter username: ')
y=input('Enter password: ')

if x==u and y==p:
    print("You are alloto enter")
elif x==u:
    y=input('Try again enter your password: ')
    if y==p:
        print("You are alloto enter")
    else:
        print('invalid')
else:
    print('invalid')



