number =input('Enter your number: ')
n0=number.count('0')
n1=number.count('1')
n2=number.count('2')
n3=number.count('3')
n4=number.count('4')
n5=number.count('5')
n6=number.count('6')
n7=number.count('7')
n8=number.count('8')
n9=number.count('9')

n0=int(n0)
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
n6=int(n6)
n7=int(n7)
n8=int(n8)
n9=int(n9)

e = int(n0+n2+n4+n6+n8)
o = int(n1+n3+n5+n7+n9)

if e>o:
    print('Even')
elif o>e:
    print('Odd')
else:
    print('equal')

