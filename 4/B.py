cm=float(input("Enter your height in the centimeter: "))
w=float(input("Enter your weight in the kilogram: "))

h=cm/100

bmi=w/h**2

if bmi < 0:
    print('invalid')
elif bmi < 18.5:
    print('thin')
elif 18.5 <=bmi < 25:
    print('normal')
elif 25 <= bmi < 30:
    print('on the verge of obesity')
elif 30 <=bmi < 35:
    print('fat')
else:
    print('very fat')






