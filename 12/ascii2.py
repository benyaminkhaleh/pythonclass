def Vowels(x) :
    for i in x :
        if ord(i) == 97 :
            x = x.replace(i,'!')    
        elif ord(i) == 101 :
            x = x.replace(i,'!')
        elif ord(i) == 105 :
            x = x.replace(i,'!')
        elif ord(i) == 111 :
            x = x.replace(i,'!')
        elif ord(i) == 117 :
            x = x.replace(i,'!')
    return x
x = input('ENTER YOUR SENTENCE: ')
print(Vowels(x))
