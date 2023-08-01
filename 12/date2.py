def date(year, month, day):
    print(year, "/", month, "/", day, sep="")
while True:
    day = int(input("enter number of day: "))
    if day > 31 :
        continue
    month = int(input("enter number of month: "))
    if month > 12 :
        continue
    year = int(input("enter number of year: "))
    date(year, month, day)
    break