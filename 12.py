n = int(input("n = "))


for i in range(1, n+1):
    a = int(input(f'{i}-son = '))    
    if i == 1:
        min = a
        max = a
    elif a >= max:
        max = a
    elif a < min:
        min = a
                
print(max, min)    