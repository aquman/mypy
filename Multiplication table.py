#MULTIPLICATION TABLE FOR ANY NUMBER(n) UPTO n*10
i=1
number = int(input('enter a number:'))
while i<11:
    print( number, '* {} is {}'.format(i,number*i))
    i = i+1
