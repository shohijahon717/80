n = int(input('N = '))
for i in range(2, n):
    a = 0
    b = 0
    for j in range(1, i):
        if i % j == 0:
            a += j
    
    for k in range(1, a):
        if a % k == 0:
            b += k
    if i != a:
        if b == i:
            print(i,a)   
        
         