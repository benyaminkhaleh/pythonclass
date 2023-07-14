x = input('Enter whatever you want: ')
numbers=[0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
letter_and_symbols= []
number_int = 0
for i in numbers:
    for j in x:
        if str(i) == j:
            number_int += i
        else:
            letter_and_symbols.append(j)
print(number_int)