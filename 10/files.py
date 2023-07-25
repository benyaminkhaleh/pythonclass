while True:
    name_files = input('Enter your name files: ')
    if '.' in name_files :
        new_files = name_files.split('.', 1)
        
        if '.' in new_files[1] :
            print('error\tyou have 2 "."in file name')
            continue
        elif new_files [1] == "err" :
            print('error\tyour extension should not be "err"')
            continue
        elif not(len(new_files[1]) == 3 or len(new_files[1]) == 2) :
            print('error\tyour extension should not be more less or than 2-3 letters')
            continue
        check = False
        for i in new_files[1] :
            if 48 <= ord(i) <= 57  :
                print('error\tyour file name must not start with a number')
                check = True
                break
        if check == True:
            continue
    print('your file name is a true')
    break

