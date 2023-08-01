def compute_lcm(x, y):
   if x > y:
       bigger = x
   else:
       bigger = y
   while(True):
       if((bigger % x == 0) and (bigger % y == 0)):
           lcm = bigger
           break
       bigger += 1
   return lcm
n1 =int(input('Enter your number : '))
n2 =int(input('Enter your number : '))
print("The LCM is", compute_lcm(n1, n2))