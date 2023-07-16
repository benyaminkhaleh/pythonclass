import random
my_list=[]
number = 0
tole=int(input('Tole list ra mosshakhas konid: '))
for i in range(tole):
    number= random.randint(0,100)
    my_list.append(number)
print(my_list)