x = int(input('year:'))
if x % 100 != 0:
    if x % 4 == 0:
        print('leap year')
    else:
        print('not leap year')
else:
    if x % 400 == 0:
        print('leap year')
    else:
        print('not leap year')
