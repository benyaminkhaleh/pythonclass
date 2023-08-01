
def gcd(x, y):
   if x > y:
       gcd_ = x
   else:
       gcd_ = y

   while(True):
       if((x % gcd_ == 0) and (y % gcd_ == 0)):
           break
       gcd_ -= 1

   return gcd_


num1 = int(input())
num2 = int(input())
print("gcd: ", gcd(num1, num2))