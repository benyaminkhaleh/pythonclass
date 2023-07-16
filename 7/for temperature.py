
while True:
    op=int(input("1_c to k\t2_c to f\t3_k to c\t4_k to f\t5_f to c\t6_f to k\t7_break\Enter your temperature: "))
    if 1 <= op <= 2:
        c=float(input('How many celsius?: '))
        k=273+c
        f=1.8*c+32
        if op==1:
           print(k)
        else:
            print(f)
    elif 3 <= op <= 4:
        k=float(input('How many kelvins?: '))
        c=k-273
        f=1.8*c+32
        if op==3:
            print(c)
        else:
            print(f)
    elif 5 <= op <= 6:  
        f=float(input("How many fahrenheit?: "))
        c=0.55*f-32*0.55
        k=273+c
        if op==5:
            print(c)
        else:
            print(k)
    elif op == 7:
        break
    else:
        print('invalid')


   
