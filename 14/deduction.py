class Deduction :
    def __init__(self,number1,denumber1,number2,denumber2):
        self.n1 = number1
        self.dn1 = denumber1
        self.n2 = number2
        self.dn2 = denumber2
    def sub(self):
        if self.dn1 == self.dn2 :
            result_num = self.n1 - self.n2
            result_denum = self.dn1
        else :
            result_num =  self.dn1 *self.n2 - self.dn2 *self.n1 
            result_denum = self.dn1 * self.dn2
        return result_num , result_denum 
    def sum(self):
        if self.dn1 == self.dn2 :
            result_num = self.n1 + self.n2
            result_denum = self.dn1
        else :
            result_num =  self.dn1 *self.n2 + self.dn2 *self.n1 
            result_denum = self.dn1 * self.dn2
        return result_num , result_denum 
    def mul(self):
        result_num = self.n1 * self.n2
        result_denum = self.dn1 * self.dn2
        return result_num , result_denum
    def div(self) :
        result_num = self.n1 * self.dn2
        result_denum = self.n2 * self.dn1
        return result_denum , result_num

op = int(input('1_sub\t2_sum\t3_mul\t4_div\tEnter your choose : '))
for i in range (4):
    if i%2 == 0 :
        if i == 0 :
            num1 = int(input(f"enter numerator : "))
        else :
            num2 = int(input(f"enter numerator : "))        
    else :
        if i == 1 :
            denum1 = int(input(f"enter denumerator : "))
        else :
            denum2 = int(input(f"enter denumerator : "))
deduction = Deduction(num1,denum1,num2,denum2)
if op == 1:
    a , b = deduction.sub()
    print(a, "\n-----\n", b)
elif op == 2:
    a , b = deduction.sum()
    print(a, "\n-----\n", b)
elif op == 3:
    a , b = deduction.mul()
    print(a, "\n-----\n", b)
elif op == 4:
    a , b = deduction.div()
    print(a, "\n-----\n", b)
