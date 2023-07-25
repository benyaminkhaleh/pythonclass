car ={'brand' : 'Iran khodro','model' : 206 ,'year': 2000 }
car.clear()
print(car)

car ={'brand' : 'Iran khodro','model' : 206 ,'year': 2000 }
car.copy()
print(car)

car ={'brand' : 'Iran khodro','model' : 206 ,'year': 2000 }
x = car.get('model')
print(x)

car ={'brand' : 'Iran khodro','model' : 206 ,'year': 2000 }
x = car.items()
car['year'] = 2010
print(x)

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
car["color"] = "white"
print(x)

car = {"brand": "Ford","model": "Mustang","year": 1964}
car.pop("model")
print(car)

car = {"brand": "Ford","model": "Mustang","year": 1964}
car.update({"color": "White"})
print(car)

car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
car["year"] = 2018
print(x)


x =(1,2,3)
y = 6
top = dict.fromkeys(x,y)
print(top)

car ={'brand' : 'Iran khodro','model' : 206 ,'year': 2000 }
y = car.items
for i in range(len(y)):
    print(car)
    





