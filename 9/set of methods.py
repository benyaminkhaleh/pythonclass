Fruits = {'apple','banana','mango'}
Fruits.add('orange')
print(Fruits)

Fruits = {'apple','banana','mango'}
Fruits.clear()
print(Fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.discard("pine apple") 
print(fruits)
 # Farqh discord ba remove in hast keh agare chizy baray hazf kardan nabasheh
 #  remove khata mideh amma discord khod set ro chop mikoneh
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# mesal
x = {"apple", "banana", "cherry"}
add = 0
while not add == 2:
    y = input('fruit ezafeh konid:')
    x.add(y)
    add += 1
print(x)





