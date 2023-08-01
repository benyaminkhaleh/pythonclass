r = int(input("Enter your number: "))
c = int(input("Enter your number: "))

for i in range(1, c+1):
    for j in range(1, r+1):
        print(j * i, end = "\t")

    print()