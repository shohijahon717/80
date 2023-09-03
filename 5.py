son = int(input('Son: '))

for i in range(1, son):
    a = 0
    for j in range(1, i):
    
        if i%j == 0:
            a = a + j
    if a == i:
        print(i)    
    
               