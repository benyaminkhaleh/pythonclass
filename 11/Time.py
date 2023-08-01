class Time :
    def __init__(self,hour,second,minute) :
        self.h = hour
        self.m = minute
        self.s = second
        def sum(self) :
            while not(0 <= self.s < 60 and 0 <= self.m < 60):
                if self.s >= 60:
                    self.s -= self.s % 60
                    self.m += self.s // 60
                if self.m >= 60:
                    self.m -= self.m % 60
                    self.h += self.m // 60
            print(self.h + ":" + self.m  + ":" + self.s)
    def sub(self):
            while not(0 <= self.s <= 60 and 0 <= self.m <= 60):
                if self.s < 0:
                    self.m -= 1
                    self.s += 60
                    if self.m < 0:
                        self.h -= 1
                        self.m += 60
            print (self.h + ":" + self.m  + ":" + self.s)
hour_1 = int(input('Enter your hour: '))
minute_1 = int(input('Enter your minute : '))
second_1 = int(input('Enter your second : '))
t1 = str(hour_1) + ":" + str(minute_1) + ":" + str(second_1)
hour_2 = int(input('Enter your hour2 : '))
minute_2 = int(input('Enter your minute2 : '))
second_2 = int(input('Enter your second2 : '))
t2 = str(hour_2) + ":" + str(minute_2) + ":" + str(second_2)
time = Time(t1 , t2)
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
if op == 1:
    time.sub()
elif op == 2:
    time.sum()




