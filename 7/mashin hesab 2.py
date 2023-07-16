import math

while True:
    n1=float(input('Enter your number: '))
    n2=float(input('Enter your number: '))
    op=int(input('1_sum\t2_subtraction\t3_multiplication\t4_division\t5_power\t6_log\t7_sin\t8_cos\t9_tan\t10_cot\t11_factorial\t12_sqrt\t13_abs\t14_round\tnenter number of operation: '))
    r = 0
    if 1<= op <= 14:
        if 1 <= op <= 6:
            if op==1:
                r = n1 + n2
            elif op==2:
                r = n1 - n2
            elif op==3:
                r = n1 * n2
            elif op==4:
                if n2==0:
                    r = None
                else:
                    r = n1 / n2
            elif op==5:
                r=math.pow(n1,n2)
            else:
                r=math.log(n1,n2)
        else:
            if op==7:
                x=math.radians(n1)
                r=math.sin(x)
            elif op==8:
                x=math.radians(n1)
                r=math.cos(x)
            elif op==9:
                x=math.radians(n1)
                r=math.tan(x)
            elif op==10:
                x=math.radians(n1)
                r=math.cot(x)
            elif op==11:
                r=math.factorial(n1)
            elif op==12:
                r=math.sqrt(n1)
            elif op==13:
                r=abs(n1)
            else:
                r=round(n1)
    else:
        print('invalid')
    print(r)
    n =int(input('0\t1\tzero 0r one:'))
    if n==0:
        break
