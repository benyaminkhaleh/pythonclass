my_list =[]
counter = 0
new_my_list=[]
for i in range(10):
    i =int(input('Enter yor number: '))
    my_list.append(i)
while counter < len(my_list):
    new_my_list.append(my_list[counter] + 2)
    counter+=1
print(my_list)
print(new_my_list)

