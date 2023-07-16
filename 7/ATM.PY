cart='1245'
password_cart=int(input("Enter your password: "))
F = 1
password_cart=str(password_cart)
if password_cart==cart[::-1]:
    print("call to police")
else:
    while not F == 3 and not password_cart==cart:
        if not len(password_cart)==4:
            print('try again')
            password_cart=input("Enter your password: ")
        if not password_cart==cart:
            print("try again")
            password_cart=input("Enter your password: ")
            F += 1

if password_cart==cart:
    print('The password is correct')
else:
    print('Your account has been locked')
    