y = int(input('Yil: '))

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('366')
        else:
            print('365')
    else: 
        print('366')
else: 
    print('365')