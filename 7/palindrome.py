str = input("Enter your sentence: ")
str = str.split()
str = ''.join(str)

a = -1
for i in range(len(str)//2):
    if str[i] != str[a]:
        print('no')
        exit(0)
    else:
        a += -1
print('yes')