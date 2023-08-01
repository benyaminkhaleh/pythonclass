d =int(input('Enter yor number : '))
if d < 0 :
    d = abs(d)
for i in range(d):
      print((d - i) * " ", end='')
      print((i * 2 - 1) * '*')
for i in range(d, 0, -1):
    print((d - i) * " ", end='')
    print((i * 2 - 1) * '*')