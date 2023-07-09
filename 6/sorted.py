numbers = []
n1=float(input('Enter your number: '))
n2=float(input('Enter your number: '))
n3=float(input('Enter your number: '))
n4=float(input('Enter your number: '))
n5=float(input('Enter your number: '))

numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
numbers.append(n5)

x = sorted(numbers)
y = x[::-1]
print(x)
print(y)


