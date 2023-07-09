fruits = ['apple','banana','cherry']
x=fruits.copy()
print(x)

fruits = ['apple','cherry','mango']
fruits.insert(1,"orange")
print(fruits)

fruits = ['apple','cherry','mango']
z = fruits.index('mango')
print(z)

fruits = ['apple','cherry','mango']
cars=['Ford','BMW','Volvo']
fruits.extend(cars)
print(fruits)