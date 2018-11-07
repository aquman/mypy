#CHECK FOR PRIME NUMBER
num = int(input('enter a number:-'))
for x in range(2,num):
    if num%x==0:
       print('{} is not a prime number'.format(num))
       break
else:
    print('{} is a prime number'.format(num))
