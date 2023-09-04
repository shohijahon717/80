def SumRow(A,K):
    s = 0
    if K > m:
        return 0
    else:
        for i in A[K]:
            s += i
        return s    
            
m = int(input("m = "))
n = int(input('n = '))
K = int(input('K = '))

A = []
for i in range(1, m+1):
    q = []
    
    for j in range(1, n+1):
        k = int(input(f'{i}.{j} element: '))
        q.append(k)
    A.append(q)
print(A)
    
print(SumRow(A, K))

