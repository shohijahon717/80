
m = int(input("m = "))
n = int(input('n = '))

a = []
for i in range(1, m+1):
    q = []
    
    for j in range(1, n+1):
        k = int(input(f'{i}.{j} element: '))
        q.append(k)
    a.append(q)
 
m = a[0][0] 

for i in a:
    for j in i:
        if j < m:
            m = j
            
def index_2d(a, v):
    for i, x in enumerate(a):
        if v in x:
            return (i, x.index(v))

print(a)      
print(index_2d(a, m))

        
        
        



