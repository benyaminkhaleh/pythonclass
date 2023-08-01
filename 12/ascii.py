


def cands(x) :
    c = 0 #captal_letters
    s = 0 #small_letters
    for i in x:
        if 65 <= ord(i) <= 90 :
            c += 1
        elif 97 <= ord(i) <= 122 :
            s += 1
        else :
            continue
    return c , s
x = input('Enter your sntence: ')
print(cands(x))