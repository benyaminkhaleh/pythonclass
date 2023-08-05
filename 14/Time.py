class Time:
    def __init__(self,hour_1,minute_1,second_1,hour_2,minute_2,second_2) :
        self.h1 = hour_1
        self.m1= minute_1
        self.s1 = second_1
        self.h2 = hour_2
        self.m2 = minute_2
        self.s2 = second_2
    def sum(self) :
        self.ht = self.h1 + self.h2
        self.mt = self.m1 + self.m2
        self.st = self.s1 + self.s2
        while not(0 <= self.st < 60 and 0 <= self.mt < 60):
            if self.st >= 60:
                self.st -= self.st % 60
                self.mt += self.st // 60
            if self.mt >= 60:
                self.mt -= self.mt % 60
                self.ht += self.mt // 60
                continue
        print(f'{self.ht} :  {self.mt}   :  {self.st}')
    def sub(self):
        self.ht = self.h1 - self.h2
        self.mt = self.m1 - self.m2
        self.st = self.s1 - self.s2
        while not(0 <= self.st <= 60 and 0 <= self.mt <= 60):
            if self.st < 0:
                self.mt -= 1
                self.st += 60
            if self.mt < 0:
                self.ht -= 1
                self.mt += 60
                continue
        print (f'{self.ht}  :  {self.mt}   :  {self.st}')
hour_1 = int(input('Enter your hour: '))
minute_1 = int(input('Enter your minute : '))
second_1 = int(input('Enter your second : '))
hour_2 = int(input('Enter your hour2 : '))
minute_2 = int(input('Enter your minute2 : '))
second_2 = int(input('Enter your second2 : '))
time = Time(hour_1,minute_1,second_1,hour_2,minute_2,second_2 )
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
if op == 1:
    time.sub()
elif op == 2:
    time.sum()



