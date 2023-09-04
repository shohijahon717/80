n = int(input('n = '))
a = []

for i in range(1, n+1):
    element = int(input(f'{i}-element: '))
    a.append(element)

for j in a:
    s = 0

    for k in a:
        if k == j:
            s += 1
            
    print(f"{j}soni {s} marta")
    
    for q in a:
        if q == j:
           a.remove(j) 
            
            
    