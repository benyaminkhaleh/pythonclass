from datetime import date

today = date.today()

year = int(input('Enter your year : '))
month = int(input('Enter your month : '))
day = int(input('Enter your day : '))

days = (today.year - year) * 365 + (today.month - month) * 30 + (today.day - day)
weeks = days // 7
seconds = days * 24 * 60 ** 2
print(days, f'days has passed since this date {year}.{month}.{day}')
print(round(weeks), f'weeks has passed since this date {year}.{month}.{day}')
print(seconds, f'seconds has passed since this date {year}.{month}.{day}')