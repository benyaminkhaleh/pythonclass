x=int(input("Enter your number: "))
if x%7==0:
    print('Yes')
else:
    print('No')
    if x%7==1:
        y=x+6
    elif x%7==2:
        y=x+5
    elif x%7==3:
        y=x+4
    elif x%7==4:
        y=x+3
    elif x%7==5:
        y=x+2
    else:
        y=x+1
    print(y)