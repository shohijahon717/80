n = int(input("n = "))
p = 0
q = 0 

for i in range(1, n+1):
    a = int(input(f'{i}-son = '))  
    if i == 1:
        min = a
        max = a
    elif a > max:
        max = a
        p = i
    elif a < min:
        min = a
        q = i
       
if p > q:
    print(min, q)
else:
    print(max, p)
 